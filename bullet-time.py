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

        while(playing):
            buttons = self.handle_buttons()
            display.scroll(buttons)

    def handle_buttons(self)
        if button_a.is_pressed():
            display.show("A")

        if button_b.is_pressed():
            display.show("B")


game = GunGame()

game.startGame()

