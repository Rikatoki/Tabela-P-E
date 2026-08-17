from . import gui
class MenuPrincipal(gui.GUI):
    def __init__(self):
        super().__init__()
        self.add_option(1, gui.Option("Criar Nova Tabela", self.new_table))
        self.add_option(2, gui.Option("Abrir tabela existente", self.load_table))
        self.add_option(0, gui.Option("Fechar o Programa", quit))

    def run(self):
        print(f"{self.create_line()}\n{self.centralize_str("Tabela de frequência de dados")}\n{self.show_options()}")
        self.select_option(self.select_option_by_input())
        print(self.create_line())
        
    def new_table(self):
        from .criar_tabela import CriarTabela
        self.change_gui(CriarTabela())

    def load_table(self):
        from .. import table_db as _db
        db: _db.TableDB = _db.TableDB()

        tables: _db.AllTableDataDB = db.get_all_tables()

        if len(tables.table_rows) == 0:
            return print("Não há tabelas criadas.")
        for r in tables.table_rows:
            print(f"ID: {r.id:^5} | Nome da tabela: {r.name:^50} | Nome dos dados: {r.data_name:^30}")
        print("")
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
        
        from .tabela import Table
        from .. import frequency_table as ft

        td: _db.TableDataDB = db.get_table(option)
        table: ft.FrequencyTable = ft.FrequencyTable(td.table.name, td.table.data_name)
        for d in td.table_datas:
            table.add_data(d.data, d.frequency)
        self.change_gui(Table(table, td.table.id))
        