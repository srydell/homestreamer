from tkinter import *
# import os
import subprocess

# Check if the url is a valid video link
def isStreamable(entryInput):
    # Supported URLs.
    goodURLs = ["youtube.com/playlist?list=", "youtube.com/watch?v="]
    for url in goodURLs:
        # If url is a substring in entryInput
        if url in entryInput:
            return True
    return False

# If the value in inputBox isStreamable
# then start the stream.
# Is called on <Return> press
def startStream(event):
    entryInput = inputBox.get()

    # Clear the text
    inputBox.delete(0, len(entryInput))

    # Call mpv if streamable
    if isStreamable(entryInput):
        # exitCode = os.system('mpv --fs=yes "{}"'.format(entryInput))
        cmd = 'open -a vlc {}'.format(entryInput)
        subprocess.call(cmd.split())

# Size of the application window
def getSizeOfWindow(window):
    return tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))

# Takes a window and centers it on the screen
def centerWindow(window):
    window.update_idletasks()

    # Size of the total screen
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()

    # Size of the application window
    size = getSizeOfWindow(window)
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    window.geometry("%dx%d+%d+%d" % (size + (x, y)))

# Automatically resize widgets when resizing root window
def resize(event):
    currentSize = getSizeOfWindow(root)

    # Padding around x axis
    padding = 10

    inputBoxSize = (currentSize[0] - padding, 30)

    # Put the inputbox in the middle of the window
    # with padding
    inputBox.place(x=padding/2, y=(currentSize[1] - inputBoxSize[1])/2, width=inputBoxSize[0], height=inputBoxSize[1])

if __name__ == '__main__':
    root = Tk()
    root.geometry("500x400")
    root.title("Stream Player")

    # Center the application on the screen
    centerWindow(root)

    # Create the entry for urls
    inputBox = Entry(root)
    # Put the inputBox in the gui
    # inputBox.pack()

    # Bind return key to running startStream()
    root.bind('<Return>', startStream)

    # Whenever resizing root window, call resize
    # to resize the widgets as well
    root.bind('<Configure>', resize)

    mainloop()
