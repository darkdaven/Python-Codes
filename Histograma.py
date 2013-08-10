#3.3 - Escribir una funcion que dado un string cualquiera, imprima un histograma con las 3 letras
#que mas se repiten:
#Ejemplo: abracadabra.

def Histogram(word):
  	histogramDict = {}
	for letter in word:
		if not histogramDict.has_key(letter):
			histogramDict[letter] = 1
		else:
			histogramDict[letter] += 1
	
	Dirtupla = []

	for letterDict in histogramDict:
		t = tuple()
		t = (histogramDict[letterDict],letterDict,)
		Dirtupla.append(t)
	
	Dirtupla.sort()
	Dirtupla.reverse()
			
	top = Dirtupla[0][0]
	histogramToDisplay = ''
	letters = ''
	i = top

	while i > 0:
		for j in range(0,3):
			if  Dirtupla[j][0] >= i:
				histogramToDisplay += '*  '
			else:
				histogramToDisplay += '   '
			
			if i == top:
				letters +=  Dirtupla[j][1]+'  '

		
		histogramToDisplay +='\n'
		i-=1
	histogramToDisplay += letters
	
	print histogramToDisplay 
		
	


Histogram('abracadabralacabramasviejadelahabana')
