from microbit import *

class GunGame():

    def __init__(self):
        pass

    def startGame(self):

        playing = True
        winner = ""

        display.clear()
        display.show("3")
        sleep(1000)
        display.show("2")
        sleep(500)
        display.show("1")

        while(playing):
            if button_a.is_pressed():
                winner = "A"
                display.show(Image.ARROW_W)
                playing = False

            if button_b.is_pressed():
                winner = "B"
                display.show(Image.ARROW_E)
                playing = False

        display.scroll("Winner is " + winner)


game = GunGame()

game.startGame()

