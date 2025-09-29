'''import json
dados_json = '{ "nome":"Geovanna", "idade":15, "cidade":"Santana de Parnaíba" }'
dados_python = json.loads(dados_json)

print(dados_python["nome"])
print(dados_python["idade"])
print(dados_python["cidade"])
'''
import json 

pythonValue = {'isdog': 'true', 'cor': 'pretinha', 'nome': 'Pelezinha', 'cor dos olhos': 'laranjinha', 'raça': 'vira-lata', 'peso':  12, 'tamanho': 'médio', 'lugar favorito': 'varanda', 'idade': 4, 'tamanho do pelo': 'curto' }

strinsOFJsonDATA = json.dumps(pythonValue)
print(strinsOFJsonDATA)