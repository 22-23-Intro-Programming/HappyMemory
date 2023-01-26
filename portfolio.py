from graphics import *
import ProblemSet3
import ProblemSet2
import ImageEditor
import PalindromeGUI
import SharkSimulator


def main():
    
    mainWin = GraphWin("Python Portfolio", 800, 800)

 

    A = RectButton(mainWin, Point(50, 50), Point(100, 100))
    A.Draw()

    B = RectButton(mainWin, Point(150, 50), Point(200, 100))
    B.Draw()

    C = RectButton(mainWin, Point(50, 150), Point(100, 200))
    C.Draw()

    D = RectButton(mainWin, Point(150, 150), Point(200, 200))
    D.Draw()

    E = RectButton(mainWin, Point(50, 250), Point(100, 300))
    E.Draw()


  

    A = Text(Point(100, 200),("ProblemSet 3")
    A.draw(mainWin)

    B = Text(Point(100, 300),("ProblemSet 2")
    B.draw(mainWin)

    C = Text(Point(100, 400),("ImageEditor")
    C.draw(mainWin)

    D = Text(Point(100, 500),("PalindromeGUI")
    D.draw(mainWin)

    E = Text(Point(100, 600),("SharkSimulator") 
    E.draw(mainWin)


    
    Qbutton = button(win, Point(600, 450), Point(700, 550), "tomato", "Quit")
    r = button(win, Point(600, 350), Point(700, 450), "teal", "run")

    A.Text("ProblemSet 3")
    B.Text("ProblemSet 2")
    C.Text("ImageEditor")
    D.Text("PalindromeGUI")
    E.Text("SharkSimulator")
 
  
   
     
        p = mainWin.getMouse()
        if A.IsClicked(p):
           ProblemSet3.main()
        elif B.IsClicked(p):
          ProblemSet2.main()
        elif C.IsClicked(p):
            ImageEditor.main()
        elif D.IsClicked(p):
           PalindromeGUI.main()
        elif E.IsClicked(p):
            SharkSimulator.main()
            break
    mainWin.close()



if __name__ == "__main__":
    main()









    
