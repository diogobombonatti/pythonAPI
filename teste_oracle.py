import oracledb as db

with db.connect(user='pf0313', 
        password='professor#23',
        dsn='oracle.fiap.com.br/orcl') as con:
    
    with con.cursor() as cur:
        sql = '''select count(*) from faturamento
                   where marca = :marca'''
        
        dic = {"marca": "Samsung"}
        cur.execute(sql, dic)
        dado = cur.fetchone()
        print("Quantidade: ", dado)