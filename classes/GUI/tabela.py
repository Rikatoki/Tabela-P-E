from . import gui
from .. import frequency_table as fb

class Table(gui.GUI):
    def __init__(self, _fb: fb.FrequencyTable, db_id: int):
        super().__init__()
        self.f_table: fb.FrequencyTable = _fb
        self.db_id = db_id # PAREI AQUI | Chave da tabela no banco de dados.

        self.add_option(1, gui.Option("Mudar nome da tabela", self.change_table_name))
        self.add_option(2, gui.Option("Mudar nome dos dados", self.change_data_name))
        self.add_option(3, gui.Option("Adicionar dado", self.add_data))
        self.add_option(4, gui.Option("Remover dado", self.remove_data))
        self.add_option(5, gui.Option("Salvar a tabela.", self.save))
        self.add_option(0, gui.Option("Voltar", self.back))

    def run(self):
        print(f"""{self.create_line()}
{self.centralize_str(self.f_table.table_name)}
{self.f_table}
{self.show_options()}
""")
        self.select_option(self.select_option_by_input())

    def change_table_name(self):
        self.f_table.table_name = input("Digite o novo nome: ").strip()

    def change_data_name(self):
        self.f_table.data_name = input("Digite o novo nome: ").strip()

    def add_data(self):
        self.f_table.add_data_by_input()

    def remove_data(self):
        self.f_table.remove_data_by_input()

    def save(self):
        from .. import table_db as _db
        db: _db.TableDB = _db.TableDB()
        datas: list[tuple] = []
        for d in self.f_table.data:
            datas.append((d.value, d.f,))

        db.modify_table_names(self.db_id, self.f_table.table_name, self.f_table.data_name)
        db.modify_table_datas(self.db_id, datas)
        print("Mudanças aplicadas com sucesso.")

    def back(self):
        from .menu_principal import MenuPrincipal
        self.change_gui(MenuPrincipal())