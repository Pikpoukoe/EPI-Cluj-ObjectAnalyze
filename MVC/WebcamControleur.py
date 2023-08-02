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

    def button_pause_clicked(self):
        WebcamModele.__init__(self)
        success, image = WebcamModele.get_frame(self)
        frame_count = 0
        while success:
            cv2.imwrite(f"assets/frame_{frame_count}.jpg", image)
            success, image = WebcamModele.get_frame(self)
            frame_count += 1


class WebcamVue:
    def __init__(self, root, width=600, height=480):
        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(root, width=width, height=height)
        self.canvas.pack(anchor='nw')
        # set minimum window size value
        root.minsize(1200, 800)
        # set maximum window size value
        root.maxsize(1200, 800)

        # Create left and right frames
        self.left_frame = tk.Frame(root, width=500, height=400, bg='lightgrey')
        self.left_frame.pack(side='left', fill='both', padx=10, pady=5, expand=True)

        self.right_frame = tk.Frame(root, width=500, height=400, bg='lightgrey')
        self.right_frame.pack(side='right', fill='both', padx=10, pady=5, expand=True)

        self.tool_bar = tk.Frame(self.left_frame, width=50, height=50, bg='grey')
        self.tool_bar.pack(side='top', fill='both', padx=5, pady=5, expand=False)

    def clicked(self):
        print("Click")

    def button_pause_view(self):
        tk.Button(self.tool_bar, text="Pause", command=WebcamModele.button_pause_clicked(self)).pack(padx=5, pady=5)


class WebcamControleur:
    def __init__(self, root):
        self.photo = None
        self.root = root
        self.modele = WebcamModele()
        self.vue = WebcamVue(root)
        self.root.bind('<q>', self.close_windows)

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
