from graphics import *
from Button import *

def main():

    win = GraphWin("Character Creator", 800, 800)
    face = Oval(Point(100, 150), Point(500, 600))
    face.draw(win)

    eyes1 = Button(win, Point(525, 150), Point(625, 225), "blue", "Big Eyes")
    eyes2 = Button(win, Point(650, 150), Point(750, 225), "cyan", "Small Eyes")

    eyes3 = Button(win, Point(525, 275), Point(625, 350), "RoyalBlue3", "Blue Eyes")
    eyes4 = Button(win, Point(650, 275), Point(750, 350), "saddle brown", "Brown Eyes")


    nose1 = Button(win, Point(525, 400), Point(625, 475), "lime green", "Big Nose")
    nose2 = Button(win, Point(650, 400), Point(750, 475), "pale green", "Small Nose")

    smile1 = Button(win, Point(525, 525), Point(625, 600), "yellow", "Happy")
    smile2 = Button(win, Point(650, 525), Point(750, 600), "gold", "Sad")

    
    QButton = Button(win, Point(675, 20), Point(775, 95), "red", "Quit")

    #big eyes
    Eye1 = Oval(Point(230,250), Point(280, 290))
    Eye2 = Oval(Point(330,250), Point(380, 290))

    #small eyes
    eye1 = Oval(Point(240,250), Point(270, 270))
    eye2 = Oval(Point(340,250), Point(370, 270))

    eyes = [Eye1, Eye2, eye1, eye2]

    #big nose
    Nose1 = Polygon(Point(305, 310), Point(280, 360), Point(330, 360))

    #small nose
    Nose2 = Polygon(Point(305, 310), Point(295, 330), Point(315, 330))
    

    Noses = [Nose1, Nose2]

    #happy smile
    Smile1 = Polygon(Point(230, 415), Point(280, 445), Point(330, 445), Point(380, 415), Point(330, 430), Point(280, 430))

    #sad smile
    Smile2 = Polygon(Point(230, 460), Point(280, 445), Point(330, 445), Point(380, 460), Point(330, 430), Point(280, 430))

    Smiles = [Smile1, Smile2]
    

    
    while True:
        m = win.getMouse()
        if eyes1.isClicked(m):
            for e in eyes:
                e.undraw()
            
            Eye1.draw(win)
            Eye2.draw(win)

        elif eyes3.isClicked(m):
                for e in eyes:
                    e.setFill("RoyalBlue3")

        elif eyes4.isClicked(m):
                for e in eyes:
                    e.setFill("saddle brown")

        elif eyes2.isClicked(m):
            for e in eyes:
                e.undraw()

            eye1.draw(win)
            eye2.draw(win)

                
            
        elif nose1.isClicked(m):
            for n in Noses:
                n.undraw()
            
            Nose1.draw(win)

        elif nose2.isClicked(m):
            for n in Noses:
                n.undraw()

            Nose2.draw(win)

        elif smile1.isClicked(m):
            for s in Smiles:
                s.undraw()
            
            Smile1.draw(win)

        elif smile2.isClicked(m):
            for s in Smiles:
                s.undraw()

            Smile2.draw(win)


            

        elif QButton.isClicked(m):
            break

    win.close()
        

if __name__ == "__main__":
    main()
