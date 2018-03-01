from tkinter import filedialog
from tkinter import messagebox
from tkinter import Label
from tkinter import CENTER


from tkinter import Toplevel


from PIL import Image
from PIL import ImageTk
from PIL import ImageDraw

from helper import get_new_name


'''
If you want to change the color of the rectangle
check the draw_rect_on function and change the
outline paremeter in ImageDraw inside it.
'''
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
        Label(root , compound = CENTER, image = image).pack()

        root.mainloop()


    draw_image_cordinates(input_file)



def draw_rect_on(image_path , cordinates):

    try:

        image = Image.open(image_path)

    except FileNotFoundError as e:
        messagebox.showerror(title = "Wrong image" , message = "{} path is not a valid image path.".format(image_path))
        return

    x1 , y1 = cordinates[0][0] , cordinates[0][1]
    x2, y2=  cordinates[1][0] , cordinates[1][1]

    draw_image = ImageDraw.Draw(image)
    draw_image.rectangle((x1 , y1  , x2 , y2) , outline = "black" )

    new_name =  get_new_name(image_path , "drawn")
    image.save(new_name)
    messagebox.showinfo(title = "Successful" , message = "Image saved as {}".format(new_name))

