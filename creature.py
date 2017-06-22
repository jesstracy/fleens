import random

class Creature():
	def __init__(self):
		self.hair = self._get_hair()
		self.eyes = self._get_eyes()
		self.nose = self._get_nose()
		self.shoes = self._get_shoes()

	def _get_hair(self):
		r = random.randint(0, 4)
		return r

	def _get_eyes(self):
		r = random.randint(0, 4)
		return r

	def _get_nose(self):
		r = random.randint(0, 4)
		return r

	def _get_shoes(self):
		r = random.randint(0, 4)
		return r

class Fleen(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.species = "Fleen"

class Zoombini(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.species = "Zoombini"

# fleen_1 = Fleen()
# print("Species: %s" % fleen_1.species)
# print("Hair: %s" % fleen_1.hair)
# print("Eyes: %s" % fleen_1.eyes)
# print("Nose: %s" % fleen_1.nose)
# print("Shoes: %s" % fleen_1.shoes)

# print("")

# zoom_1 = Zoombini()
# print("Species: %s" % zoom_1.species)
# print("Hair: %s" % zoom_1.hair)
# print("Eyes: %s" % zoom_1.eyes)
# print("Nose: %s" % zoom_1.nose)
# print("Shoes: %s" % zoom_1.shoes)