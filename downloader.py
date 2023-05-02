import tkinter as tk
import youtube_dl

def download_mp3():
    url = url_entry.get()
    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    }],
    'ignoreerrors': True  # อย่าลืมเพิ่ม parameter นี้เพื่อ ignore error
}

    ydl = youtube_dl.YoutubeDL(ydl_opts)
    ydl.download([url])

    

window = tk.Tk()
window.title("YT Downloader PTD")

url_entry = tk.Entry(window, width=50)
url_entry.pack()

download_button = tk.Button(window, text="Download MP3", command=download_mp3)
download_button.pack()

window.mainloop()
