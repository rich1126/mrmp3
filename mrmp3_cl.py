import functions.encode_mp3 as emp3
import functions.make_chapters as mc
import sys

"""
If the tag -e [encoding] is chosen:
    - Takes input from User for input audio, editing text file, and output file
    - Takes make_chapters functions to generate ffmpeg metadata file
    - Takes encode_mp3 function to actually encode the mp3

If the tag -d [datafying] is chosen:
    - Does the first two steps above
    - Simply adds mp3 chapters and other metadata to the output file
"""

def main():
    encode_or_data = sys.argv[1]
    input_audio = sys.argv[2]
    input_data = sys.argv[3]
    output_audio = sys.argv[4]

    if encode_or_data == '-e':
        output_data = sys.argv[3].split('.')[0]+"FF"+".txt" ## Name ffmpeg data file

        chapter_list, header_list = mc.parse_edit(input_data)
        mc.create_file(output_data, chapter_list, header_list)
        emp3.encodeMP3(input_audio, output_data, output_audio)

    elif encode_or_data == '-d':
        if input_audio == output_audio:
            print("WARNING: ffmpeg requires input and output to be different.")
        else:
            output_data = sys.argv[3].split('.')[0]+"FF"+".txt" ## Name ffmpeg data file

            chapter_list, header_list = mc.parse_edit(input_data)
            mc.create_file(output_data, chapter_list, header_list)
            emp3.dataMP3(input_audio, output_data, output_audio)
            
    else:
        print("WARNING: Require declaration of -e for encoding, or -d for adding data only.")

if __name__ == "__main__":
    main()
