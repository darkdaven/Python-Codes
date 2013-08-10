# 3.4 - Dada una lista de enteros, escribir una funcion que retorna una nueva lista, con los
# elementos de la primera lista ordenados de menor a mayor. La funcion solo podra recorrer la
# lista una sola vez.

def OrderList(intList):
    ilist = intList
    newList = []
    topIndex = len(ilist) - 1
    removeIndex = 0
    nowIndex = 0
    nowValue = ilist[0]
	
	while True:
	    if nowValue > ilist[nowIndex]:
			nowValue = ilist[nowIndex]
			removeIndex = nowIndex
		else:
			nowIndex +=1
		
		if nowIndex == topIndex:
			newList.append(nowValue)
			ilist.pop(removeIndex)
			nowIndex = 0 
			topIndex = len(ilist) -1
			
			if topIndex <= 0:
				newList.append(ilist[0])
				break

			nowValue = ilist[0]
	  
	return newList
