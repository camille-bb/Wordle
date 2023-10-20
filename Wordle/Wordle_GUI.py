'''user Interface for Wordle Game'''


import JFrame from swing
import Wordle_Class

class GUI():

    def CreateFrame():
        frame = JFrame()
        frame.show
        frame.size = 200,200
        frame.title = "Wordle"
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)

