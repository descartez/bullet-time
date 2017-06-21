from microbit import *
import random



class GunGame():

    def __init__(self):
        pass

    def startGame(self):
        playing = False
        winner = ""

        a_fire1 = Image("00000:"
                        "00000:"
                        "95000:"
                        "00000:"
                        "00000:")
        a_fire2 = Image("00000:"
                        "05000:"
                        "59000:"
                        "05000:"
                        "00000:")
        a_fire3 = Image("00500:"
                        "00000:"
                        "35900:"
                        "00000:"
                        "00500:")

        gunfire_a = [a_fire1, a_fire2, a_fire3]
        gunfire_b = []

        display.clear()
        display.show("3")
        sleep(1000)
        display.show("2")
        sleep(random.randint(500,2000))
        display.show("1")
        sleep(200)
        display.show(Image.SQUARE)

        playing = True

        while(playing):
            if button_a.is_pressed():
                winner = "A"
                display.show(gunfire_a, delay=100)
                sleep(1000)
                playing = False

            if button_b.is_pressed():
                winner = "B"
                display.show(Image.ARROW_E)
                sleep(1000)
                playing = False

        display.scroll(winner)
        sleep(500)
        display.clear()
        display.scroll(winner)
        sleep(500)
        display.clear()




game = GunGame()

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        game.startGame()

