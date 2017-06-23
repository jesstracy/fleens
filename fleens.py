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

	print("fleens[0].hair = %s" % fleens[0].hair)
	print("fleens[0].eyes = %s" % fleens[0].eyes)
	print("fleens[0].nose = %s" % fleens[0].nose)
	print("fleens[0].shoes = %s" % fleens[0].shoes)

	print("")

	print("zoombinis[0].hair = %s" % zoombinis[0].hair)
	print("zoombinis[0].eyes = %s" % zoombinis[0].eyes)
	print("zoombinis[0].nose = %s" % zoombinis[0].nose)
	print("zoombinis[0].shoes = %s" % zoombinis[0].shoes)

	for line in fleens[0].drawing:
		print line

	print("")

	for line in zoombinis[0].drawing:
		print line




if __name__ == '__main__':
    #unittest.main()  
    main()
