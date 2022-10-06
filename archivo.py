#!/usr/bin/python3
# Este script desencripta el texto. Para ello pegar en la variable texto el mismo texto que se pegó en "archivo2.py". Seguido, sobrescribir el diccionario letras (linea 7)
# por el output recibido en archivo2.py. Finalmente, ejecutar el fichero con "$python3 archivo.py". El output será el texto inicial (sin descifrar) y debajo el texto
# descifrado con el mapeo usado en letras (es posible que el mapeo obtenido en el script 2 a partir del analisis de frecuencia no sea el correcto, por lo que habrá que
# ir probando editando los valores de la variable letras para poder sacar el texto descifrado).

# En la variable letras se almacena la clave del descifro. La clave del diccionario (valor de la izquierda) es el valor de la letra encriptada, y el objeto del diccionario
# (valor de la derecha) es el valor de la letra desencriptada.


texto = "cdcuvgeg eqp ncu pqtocu pgeguctkcu. Jcdncoqu fg wp rcÍu rctckuqoÁvkeq gp gn swg c wpq ng ecgp rgfcbqu fg htcugu cucfcu gp nc dqec. Pk ukswkgtc nqu vqfqrqfgtququ ukipqu fg rwpvwcekÓp fqokpcp c nqu vgzvqu ukowncfqu; wpc xkfc, ug rwgfg fgekt, rqeq qtvqitÁhkec."

texto = texto.upper()

letras =  {
'A' : 'O',
'B' : 'L',
'C' : 'S',
'D' : 'N',
'E' : 'D',
'F' : 'R',
'G' : 'U',
'H' : 'I',
'I' : 'T',
'J' : 'E',
'K' : 'C',
'L' : 'P',
'M' : 'M',
'N' : 'Y',
'Ñ' : 'Q',
'O' : 'B',
'P' : 'A',
'Q' : 'H',
'R' : 'G',
'S' : 'F',
'T' : 'V',
'U' : 'J',
'V' : 'Ñ',
'W' : 'Z',
'X' : 'X',
'Y' : 'K',
'Z' : 'W',
}





print(texto)
print("")

for i in range(0, len(texto)):
	if (texto[i] in letras):
		print(letras[texto[i]], end= '')
	
	else:	
		print(texto[i], end = '')
		


print("")

