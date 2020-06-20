# mrmp3
Small Linux utility to encode id3v2 version 3 MP3 chapters and metadata into MP3 files. Aimed at podcasting.

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

In the repository is the prebuilt executable, which you should be able to just download and run, given you have the requirements listed below. This uses PySimpleGUIQt, and will always assume the project is at 44100 HZ, and encodes at a 64k bitrate.

If you prefer, you can clone the repository
`git clone https://github.com/rich1126/mrmp3` and tweak `encode_mp3.py` to adjust the encoding settings you want. Then, run `python3 mrmp3_cl.py [input_audio] [metadata_file] [output_audio]` from the command line, or `python3 mrmp3_gui.py` for the GUI version.

If you make tweaks and want a single executable version, I used [Pyinstaller](http://www.pyinstaller.org/) to create the executable: `pyinstaller --onefile mrmp3_gui.py`.

## Requirements
Uses the [LAME MP3 encoder](https://lame.sourceforge.io/) and [ffmpeg](https://ffmpeg.org/). Written in Python 3.
