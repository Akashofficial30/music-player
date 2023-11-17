import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        self.master.geometry("400x500")
        
    


        self.playlist = []  # List to store song information and file paths
        self.current_index = 0

        pygame.mixer.init()

        self.create_widgets()

    def create_widgets(self):
        self.playlistbox = tk.Listbox(self.master, selectmode=tk.SINGLE, bg="pink", selectbackground="blue")
        self.playlistbox.pack(pady=20)

        self.add_button = tk.Button(self.master, text="Add Music", command=self.add_music,foreground="black",font="bold")
        self.add_button.pack(pady=10)

        self.play_button = tk.Button(self.master, text="Play", command=self.play_music,foreground="black",font="bold")
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_music,foreground="black",font="bold")
        self.stop_button.pack(pady=10)

        self.next_button = tk.Button(self.master, text="Next", command=self.next_music,foreground="black",font="bold")
        self.next_button.pack(pady=10)

        self.prev_button=tk.Button(self.master,text="prev",command=self.prev_music,foreground="black",font="bold")
        self.prev_button.pack(pady=10)
        self.load_playlist()

    def load_playlist(self):
        try:
            with open("playlist.txt", "r") as file:
                self.playlist = [line.strip().split('|') for line in file.readlines()]
                self.playlistbox.delete(0, tk.END)
                for song_info, file_path in self.playlist:
                    self.playlistbox.insert(tk.END, song_info)
        except FileNotFoundError:
            print("Playlist file not found. Create a 'playlist.txt' file with song paths.")

    def save_playlist(self):
        with open("playlist.txt", "w") as file:
            for song_info, file_path in self.playlist:
                file.write(f"{song_info}|{file_path}\n")

    def add_music(self):
        file_path = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            song_info = os.path.basename(file_path)
            self.playlist.append((song_info, file_path))
            self.playlistbox.insert(tk.END, song_info)
            self.save_playlist()

    def play_music(self):
        if self.playlist:
            song_info, file_path = self.playlist[self.current_index]
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

    def next_music(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.play_music()
    def prev_music(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
