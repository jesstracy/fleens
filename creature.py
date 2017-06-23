import random

# #ZOOMBINI
# print("   ******")
# print(" (  o  o  )")
# print(" (   ()   )")
# print("   ------")
# print("(_\\\\_||_//_)") 

# #FLEEN
# print("   ****")
# print("  |    |")
# print("  | oo |")
# print("  | [] |")
# print("  |    |")
# print("   ----")
# print("<___||___>")


PINK = '\033[95m' #0
BLUE = '\033[94m' #1
GREEN = '\033[92m' #2
YELLOW = '\033[93m' #3
RED = '\033[91m' #4
ENDC = '\033[0m'

class Creature():
    def __init__(self, id, hair, eyes, nose, shoes):
        self.id = id
        self.hair = hair
        self.eyes = eyes
        self.nose = nose
        self.shoes = shoes

class Fleen(Creature):
    def __init__(self, id, hair, eyes, nose, shoes):
        Creature.__init__(self, id, hair, eyes, nose, shoes)
        self.species = "Fleen"
        self.drawing = self._draw_me()
        # print GREEN + "green" + ENDC

    def _draw_me(self):
        drawing = []
        hair = self._draw_hair()
        eyes = self._draw_eyes()
        nose = self._draw_nose()
        shoes = self._draw_shoes()
        drawing.append(hair)
        drawing.append("  |    |")
        drawing.append(eyes)
        drawing.append(nose)
        drawing.append("  |    |")
        drawing.append("   ----")
        drawing.append(shoes)
        return drawing

    def _draw_hair(self):
        color = get_color(self.hair)
        return str(color) + "   ****" + str(ENDC)

    def _draw_eyes(self):
        color = get_color(self.eyes)
        return "  | " + str(color) + "oo" + str(ENDC) + " |"

    def _draw_nose(self):
        color = get_color(self.nose)
        return "  | " + str(color) + "[]" + str(ENDC) + " |"

    def _draw_shoes(self):
        color = get_color(self.shoes)
        return str(color) + "<___||___>" + str(ENDC)


class Zoombini(Creature):
    def __init__(self, id, hair, eyes, nose, shoes):
        Creature.__init__(self, id, hair, eyes, nose, shoes)
        self.species = "Zoombini"
        self.drawing = self._draw_me()

    def _draw_me(self):
        drawing = []
        hair = self._draw_hair()
        eyes = self._draw_eyes()
        nose = self._draw_nose()
        shoes = self._draw_shoes()
        drawing.append(hair)
        drawing.append(eyes)
        drawing.append(nose)
        drawing.append("   ------")
        drawing.append(shoes)
        return drawing

    def _draw_hair(self):
        color = get_color(self.hair)
        return str(color) + "   ******" + str(ENDC)

    def _draw_eyes(self):
        color = get_color(self.eyes)
        return " (  " + str(color) + "o  o" + str(ENDC) + "  )"

    def _draw_nose(self):
        color = get_color(self.nose)
        return " (   " + str(color) + "()" + str(ENDC) + "   )"

    def _draw_shoes(self):
        color = get_color(self.shoes)
        return str(color) + "(_\\\\_||_//_)" + str(ENDC)


def get_color(num):
    color = ""
    if num == 0:
        color = PINK
    elif num == 1:
        color = BLUE
    elif num == 2:
        color == GREEN
    elif num == 3:
        color = YELLOW
    elif num == 4:
        color = RED
    return color
