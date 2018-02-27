from tkinter import filedialog
from tkinter import messagebox



def is_valid_image(path):

    valid_ext = [ "jpg" , "png" , "jpg" ]
    image_ext = path.split(".")[-1]

    return image_ext in valid_ext


def drawer_callback():

    input_file =  filedialog.askopenfilename()

    if is_valid_image(input_file) == False:
        messagebox.showerror(title = "Wrong image" , message = "Image not supported.")
        return

    print("found {}".format(input_file))

