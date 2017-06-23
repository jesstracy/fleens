from creature import Zoombini, Fleen
import random

NUM_ZOOMBINIS = 16
HAIR_DIFF = random.randint(0, 4)
EYE_DIFF = random.randint(0, 4)
NOSE_DIFF = random.randint(0, 4)
SHOES_DIFF = random.randint(0, 4)

def main():
	#Make 16 random zoombinis and corresponding fleens
	zoombinis = []
	fleens = []
	for i in range(0, NUM_ZOOMBINIS):
		h = random.randint(0, 4)
		e = random.randint(0, 4)
		n = random.randint(0, 4)
		s = random.randint(0, 4)
		new_zoom = Zoombini(i, h, e, n, s)
		zoombinis.append(new_zoom)
		#all fleen 0 hairs should correspond to zoombini 2
		new_fleen = Fleen(i, (h + HAIR_DIFF) % 5, (e + EYE_DIFF) % 5, (n + NOSE_DIFF) % 5, (s + SHOES_DIFF) % 5)
		fleens.append(new_fleen)

	print("Hair difference: %i" % HAIR_DIFF)
	for i in range(0, 3):
		print("Zoombini%i hair: %i" % (i + 1, zoombinis[i].hair))
		print("Fleen%i hair: %i" % (i + 1, fleens[i].hair))

	print("")

	print("Eye difference: %i" % EYE_DIFF)
	for i in range(0, 3):
		print("Zoombini%i eyes: %i" % (i + 1, zoombinis[i].eyes))
		print("Fleen%i eyes: %i" % (i + 1, fleens[i].eyes))

	for line in fleens[0].drawing:
		print line

	print("")

	for line in zoombinis[0].drawing:
		print line




if __name__ == '__main__':
    #unittest.main()  
    main()
