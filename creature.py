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
        return "   ****"

    def _draw_eyes(self):
        return "  | oo |"

    def _draw_nose(self):
        return "  | [] |"

    def _draw_shoes(self):
        return "<___||___>"


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
        return "   ******"

    def _draw_eyes(self):
        return " (  o  o  )"

    def _draw_nose(self):
        return " (   ()   )"

    def _draw_shoes(self):
        return "(_\\\\_||_//_)"
