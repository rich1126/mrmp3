# mrmp3
Small utility to encode id3v2 version 3 MP3 chapters and metadata into MP3 files. Aimed at podcasting.

If you really like ffmpeg and happened upon this because of MP3 chapters, all I'm doing is creating a metadata file that is actually usable by ffmpeg, then running this bash file, which took me way too long to formulate.
```
#!/bin/bash

ffmpeg -i $1 -i $2 -map_metadata 1 -c:a libmp3lame -ar 44100 -b:a 64k -id3v2_version 3 -f mp3 $3
```

## Functionality

Given some audio file (typically a \*.wav after editing, but could be \*.mp3), a human-readable metadata file (described below) and a chosen output, **mrmp3** will create a metadata file readable by ffmpeg, and use the LAME MP3 encoder, through ffmpeg, to encode your chapters into the MP3 file. It will encode at a bitrate of 64k, and assumes the project is at 44100 HZ, but this can be changed if you care enough to dig into `encode_mp3.py`. 

This is mainly intended for podcasts, and is meant as a dirty replacement for [Forecast](https://overcast.fm/forecast), which is Mac-only. After hunting around, it seems there are essentially no programs that support adding *chapter markers* to MP3 files, despite it being supported in the MP3 spec for years. 

## Metadata File Format

The human-readable format is shown below. You can look at `metadata_example.txt` for a specific example from one of my podcasts.

```
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
```
I use this format because it's what I already did while editing to share timestamps with my co-hosts for review listens. The header items prior to the chapter list are for the sake of the typical MP3 metadata that many tools can provide.

## Usage

Clone the repository
`git clone https://github.com/rich1126/mrmp3`. Then, run `python3 mrmp3_cl.py [input_audio] [metadata_file] [output_audio]` from the command line, or `python3 mrmp3_gui.py` for the GUI version. Feel free to make tweaks to `functions/encode_mp3.py` if you prefer encoding at a different rate.

Also, note that if Qt is giving trouble for some reason, you can change the import in `mrmp3_gui.py` to be `import PySimpleGUI as sg` and everything will run the same, but use Tkinter to render everything.

If you make tweaks and want a single executable version, I used [Pyinstaller](http://www.pyinstaller.org/) to create the executable: `pyinstaller --onefile mrmp3_gui.py`. Note: I'm on Ubuntu 20.04.

If you really want the executable, you can find it [here](https://www.dropbox.com/s/drvo8unggdsml0s/mrmp3_gui?dl=0) (on Dropbox). I'm new to any sort of software, so that's what I've got for you! (I may make a Snap and/or Flatpack if I can figure out how.)

## Requirements
Uses the [LAME MP3 encoder](https://lame.sourceforge.io/) and [ffmpeg](https://ffmpeg.org/). Written in Python 3 using `PySimpleGUIQt`, although it's easy to change to `PySimpleGUI` for wider device support; both can be installed using pip. 

## Images

The basic user interface is, well, basic. Click on the browse button to browse for files, or just type in the paths yourself.

![Basic Interface](/images/mrmp3_input.png)

It'll say "Processing" while going (although if you run it from the command line, you'll see ffmpeg's own progress meter.)

![Processing](/images/mrmp3_processing.png)

And it'll tell you how speedy things went along. Sorry I'm not (yet) cool enough to multithread the LAME encoder, like Marco Arment was when writing Forecast.

![Complete](/images/mrmp3_complete.png)
