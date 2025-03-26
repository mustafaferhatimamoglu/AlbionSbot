from PIL import ImageGrab, Image

def copy_image():
    img = ImageGrab.grabclipboard()
    print(img)
    print(isinstance(img, Image.Image))
    print(img.size)
    print(img.mode)
    #img.save('clipboard_image.jpg')
    img.save('clipboard.png')
    img_jpg = img.convert('RGB')
    img_jpg.save("clipboard.jpg")

if __name__ == "__main__":
    copy_image()