from helper import load_image
from helper import get_new_name
from helper import callback


from tkinter import messagebox

def cropper_callback():

    callback(crop_image)


def crop_image(image_path , cordinates):

    image = load_image(image_path)

    if image is None:
        return


    x1 , y1 = cordinates[0][0] , cordinates[0][1]
    x2, y2=  cordinates[1][0] , cordinates[1][1]

    region = image.crop((x1 , y1 , x2 , y2))
    new_name = get_new_name(image_path , "Cropped")
    region.save(new_name)

    messagebox.showinfo(title = "Successful" , message = "Image saved as {}".format(new_name))


