import sys
import os
from PIL import Image as pic

'''
    File will processes the PNG files located in the listed directory so they are cropped to the size specified in the code
'''

filepath = "C:\\my documents\\pictures\\AZ-900_PresentationDeck\\"

def image_crop():
    global filepath

    # Loop through all provided arguments
    for filename in os.listdir(filepath):
        if "." not in filename:
            continue
        ending = filename.split(".")[1]
        if ending not in ["png"]:
            continue

        try:
            # Attempt to open an image file
            image = pic.open(os.path.join(filepath, filename))
        except IOError:
            # Report error, and then skip to the next argument
            print("Problem opening", filepath)
            continue

        def pic_size(picture):
            width, height = picture.size
            return width * height

        # Perform operations on the image here
        if pic_size(image) == 2029440:
            image = image.crop((624, 191, 1392, 625))
        else:
            continue

        # Split our origional filename into name and extension 
        name, extension = os.path.splitext(filename)

        # Save the image as "(origional_name)_thumb.jpg
        print(name + '_cropped.png')
        image.save(os.path.join(filepath, name + '_cropped.png'))


def failed_file_cleanup():
    '''
        Function to be called in the event that the cropped images are incorrect and need to be cleared so they can be processed once again
    '''
    global filepath
    
    for filename in os.listdir(filepath):
        if filename[3:] == "_cropped.png":
            print("File:", filename, "has been identified for deletion")
            os.remove(filename)
            print("File:", filename, "has been deleted successfully")


def success_file_cleanup():
    '''
        Function to be called in the event that the cropped images are correct and the original images will need to be removed
    '''
    global filepath

    for filename in os.listdir(filepath):
        if len(filename) == 7 and "vscode" not in filename:
            print("File:", filename, "has been identified for deletion")
            os.remove(filename)
            print("File:", filename, "has been deleted successfully")


def cropped_image_file_rename():
    '''
        Function to  be called to rename all files ending in "_cropped.png" to just ".png"
    '''

    global filepath

    for filename in os.listdir(filepath):
        if filename[3:] == "_cropped.png":
            print("File:", filename, "has been identified for renaming")
            os.rename(filename, filename[0:3] + ".png")
            print("File:", filename, "has been renamed successfully")