from tkinter import *
import os

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

    if isStreamable(entryInput):
        os.system('mpv --fs=yes "{}"'.format(entryInput))

# Takes a window and centers it on the screen
def center(window):
    window.update_idletasks()

    # Size of the total screen
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()

    # Size of the application window
    size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2

    # Move to center
    window.geometry("%dx%d+%d+%d" % (size + (x, y)))

if __name__ == '__main__':
    root = Tk()
    root.geometry("300x200")
    root.title("Stream Player")

    # Create the entry for urls
    inputBox = Entry(root)
    # Put the inputBox in the gui
    inputBox.grid(row=1)

    # Bind return key to running startStream()
    root.bind('<Return>', startStream)

    # Center the window on the screen
    center(root)
    mainloop()
