""" 
Introdução ao desampacotamento + tuples (tuplas)
"""
nome1, nome2, nome3 =['Maria','Helena','Luiz']
print(nome2)
#Para pegar o resto
nome1, *resto =['Maria','Helena','Luiz'] # Use o *_ enves  de *resto
print(resto)