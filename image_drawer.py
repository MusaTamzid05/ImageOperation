from PIL import ImageDraw

from helper import get_new_name
from helper import callback
from helper import load_image


from tkinter import messagebox

def drawer_callback():

    callback(draw_rect_on)

def draw_rect_on(image_path , cordinates):

    image = load_image(image_path)

    if image is None:
        return


    x1 , y1 = cordinates[0][0] , cordinates[0][1]
    x2, y2=  cordinates[1][0] , cordinates[1][1]

    draw_image = ImageDraw.Draw(image)
    draw_image.rectangle((x1 , y1  , x2 , y2) , outline = "black" )

    new_name =  get_new_name(image_path , "drawn")
    image.save(new_name)
    messagebox.showinfo(title = "Successful" , message = "Image saved as {}".format(new_name))

