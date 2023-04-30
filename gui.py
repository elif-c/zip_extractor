import PySimpleGUI as sg
from zip_extractor import extract_zip

sg.theme("DarkGreen")

select_zip = sg.Text("Select file to extract:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Browse", key="selected_file")

select_destination = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Browse", key="selected_folder")

extract_button = sg.Button("Extract")
message = sg.Text(key="message", text_color="DarkGreen", justification="right")

layout = [[select_zip, sg.Push(), input1, choose_button1],
          [select_destination, input2, choose_button2],
          [sg.Push(), message, extract_button]]

window = sg.Window("Zip Extractor",
                   text_justification="center",
                   layout=layout,
                   default_button_element_size=(6, 1))
while True:
    event_key, value = window.read()

    match event_key:
        case "Extract":
            filepath = value["selected_file"]
            folder = value["selected_folder"]
            extract_zip(filepath, folder)
            window["message"].update(value="Extraction successful!")
        case sg.WINDOW_CLOSED:
            break

window.close()
