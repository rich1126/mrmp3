"""
A function that calls ffmpeg to encode the .wav file
using the created metadata txt file.
"""

import subprocess

def encodeMP3(input_audio, metadata_file, output_audio):
    audio_encode=["ffmpeg", '-i', input_audio, '-i', metadata_file,'-map_metadata','1','-c:a',\
            'libmp3lame','-ar','44100','-b:a','64k','-id3v2_version', '3','-f',\
            'mp3',output_audio]

    print("STARTING")

    process = subprocess.run(audio_encode)

    if not process:  ## Ensures that the process is done running before return
        return True
     
