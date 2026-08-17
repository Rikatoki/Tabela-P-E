from classes import frequency_table as frequency
from classes import table_db as db

table = frequency.FrequencyTable("O Teste", "Números")
table_db = db.TableDB()

# Função que mostra no terminal os dados relacionado ao ID da tabela.
def show_table(table_id: int):
    table_data: db.TableDataDB = table_db.get_table(table_id)

    print(f"ID: {table_data.table.id} | Nome da tabela: {table_data.table.name} | Nome dos dados: {table_data.table.data_name}")

    print("Dados atuais")

    for d in table_data.table_datas:
        print(f"Dado: {d.data} | Frequência: {d.frequency}")

# INÍCIO
print("APRENDENDO BANCO DE DADOS")

# MOSTRANDO TODOS OS DADOS DO BANCO
print("Dados existentes")

table_datas: db.AllTableDataDB = table_db.get_all_tables()
for t in table_datas.table_rows:
    print(f" {t.id:^5} | {t.name:^30} | {t.data_name:^30} |")

# ADICIONANDO DADOS NA NOVA TABELA
print("Adicionando dados na nova tabela...")
table.add_data(1, 2)
table.add_data(3,5)
table.add_data(5, 3)

# SALVANDO A TABELA NO BANCO
print("salvando no banco...")
table_id: int = table_db.add_table(table.table_name, table.data_name, table.get_all_datas())

print("Salvou!!!")

print("É importante guardar o ID da tabela.")

# MOSTRA OS DADOS DO BANCO DA TABELA ATUAL NO TERMINAL
print("Tabela atual no banco de dados")
show_table(table_id)

# MUDANDO ALGUNS DADOS NA TABELA E NO BANCO
table.data_name = "Alunos"
table.table_name = "Estudandes de Ciências da Computação"

print("Opa, troquei o nome de data e tabela.")
print("MUDANDO OS NOMES NO BANCO DE DADOS")

table_db.modify_table_names(table_id, table.table_name, table.data_name)

print("Nome dos dados modificados.")

# DADOS DO BANCO APÓS AS MUDANÇAS
print("Dados no banco após a mudança:")
show_table(table_id)

# CONCLUSÃO DO TESTE
print(f"Testes concluídos. Para acabar, deletar a tabela. {table_id}")
print("Deletando...")

table_db.delete_table(table_id)

print("Excluído com sucesso!")

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