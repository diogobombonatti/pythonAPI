import oracledb as db

dsn = 'oracle.fiap.com.br/orcl'
user = 'pf0313'
pwd = 'professor#23'

def faturamento_mensal_produto(mes):
    with db.connect(user=user, 
            password=pwd, dsn=dsn) as con:
        
        with con.cursor() as cur:
            sql = '''select loja, produto, 
                sum(qtd * valor) from faturamento 
                where to_char(data, 'MM') = :mes
                group by loja, produto'''
            
            if mes < 10:
                aux_mes = "0" + str(mes)
            else:
                aux_mes = str(mes)
            par = {"mes": aux_mes}
            
            cur.execute(sql, par)
            dado = cur.fetchall()
    return dado

if __name__ == '__main__':
    info = faturamento_mensal_produto(3)
    print(info)


