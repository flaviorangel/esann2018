from random import randint

def randomFeature(sizeOfFeature, isQuant):
	'''
	Generates a random binary encoded feature for test purposes

	Args:
		sizeOfFeature (int): gives the size of the feature to create
		isQuant (bool): if True, the feature is quantitative

	Return:
		(int[]): binary encoded feature
	'''

	middle = sizeOfFeature/2
	feature = [False]*sizeOfFeature
	position = randint(0, sizeOfFeature - 1)
	feature[position] = True

	if isQuant:
		if position > middle:
			while position != middle:
				position -= 1
				feature[position] = True
		elif position < middle:
			while position != middle:
				position += 1
				feature[position] = True
	
	return feature


def perturbQuali(binaryVector):
	'''
	Given a binary encoded qualitative feature, randomly change its value
	'''

	# Will somehow access the feature's size
	sizeOfFeature = len(binaryVector)

	while True:
		position = randint(0, sizeOfFeature - 1)
		if binaryVector[position] == False:
			break

	for i in range(0, sizeOfFeature):
		if i == position:
			binaryVector[i] = True
		else:
			binaryVector[i] = False


def perturbQuant(binaryVector):
	'''
	Given a binary encoded quantitative feature, randomly change its value
	'''

	# Will somehow access the feature's size
	sizeOfFeature = len(binaryVector)
	middle = sizeOfFeature/2

	position = middle
	while position == middle:
		position = randint(0, sizeOfFeature - 1)

	if position > middle:
		if binaryVector[position] == True:
			while position < sizeOfFeature and binaryVector[position] == True:
				binaryVector[position] = False
				position += 1
		else:
			while position > middle and binaryVector[position] == False:
				binaryVector[position] = True
				position -= 1
			if position == middle:
				position -= 1
				while position >= 0 and binaryVector[position] == True:
					binaryVector[position] = False
					position -= 1
	else:
		if binaryVector[position] == True:
			while position >= 0 and binaryVector[position] == True:
				binaryVector[position] = False
				position -= 1
		else:
			while position < middle and binaryVector[position] == False:
				binaryVector[position] = True
				position += 1
			if position == middle:
				position += 1
				while position < sizeOfFeature and binaryVector[position] == True:
					binaryVector[position] = False
					position += 1

# Number of tests to be executed
nTests = 10

# Size of test features
sizeOfTestFeature = 11

def main():
	isQuant = True
	for i in range(0, nTests):
		feature = randomFeature(sizeOfTestFeature, isQuant)
		print "this is my feature:"
		print feature
		print
		if isQuant:
			perturbQuant(feature)
		else:
			perturbQuali(feature)
		print "after change:"
		print feature
		print
		isQuant = not isQuant

if __name__ == "__main__":
    main()