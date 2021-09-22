from time import sleep

tuples = [0]

max_val = 26
max_list = 3

pasws = 'malas'

while True:
	criteria = (tuples[i]==0)
		i+=1
		
		Try = ''
		for m in tuples:
			Try += chr(97+m)
		
		print(Try,end='\r')

	if Try==pasws:
		print(Try,end='\r')
		break

	i = 0
	criteria = True
	while i<len(tuples):
		
		if criteria:
			tuples[i]+=1
			tuples[i]%=max_val
		elif not criteria:
			break
		
		
		if all(list(map(lambda x:x==0,tuples))) and i==(len(tuples)-1):
			tuples.append(0)
			
		
		
