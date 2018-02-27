from tkinter import filedialog
from tkinter import messagebox
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


    def draw_image_cordinates(image_path):

        root = Toplevel()
        root.title("Click two points")


        def mouse_handler(event):

            cordinates.append((event.x , event.y))

            if len(cordinates) == 2:
                draw_rect_on(image_path, cordinates)
                root.destroy()



        root.bind("<Button-1>" , mouse_handler)
        image_data =  Image.open(image_path)
        image = ImageTk.PhotoImage(image_data)
        w1 = Label(root , compound = CENTER, image = image).pack()

        root.mainloop()


    draw_image_cordinates(input_file)



def draw_rect_on(image_path , cordinates):

    for cordinate in cordinates:
        print(cordinate)
