from creature import Zoombini

NUM_ZOOMBINIS = 16

def main():
	#Make 16 random zoombinis
	zoombinis = []
	for i in range(0, NUM_ZOOMBINIS):
		new_zoom = Zoombini()
		zoombinis.append(new_zoom)

	count = 1
	for zoom in zoombinis:
		print("%i- %i" % (count, zoom.hair))
		count = count + 1


if __name__ == '__main__':
    #unittest.main()  
    main()
