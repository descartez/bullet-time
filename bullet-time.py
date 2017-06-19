from microbit import *

class GunGame():

    def __init__(self):
        pass

    def startGame(self):

        playing = True

        display.clear()
        display.show("3")
        sleep(1000)
        display.show("2")
        sleep(500)
        display.show("1")


game = GunGame()

game.startGame()

