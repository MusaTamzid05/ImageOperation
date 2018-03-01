
'''
All the function here are common to all operation such as  cropping or drawing.
All the operation needs two points from the image.Here we have all the code
that can take two points.
'''

from tkinter import filedialog
from tkinter import messagebox


from tkinter import Toplevel
from tkinter import Label
from tkinter import CENTER

from PIL import Image
from PIL import ImageTk

def get_new_name(image_path , operation):

    old_image_name= image_path.split("/")[-1]
    name ,ext = old_image_name.split(".")

    return name +  "_" + operation + "." + ext


def is_valid_image(path):

    valid_ext = [ "jpg" , "png" , "jpg" ]
    image_ext = path.split(".")[-1]

    return image_ext in valid_ext


def ask_user_for_path():


    input_file =  filedialog.askopenfilename()

    if input_file == "":
        return None


    if is_valid_image(input_file) == False:
        messagebox.showerror(title = "Wrong image" , message = "Image not supported.")
        return None

    return input_file




def callback(operation_function):

    '''
    The call back will be called by the all the gui callbacks.The arguments it takes
    is function that will do the operation such as cropping.Because we need
    the image cordinates for this, we will use this callback to get the image cordinates.
    Once we have the coordinates that we will call the operatin function.
    '''

    input_file = ask_user_for_path()

    if input_file is None:
        return


    cordinates = []


    def execute_operation(image_path):

        root = Toplevel()
        root.title("Click two points")


        def mouse_handler(event):

            cordinates.append((event.x , event.y))

            if len(cordinates) == 2:
                operation_function(image_path, cordinates)
                root.destroy()



        root.bind("<Button-1>" , mouse_handler)
        image_data =  Image.open(image_path)
        image = ImageTk.PhotoImage(image_data)
        Label(root , compound = CENTER, image = image).pack()

        root.mainloop()


    execute_operation(input_file)

def load_image(image_path):


    try:
        image = Image.open(image_path)
        return image

    except FileNotFoundError as e:
        messagebox.showerror(title = "Wrong image" , message = "{} path is not a valid image path.".format(image_path))
        return None
