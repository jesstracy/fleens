import random

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

class Zoombini(Creature):
	def __init__(self, id, hair, eyes, nose, shoes):
		Creature.__init__(self, id, hair, eyes, nose, shoes)
		self.species = "Zoombini"
