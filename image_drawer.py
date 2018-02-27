from tkinter import filedialog
from tkinter import messagebox
from tkinter import Tk
from tkinter import Label
from tkinter import CENTER

from tkinter import Toplevel


from PIL import Image
from PIL import ImageTk


def is_valid_image(path):

    valid_ext = [ "jpg" , "png" , "jpg" ]
    image_ext = path.split(".")[-1]

    return image_ext in valid_ext


def drawer_callback():

    input_file =  filedialog.askopenfilename()

    if is_valid_image(input_file) == False:
        messagebox.showerror(title = "Wrong image" , message = "Image not supported.")
        return


    cordinates = []

    def get_image_cordinates(image_path):

        root = Toplevel()
        root.title("Click two points")
        #image = PhotoImage(file = image_path)

        image = ImageTk.PhotoImage(Image.open(image_path))
        w1 = Label(root , compound = CENTER, image = image).pack()

        root.mainloop()

    get_image_cordinates(input_file)

