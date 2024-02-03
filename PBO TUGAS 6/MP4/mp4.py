import tkinter as tk
from tkinter import messagebox
import cv2

class VideoPlayerApp:
    def __init__(self, root, video_path):
        self.root = root
        self.root.title("Video Player App")

        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)

        if not self.cap.isOpened():
            messagebox.showerror("Error", "Could not open video file.")
            self.root.destroy()
            return

        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        self.canvas = tk.Canvas(root, width=self.width, height=self.height)
        self.canvas.pack()

        self.btn_play = tk.Button(root, text="Play", command=self.play_video)
        self.btn_play.pack(pady=10)

        self.btn_pause = tk.Button(root, text="Pause", command=self.pause_video)
        self.btn_pause.pack(pady=10)
        self.btn_pause["state"] = "disabled"

        self.btn_stop = tk.Button(root, text="Stop", command=self.stop_video)
        self.btn_stop.pack(pady=10)
        self.btn_stop["state"] = "disabled"

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def play_video(self):
        self.btn_play["state"] = "disabled"
        self.btn_pause["state"] = "normal"
        self.btn_stop["state"] = "normal"
        self.update()
    
    def update(self):
        ret, frame = self.cap.read()
        if ret:
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            self.root.after(10, self.update)
        else:
            self.stop_video()

    def pause_video(self):
        self.btn_play["state"] = "normal"
        self.btn_pause["state"] = "disabled"
        self.btn_stop["state"] = "normal"
        self.canvas.delete("all")

    def stop_video(self):
        self.btn_play["state"] = "normal"
        self.btn_pause["state"] = "disabled"
        self.btn_stop["state"] = "disabled"
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.canvas.delete("all")

    def on_close(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.cap.release()
            self.root.destroy()

if __name__ == "__main__":
    video_path = "videocia.mp4"
    root = tk.Tk()
    app = VideoPlayerApp(root, video_path)
    root.mainloop()
