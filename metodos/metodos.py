from tkinter import filedialog


def openFile():
    try:
        file = filedialog.askopenfilename(title = "Seleccione su archivo", filetypes=(("PXLA FILES","*.pxla"),("TXT FILES","*.txt"),))
        content = open(file, "r").read()
        return content
    except FileNotFoundError:
        return None
    except IOError:
        return None 