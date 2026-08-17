from classes import frequency_table as frequency
from classes import table_db as db

table = frequency.FrequencyTable("O Teste", "Números")
table_db = db.TableDB()
print("APRENDENDO BANCO DE DADOS")

print("Adicionando dados...")
table.add_data(1, 2)
table.add_data(3,5)
table.add_data(5, 3)

print("salvando na tabela...")
table_id: int = table_db.add_table(table.table_name, table.data_name, table.get_all_datas())

print("Salvou!!!")

print("É importante guardar o ID da tabela.")

table.data_name = "Alunos"
table.table_name = "Estudandes de Ciências da Computação"

print("Opa, troquei o nome de data e tabela.")
print("MUDANDO OS NOMES NO BANCO DE DADOS")

table_db.modify_table_names(table_id, table.table_name, table.data_name)

print("Nome dos dados modificados.")


print("Testes concluídos. Para acabar, deletar a tabela.")
print("Deletando...")

table_db.delete_table(table_id)

print("Escluído com sucesso!")

'''
con = db.sql.connect("teste.db")

cur = con.cursor()

try:
    cur.execute("""
CREATE TABLE Tutorial(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome VARCHAR(30)
)
""")
except db.sql.OperationalError:
    None


print("Fiz o SELECT")
print(cur.execute("SELECT name FROM sqlite_master").fetchall())


cur.execute("""
INSERT INTO Tutorial(nome) VALUES
    ('Tabela Legal'),
    ('Tabela feia'),
    ('Tabela mediana')
""")



print(cur.fetchone())

cur.execute("SELECT * FROM Tutorial")
print("FetchOne")
print(cur.fetchone())

print("FetchALL")
print(cur.fetchall())

cur.execute("DELETE FROM Tutorial WHERE nome = 'Tabela Legal'")

con.commit()

con.close()
'''