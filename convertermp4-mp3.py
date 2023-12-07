from moviepy.editor import *
import tkinter as tk
from tkinter import filedialog
import sys

class Application:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("MP4 to MP3 converter")

        # Sekcja pliku wejściowego
        self.label = tk.Label(self.app, text="Nazwa pliku do konwersji")
        self.label.grid(row=0, column=0, padx=20, pady=10)

        self.input_file = tk.Entry(self.app, width=100)
        self.input_file.grid(row=0, column=1, pady=10)

        self.browse_button = tk.Button(self.app, text="...", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, pady=10)

        # Sekcja pliku wyjściowego
        self.output_location_label = tk.Label(self.app, text="Lokalizacja pliku wyjściowego")
        self.output_location_label.grid(row=1, column=0, padx=20, pady=10)

        self.output_file = tk.Entry(self.app, width=100)
        self.output_file.grid(row=1, column=1, pady=10)

        self.browse_output_button = tk.Button(self.app, text="...", command=self.browse_output)
        self.browse_output_button.grid(row=1, column=2, pady=10)

        # Przycisk konwersji
        self.convert_btn = tk.Button(self.app, text="Konwertuj", command=self.generate_video, width=40, height=5)
        self.convert_btn.grid(row=2, column=1, padx=20, pady=10)

        # Etykieta błędu
        self.error_label = tk.Label(self.app, text="Błędna nazwa pliku lub podany plik nie istnieje")

    def main(self):
        self.app.mainloop()


    def generate_video(self):
        if self.error_label:
            self.error_label.destroy()
        try:
            video_name = self.input_file.get()
            video = VideoFileClip(video_name)
            if self.output_file.get():
                video.audio.write_audiofile("output.mp3")
            else:
                video.audio.write_audiofile(video_name[0:-4] + "_output.mp3")
        except IOError:
            self.error_label = tk.Label(self.app, text="Błędna nazwa pliku lub podany plik nie istnieje")
            self.error_label.pack(padx=20, pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Pliki MP4", "*.mp4"), ("Wszystkie pliki", "*.*")])
        if file_path:
            self.input_file.delete(0, tk.END)
            self.input_file.insert(0, file_path)

    def browse_output(self):
        file_path = filedialog.askdirectory()
        if file_path:
            self.output_file.delete(0, tk.END)
            self.output_file.insert(0, file_path + "/")


app = Application()

app.main()

