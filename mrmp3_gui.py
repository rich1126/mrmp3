import functions.encode_mp3 as emp3
import functions.make_chapters as mc
import PySimpleGUIQt as sg  ## Can change to PySimpleGUI for Tkinter
import time


"""
A helper function
    - Takes the "editing text file" with user-readable timestamps
    - Creates the ffmpeg metadata file at output_data
"""

def get_file(input_data):
    output_data = input_data.split('.')[0]+"FF.txt"

    chapter_list, header_list = mc.parse_edit(input_data)
    
    mc.create_file(output_data,chapter_list,header_list)

    return output_data

  
"""
Main function
    - Creates GUI with fields for...
        - Input audio selection (*.wav typically)
        - Input data selection (*.txt, becomes the "output_data" file above)
        - Export audio location/name (*.mp3)
        
    - Calls the encodeMP3 function, which is just a wrapper around a very long
      ffmpeg call to the command line
    - Ends with a report on how long the encoding took
"""

def main():
    sg.theme('Reddit')

    layout = [[sg.Text('', font=('Times', 12), key='timer')],
            [sg.Text('Input Audio', size=(10,1),font='Times 14'),
                    sg.InputText(key="audioIN",size=(50,1)),
                    sg.FileBrowse(initial_folder="/home",target="audioIN")],
            [sg.Text('Input Data', size=(10,1),font='Times 14'),
                    sg.InputText(key="dataIN",size=(50,1)), 
                    sg.FileBrowse(initial_folder="/home",target="dataIN")],
            [sg.Text('Encode To', size=(10,1),font='Times 14'),
                    sg.InputText(key="audioOUT",size=(50,1)),
                    sg.FolderBrowse(initial_folder="/home",target="audioOUT")],
            [sg.Submit('Encode',size=(10,1)), sg.Cancel('Quit',size=(10,1))]]

    window = sg.Window('mrmp3',layout)

    ####### Main Event Loop ########
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Quit":
            break
            
        ######### When User hits "Encode" button ######### 
        if event == "Encode":
            ## Get time for timing encoding
            start_time = int(round(time.time() * 100))
            
            ## Get variables for encodeMP3 call
            input_audio = values["audioIN"]
            input_data = values["dataIN"]
            output_audio = values["audioOUT"]
            output_data = get_file(input_data)
            
            ## Update window to prepare for processing
            window['timer'].Update('Processing...')
            window.Refresh()

            ## Call ffmpeg to encode to mp3
            emp3.encodeMP3(input_audio, output_data, output_audio)
            
            ## Calculate and report encoding completion time           
            final_time = int(round(time.time()*100)) - start_time
            format_time = '{:02d}:{:02d}.{:02d}'.format((final_time // 100) // 60,
                    (final_time // 100) % 60, final_time % 100)

            window['timer'].update(f"Completed in {format_time}.")

    window.close()

if __name__ == "__main__":
    main()

