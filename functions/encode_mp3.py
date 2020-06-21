import subprocess

def encodeMP3(input_audio, metadata_file, output_audio):
    """
    A function that calls ffmpeg to encode the .wav file
    using the created metadata txt file.

    Specifically, it is calling this:
    $ ffmpeg -i input_audio -i metadata_file -map_metadata 1 -c:a libmp3lame
      -ar 44100 -b:a 64k -id3v2_version 3 -f mp3 output_audio
      
    Change '44100' if your sample rate of your project is different.
    Change '64k' if you like different bitrate encoding.
    """
    audio_encode=["ffmpeg", '-i', input_audio, '-i', metadata_file,'-map_metadata','1','-c:a',
            'libmp3lame','-ar','44100','-b:a','64k','-id3v2_version', '3','-f',
            'mp3',output_audio]

    process = subprocess.run(audio_encode)

    if not process:  ## Ensures that the process is done running before return
        return True


def dataMP3(input_audio, metadata_file, output_audio):
    """
    A function that calls ffmpeg to add metadata to an existing .mp3 file
    using the created metadata txt file.

    Specifically, it is calling this:
    $ ffmpeg -i input_audio -i metadata_file -map_metadata 1 -c copy output_audio
    """
    data_encode=["ffmpeg", "-i", input_audio, "-i", metadata_file, "-map_metadata", "1",
            "-c", "copy", output_audio]

    process = subprocess.run(data_encode)

    if not process: ## Ensures that the process is done running before return
        return True

