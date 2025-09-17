import types

def diz_o_tipo(a):
  tipo = type(a)
  if tipo == str:
    return("String")
  elif tipo == list:
    return("Lista")
  elif tipo == dict:
    return("Dicionário")
  elif tipo == int:
    return("Número inteiro")
  elif tipo == float:
    return("Número decimal")
  elif tipo == types.FunctionType:
    return("Função")
  elif tipo == types.BuiltinFunctionType:
    return("Função interna")
  else:
    return(str(tipo))
l = ['1,2,3']
loja = {"tomate": 1.29}
gosto_de_programar = True
def a():
  return
print(diz_o_tipo("Alô"))
print(diz_o_tipo(print))
print(diz_o_tipo(diz_o_tipo))
print(diz_o_tipo(12))
print(diz_o_tipo(1.23))
print(diz_o_tipo(l))
print(diz_o_tipo(range))
print(diz_o_tipo(loja))
print(diz_o_tipo(gosto_de_programar))
print(diz_o_tipo(a))
print(diz_o_tipo((1,2,3,4,5,6,7)))