import tkinter as tk
from tkinter import messagebox, filedialog

from main import downloadVideo

def download_video():
    url = url_entry.get()
    if url == "":
        messagebox.showerror("Error", "Please enter a valid URL")
        return
    save_location = filedialog.askdirectory()
    if not save_location:
        messagebox.showerror("Error", "Please choose a valid save location")
        return
    try:
        downloadVideo(url, save_location, 1)
        status_label.config(text="Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Video Downloader")

url_label = tk.Label(root, text="Please paste the link of the video you want to download:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()