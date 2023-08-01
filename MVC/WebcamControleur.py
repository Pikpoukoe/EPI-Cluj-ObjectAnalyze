import tkinter as tk
from PIL import Image, ImageTk
import cv2

class WebcamModele:
    def __init__(self, video_source=0):
        self.vid = cv2.VideoCapture(video_source)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            frame = cv2.flip(frame, 1)
            if ret:
                # Return a boolean success flag and the frame
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                return False, None
        else:
            return False, None

    def close_windows(self):
        if self.vid.isOpened():
            self.vid.release()


class WebcamVue:
    def __init__(self, root, width=600, height=480):
        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(root, width=width, height=height)
        self.canvas.pack(anchor='nw')
        # set minimum window size value
        root.minsize(1200, 800)
        # set maximum window size value
        root.maxsize(1200, 800)

    def frame_left_right(self):
        # Create left and right frames
        left_frame = tk.Frame(root, width=200, height=400, bg='grey')
        left_frame.pack(side='left',  fill='both',  padx=10,  pady=5,  expand=True)

        right_frame = tk.Frame(root,  width=650,  height=400,  bg='grey')
        right_frame.pack(side='right',  fill='both',  padx=10,  pady=5,  expand=True)


class WebcamControleur:
    def __init__(self, root):
        self.photo = None
        self.root = root
        self.modele = WebcamModele()
        self.vue = WebcamVue(root)
        self.root.bind('<q>', self.close_windows)
        self.vue.frame_left_right()

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()

    def update(self):
        ret, frame = self.modele.get_frame()

        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.vue.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.root.after(self.delay, self.update)

    def close_windows(self, event=None):
        self.modele.close_windows()
        self.root.destroy()


root = tk.Tk()
root.title("Detect-o-bot")
root.config(bg="#dfebed")
app = WebcamControleur(root)
root.mainloop()
