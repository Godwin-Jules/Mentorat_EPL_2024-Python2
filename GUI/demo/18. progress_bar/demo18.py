from tkinter import *   # type:ignore
from tkinter import ttk
import time

from numpy import pad

def start():
    bar['value'] = 0
    download_size = 250
    speed = 2
    progress = (speed / download_size) * 100
    download = 0
    while download < download_size:
        time.sleep(0.05)
        bar['value'] += progress  # increase the progress bar value by 10
        download += speed
        percent.set(f"{int((download/download_size)*100)}%")
        text.set(f"{int(download)} over {download_size} GB downloaded")
        root.update_idletasks()    # this method'll update the GUI
    time.sleep(1)
    text.set("Download Complete")
    download_button.config(text="Download Again")



root = Tk()

percent = StringVar()
text = StringVar()

bar = ttk.Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
bar.pack(padx=5,pady=10)

percent_label = Label(root, textvariable=percent).pack(padx=5,pady=5)
task_label = Label(root, textvariable=text).pack(padx=5,pady=5)

download_button = Button(root, text="Download", command=start)
download_button.pack(padx=5,pady=5)

root.mainloop()