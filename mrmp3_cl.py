import functions.encode_mp3 as emp3
import functions.make_chapters as mc
import sys

"""
The main function the does the following:
    - Takes input from User for input audio, editing text file, and output file
    - Takes make_chapters functions to generate ffmpeg metadata file
    - Takes encode_mp3 function to actually encode the mp3
"""

def main():
    input_audio = sys.argv[1]
    input_data = sys.argv[2]
    output_audio = sys.argv[3]
    output_data = "FF"+sys.argv[2]  # Prepends 'FF' to denote ffmpeg text

    chapter_list, header_list = mc.parse_edit(input_data)
    
    mc.create_file(output_data,chapter_list,header_list)

    emp3.encodeMP3(input_audio, output_data, output_audio)


if __name__ == "__main__":
    main()
