from . import gui
from .. import frequency_table as fb

class CriarTabela(gui.GUI):
    def __init__(self):
        super().__init__()
        self.frequency_table: fb.FrequencyTable = fb.FrequencyTable(table_name="Tabela 1")

        self.add_option(1, gui.Option("Mudar nome da tabela", self.change_table_name))
        self.add_option(2, gui.Option("Mudar nome do dado", self.change_data_name))
        self.add_option(3, gui.Option("Adicionar dado", self.add_data))
        self.add_option(4, gui.Option("Remover dado", self.remove_data))
        self.add_option(5, gui.Option("Criar Tabela", self.create_table))
        self.add_option(0, gui.Option("Voltar", self.back))
        
    def run(self):
        datas_str: str = self.frequency_table.get_all_data_string()
        data_name: str = self.frequency_table.data_name

        print(f"""{self.create_line()}
{self.centralize_str(self.frequency_table.table_name)}
Nome dos dados: {data_name if data_name != "" else "Nenhum nome definido."}
Dados: {datas_str if datas_str != "" else "Nenhum dado inserido."}

{self.show_options()}
""")
        self.select_option(self.select_option_by_input())

    def change_table_name(self):
        self.frequency_table.table_name = input("Digite o novo nome: ")

    def change_data_name(self):
        self.frequency_table.data_name = input("Digite o novo nome: ")

    def add_data(self):
        self.frequency_table.add_data_by_input()

    def remove_data(self):
        self.frequency_table.remove_data_by_input()

    def create_table(self):
        from .tabela import Table
        self.change_gui(Table(self.frequency_table))

    def back(self):
        from .menu_principal import MenuPrincipal
        self.change_gui(MenuPrincipal())