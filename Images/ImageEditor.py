from graphics import *
from Button import *

def darken(img):

    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            r = r - 50
            g = g - 50
            b = b - 50
            if r < 0:
                r = 0
            if g < 0:
                g = 0
            if b < 0:
                b = 0
            newColor = color_rgb(r, g, b)
            img.setPixel(i, j, newColor)


def lighten(img):

    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            r = r + 50
            g = g + 50
            b = b + 50
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255
            newColor = color_rgb(r, g, b)
            img.setPixel(i, j, newColor)


def grayscale(img):
    
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            h = r + g + b
            h = h//3
            r = h
            g = h
            b = h
            
            newColor = color_rgb(r,g, b)
            img.setPixel(i, j, newColor)

def contrast(img):
    
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            h = r + g + b
            h = h//3
            if h < 128:
                r = r - 20
                g = g - 20
                b = b - 20
            if h > 128:
                r = r + 20
                g = g + 20
                b = b + 20
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255
            if r < 0:
                r = 0
            if g < 0:
                g = 0
            if b < 0:
                b = 0
            newColor = color_rgb(r,g, b)
            img.setPixel(i, j, newColor)

def neon(img):
    
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            r = r - 50
            g = g - 50
            b = b - 50
            if r < 0:
                r = 255
            if g < 0:
                g = 255
            if b < 0:
                b = 255
            newColor = color_rgb(r, g, b)
            img.setPixel(i, j, newColor)

def red(img):

    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            h = r + g + b
            h = h//3
            if (r < (g + 25)) or (r < (b + 25)):
                g = h
                b = h
                r = h
            newColor = color_rgb(r, g, b)
            img.setPixel(i, j, newColor)

def main():

    win = GraphWin("Image Editor", 800, 800)
    win.setBackground("DarkOrange2")

    I = Image(Point(300,300), "veitchii.png")
    I.draw(win)

    B = Button(win, Point(600, 50), Point(700, 125), "blue", "Darken")
    B2 = Button(win, Point(600, 150), Point(700, 225), "cyan", "Lighten")
    B3 = Button(win, Point(600, 250), Point(700, 325), "yellow", "Grayscale")
    B4 = Button(win, Point(600, 350), Point(700, 425), "violet", "Contrast")
    B5 = Button(win, Point(600, 450), Point(700, 525), "green2", "Demonic")
    B6 = Button(win, Point(600, 550), Point(700, 625), "IndianRed1", "Highlight Red")
    B7 = Button(win, Point(600, 650), Point(700, 725), "lemon chiffon", "Reset")
    

    
    QButton = Button(win, Point(450, 650), Point(550, 725), "red", "Quit")

    
    while True:
        m = win.getMouse()
        
        if B.isClicked(m):
            darken(I)

        elif B2.isClicked(m):
            lighten(I)

        elif B3.isClicked(m):
            grayscale(I)

        elif B4.isClicked(m):
            contrast(I)

        elif B5.isClicked(m):
            neon(I)

        elif B6.isClicked(m):
            red(I)

        elif B7.isClicked(m):
            I = Image(Point(300,300), "veitchii.png")
            I.draw(win)
            
        elif QButton.isClicked(m):
            break

    win.close()
        

if __name__ == "__main__":
    main()

