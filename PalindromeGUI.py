from graphics import *
from Button import *

def main():

      win = GraphWin("Palindrome", 800, 600)
      win.setBackgrounf("beige")

      Q = Button(win, Point(650, 500), Point(750, 575), "tomato", "Quit")
      P = Button(win, Point(350, 350), Point(450, 425), "cyan", "Check!")

      E = Entry(point(400, 300),30)
      E.draw(win)

      T = TextPoint(400, 250), "wtite something below that you think is a palindrome."
      T.draw(win)
      
     Ts = Text(Point400,450),"This is palindrome :(")
     Tf = Text(Point400,450),"This is not palimdrome:(")
      

      while True:
          m = win.getMouse()

          if Q.isClick(m)
             break

        if P.isClick(m):
            pal = E.getText()
          #test pal for palndrome
          #have a GUI output
            

     win.close()





if __name__ == "__main__":
   main()
    
