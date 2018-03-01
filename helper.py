

def get_new_name(image_path , operation):

    old_image_name= image_path.split("/")[-1]
    name ,ext = old_image_name.split(".")

    return name +  "_" + operation + "." + ext

