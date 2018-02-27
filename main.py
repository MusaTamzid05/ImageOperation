from tkinter import Tk
from tkinter import X
from tkinter import Button
from tkinter import Frame

from image_cropper import cropper_callback
from image_drawer import drawer_callback
from logo_callback import  image_logo_callback



def main():



    callbacks = {}

    #add the callbacks here.
    callbacks["Draw on image"]  = drawer_callback
    callbacks["Crop Image" ]  =  cropper_callback
    callbacks["Add logo"]  = image_logo_callback

    root = Tk()

    # we want the row size to be little bit
    # bigger that the number of button out
    # there.So little bit of hacking
    # to achive this.

    row_size = (len(callbacks) * 10) + 100
    root.title("Image Pro 1 tail")
    root.geometry("800x" + str(row_size))
    parent = Frame(root)

    for text , callback in callbacks.items():
        Button(parent , text = text  , command = callback).pack(fill = X , expand = 1)


    parent.pack(fill = X , expand = 1)
    root.mainloop()


if __name__ == "__main__":
    main()
