from flask import Flask
import banco_consultas as bd

app = Flask(__name__)

@app.route("/faturamento/<int:mes>")
def faturamento_mensal(mes):
    try:
        dados = bd.faturamento_mensal_produto(mes)
        lista = []
        for reg in dados:
            dic = {
                'loja': reg[0],
                'produto': reg[1],
                'faturamento': reg[2]
            }
            lista.append(dic)
    except Exception as erro:
        return {"erro": str(erro)}, 400
    return lista, 200

app.run(debug=True)
