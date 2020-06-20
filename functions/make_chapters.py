"""
A series of functions that provides the functionality to
make a metadata file that is readable by ffmpeg
containing chapter and title information

Assumes an input_file formatted as follows:

ALBUM
ARTIST
TITLE
TOTAL TIME in h:mm:ss
YEAR
---Chapter List---  (or empty line)
h:mm:ss - Chapter 1 title
h:mm:ss - Chapter 2 title
	.
	.
	.
	.
"""


# A function to get the seconds out of a regular time-stamp
def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.strip().split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

# Creates a list containing the metadata information for one chapter
def chapter_add(chapter_name, start_time, end_time):
    start_time = get_sec(start_time)*1000
    end_time = get_sec(end_time)*1000

    chapter_list = ["[CHAPTER]\n","TIMEBASE=1/1000\n",f"START={start_time}\n",\
            f"END={end_time}\n", f"title={chapter_name}"]

    return chapter_list

# Creates a list containing the metadata information for the header
def header(album, artist, title, total_len, date):
    header_list = [";FFMETADATA1\n", f"album={album}", f"artist={artist}",\
            f"title={title}", f"TLEN={total_len}\n", "encoded_by=mrmp3\n",\
            f"date={date}", "encoder=lame\n"]

    return header_list

# A function to take the standard mrmp3 "editing metadata" format
# and turn it into the prescribed ffmpeg metadata
def parse_edit(input_file):
    inFile = open(input_file,'r')
    line_list = [line for line in inFile]
    inFile.close()
    
    header_list = header(line_list[0], line_list[1], line_list[2], \
            get_sec(line_list[3])*1000, line_list[4])

    chapter_list = []

    for i in range(len(line_list[6:-1])):
        [start_time, chapter_name] = line_list[i+6].split(' - ',1)
        end_time = line_list[i+7].strip().split(' - ',1)[0]

        chapter_list.append(chapter_add(chapter_name, start_time, end_time))

    [start_time,chapter_name] = line_list[-1].strip().split(' - ',1)
    end_time = line_list[3]

    chapter_list.append(chapter_add(chapter_name, start_time, end_time))

    return chapter_list, header_list


# Creates metadata file assuming a list of chapter_list items and a header list
def create_file(output, chapterList, header):
    output_file = open(output,'w')
    for line in header:
        output_file.write(line)

    for chapter in chapterList:
        for line in chapter:
            output_file.write(line)

    output_file.close()
