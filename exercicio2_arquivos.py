import oracledb as db

with db.connect(user='pf0313', 
        password='professor#23',
        dsn='oracle.fiap.com.br/orcl') as con:
    
    with con.cursor() as cur:

        sql = '''insert into faturamento
        (produto, marca, loja, data, qtd, valor) values
        (:prod, :marca, :loja, to_date(:data,'yyyy-MM-dd'), 
        :qtd, :valor)'''

        with open('faturamento_anual.txt') as arq:
            lista = []
            for lin in arq:
                dado = lin.replace('\n', '').split(";")
                dic = {}
                dic['prod'] = dado[0]
                dic['marca'] = dado[1]
                dic['loja'] = dado[2]
                dic['data'] = dado[3]
                dic['qtd'] = int(dado[4])
                dic['valor'] = float(dado[5])
                lista.append(dic)

        cur.executemany(sql, lista)

    con.commit()
print("Registros incluidos com sucesso!")
