from graphics import *
from Button import *

def main():

    win = GraphWin("Palindrome", 800, 600)
    win.setBackground("beige")

    Q = Button(win, Point(650, 500), Point(750, 575), "tomato", "Quit")
    P = Button(win, Point(350, 320), Point(450, 380), "cyan", "Check!")

    E = Entry(Point(400, 300), 30)
    E.draw(win)

    T = Text(Point(400, 250), "Write something below that you think is a palindrome.")
    T.draw(win)

    F = Text(Point(400, 450), "")
    F.draw(win)

    while True:
        m = win.getMouse()

        if Q.isClicked(m):
            break

        if P.isClicked(m):
            pal = E.getText()
            #test pal for palindrome
            #have a GUI output for the result
            start = pal[0]
            last = len(pal)-1
            i = 0
            for char in pal:
                if (pal[i] != pal[last-i]):
                    F.setText("That is not a palindrome!")
                    break
                i = i + 1
                F.setText("That is a palindrome!")
            


    win.close()
            




if __name__ == "__main__":
    main()
