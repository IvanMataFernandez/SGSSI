#!/usr/bin/python3

texto = "cdcuvgeg eqp ncu pqtocu pgeguctkcu. Jcdncoqu fg wp rcÍu rctckuqoÁvkeq gp gn swg c wpq ng ecgp rgfcbqu fg htcugu cucfcu gp nc dqec. Pk ukswkgtc nqu vqfqrqfgtququ ukipqu fg rwpvwcekÓp fqokpcp c nqu vgzvqu ukowncfqu; wpc xkfc, ug rwgfg fgekt, rqeq qtvqitÁhkec."
frecuencias = {
'A' : 0,
'B' : 0,
'C' : 0,
'D' : 0,
'E' : 0,
'F' : 0,
'G' : 0,
'H' : 0,
'I' : 0,
'J' : 0,
'K' : 0,
'L' : 0,
'M' : 0,
'N' : 0,
'Ñ' : 0,
'O' : 0,
'P' : 0,
'Q' : 0,
'R' : 0,
'S' : 0,
'T' : 0,
'U' : 0,
'V' : 0,
'W' : 0,
'X' : 0,
'Y' : 0,
'Z' : 0

}

for i in range(0, len(texto)):
	l = texto[i]
	if (l in frecuencias):
		frecuencias[l] = frecuencias[l] + 1



letras = {}

for i in range(0, 27):
	maxi = -1
	let = ' '

		
	for l in frecuencias:
		if frecuencias[l] > maxi:
			maxi = frecuencias[l]
			let = l


				
	letras[let] = i
	frecuencias[let] = -1	
	

lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
orden = ['E', 'A', 'O', 'L', 'S', 'N', 'D', 'R', 'U', 'I', 'T', 'C', 'P', 'M', 'Y', 'Q', 'B', 'H', 'G', 'F', 'V', 'J', 'Ñ', 'Z', 'X', 'K', 'W']



print("letras =  {")

	
for i in range(0,27):
	print("'" ,end="")
	print(lista[i], end="" )
	print("' : '" ,end="")
	print(orden[letras[lista[i]]], end="" )
	print("',")
	
print("}")
	
	
	
