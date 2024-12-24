""" 
Introdução ao desampacotamento 
"""
nome1, nome2, nome3 =['Maria','Helena','Luiz']
print(nome2)
#Para pegar o resto
nome1, *resto =['Maria','Helena','Luiz'] # Use o *_ enves  de *resto
print(resto)
#Para guarda o segudo valor ou terceiro assim por endiante
_,*resto2, _, nome4 =['Maria','Helena','Luiz','Pedro']
print(resto2)