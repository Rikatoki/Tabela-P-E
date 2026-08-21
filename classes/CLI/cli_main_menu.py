from . import cli
from .. import table_db as _db

class CLIMainMenu(cli.CLI):
    def __init__(self):
        super().__init__()
        self.add_option(1, cli.Option("Criar Nova Tabela", self.new_table))
        self.add_option(2, cli.Option("Abrir tabela existente", self.load_table))
        self.add_option(3, cli.Option("Excluir tabela existente", self.delete_table))
        self.add_option(0, cli.Option("Fechar o Programa", quit))

    def run(self):
        print(f"{self.create_line()}\n{self.centralize_str("Tabela de frequência de dados")}\n{self.show_options()}")
        self.select_option(self.select_option_by_input())
        print(self.create_line())
        
    def new_table(self):
        from .cli_create_table import CLICreateTable
        self.change_gui(CLICreateTable())

    def show_tables(self, db: _db.TableDB) -> bool:
        tables: _db.AllTableDataDB = db.get_all_tables()
        if len(tables.table_rows) == 0:
            print("Não há tabelas criadas.")
            return False
        for r in tables.table_rows:
            print(f"ID: {r.id:<5} | Nome da tabela: {r.name:<50} | Nome dos dados: {r.data_name:<30}")
        print("")
        return True

    def get_table_by_input(self, db: _db.TableDB) -> int | None:
        option: int = None
        while option == None:
            try:
                option = int(input("Digite 0 para voltar.\nSelecione a tabela pelo ID:"))
                if option != 0 and not db.has_table_id(option):
                    option = None
                    print("Digite um ID válido.")
            except ValueError:
                option = None
                print("Digite apenas números inteiros.")
        if option == 0:
            return None
        return option

    def load_table(self):
        db: _db.TableDB = _db.TableDB()
        if not self.show_tables(db):
            return None
        table_id: int = self.get_table_by_input(db)
        if table_id is None:
            return None
    
        from .cli_tabela import CLIFrequencyTable
        from .. import frequency_table as ft
        
        td: _db.TableDataDB = db.get_table(table_id)
        table: ft.FrequencyTable = ft.FrequencyTable(td.table.name, td.table.data_name)
        for d in td.table_datas:
            table.add_data(d.data, d.frequency)
        self.change_gui(CLIFrequencyTable(table, td.table.id))

    def delete_table(self):
        db: _db.TableDB = _db.TableDB()
        if not self.show_tables(db):
            return None
        table_id: int = self.get_table_by_input(db)
        if table_id is None:
            return None
        db.delete_table(table_id)
        print("Tabela excluída com sucesso.")