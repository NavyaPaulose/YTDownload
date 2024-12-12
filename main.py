import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import yt_dlp
import threading

def download_video():
    url = url_entry.get()
    if url:
        threading.Thread(target=download_thread, args=(url,), daemon=True).start()
    else:
        messagebox.showerror("Error", "Please enter a YouTube URL")

def download_thread(url):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'progress_hooks': [update_progress]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    messagebox.showinfo("Success", "Video downloaded!")

def update_progress(d):
    if d['status'] == 'downloading':
        percent = d['downloaded_bytes'] / d['total_bytes'] * 100
        progress_bar['value'] = percent
        percentage_label.config(text=f"{percent:.0f}%")
        root.update_idletasks()

root = tk.Tk()
root.title("YouTube Downloader")

root.configure(bg='#1e3d59')

window_width = 400
window_height = 250

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

label = tk.Label(root, text="Enter YouTube URL:", bg='#1e3d59', fg='white', font=('Arial', 12))
label.pack(pady=10)

url_entry = tk.Entry(root, width=50, bg='black', fg='white', font=('Arial', 12))
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Download", command=download_video, bg='lightgreen', font=('Arial', 12))
download_button.pack(pady=10)

progress_bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
progress_bar.pack(pady=10)

percentage_label = tk.Label(root, text="0%", bg='#1e3d59', fg='white', font=('Arial', 12))
percentage_label.pack(pady=5)

root.mainloop()
