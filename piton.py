import tkinter as tk
from PIL import Image, ImageTk

class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cookie Clicker")
        master.geometry("400x300")  # Set the size of the window
        master.resizable(False, False)  # Disable window resizing

        # Set the favicon (replace "cookie.ico" with the actual filename)
        master.iconbitmap("Assets/Cookie.ico")

        self.cookies = 0  # Variable to store the number of cookies

        # Load a PNG image using Pillow
        image = Image.open("Assets/Cookie.png")
        self.button_image = ImageTk.PhotoImage(image)

        self.label = tk.Label(master, text="Cookies: 0", font=("Lucida Console", 16))
        self.label.pack(pady=10)

        self.button = tk.Button(master, image=self.button_image, command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        self.cookies += 1
        self.label.config(text=f"Cookies: {self.cookies}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = MyGUI(root)
    root.mainloop()
