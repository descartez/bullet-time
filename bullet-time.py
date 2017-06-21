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
        a_fire4 = Image("00000:"
                        "00000:"
                        "35669:"
                        "00000:"
                        "00000:")

        b_fire1 = Image("00000:"
                        "00000:"
                        "00059:"
                        "00000:"
                        "00000:")
        b_fire2 = Image("00000:"
                        "00050:"
                        "00095:"
                        "00050:"
                        "00000:")
        b_fire3 = Image("00500:"
                        "00000:"
                        "00953:"
                        "00000:"
                        "00500:")
        b_fire4 = Image("00000:"
                        "00000:"
                        "99663:"
                        "00000:"
                        "00000:")

        gunfire_a = [a_fire1, a_fire2, a_fire3, a_fire4]
        gunfire_b = [b_fire1, b_fire2, b_fire3, b_fire4]

        display.clear()
        display.show(Image.ALL_CLOCKS, loop=False, delay=random.randint(10,200))
        display.show(Image.SQUARE)

        playing = True

        while(playing):
            if button_a.is_pressed():
                winner = "A"
                display.show(gunfire_a, delay=30)
                display.clear()
                sleep(1000)
                playing = False

            if button_b.is_pressed():
                winner = "B"
                display.show(gunfire_b, delay=30)
                display.clear()
                playing = False

        display.scroll(winner)
        sleep(500)
        display.clear()
        display.scroll(winner)
        sleep(500)
        display.clear()

game = GunGame()

while True:
    both_arrows = Image("00000:"
                        "09090:"
                        "99999:"
                        "09090:"
                        "00000:")
    display.show(both_arrows)

    if button_a.is_pressed() and button_b.is_pressed():
        game.startGame()

