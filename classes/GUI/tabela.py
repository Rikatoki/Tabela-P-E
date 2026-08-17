from . import gui
from .. import frequency_table as fb

class Table(gui.GUI):
    def __init__(self, _fb: fb.FrequencyTable):
        super().__init__()
        self.frequency_data: fb.FrequencyTable = _fb

        self.add_option(1, gui.Option("Mudar nome da tabela", self.change_table_name))
        self.add_option(2, gui.Option("Mudar nome dos dados", self.change_data_name))
        self.add_option(3, gui.Option("Adicionar dado", self.add_data))
        self.add_option(4, gui.Option("Remover dado", self.remove_data))
        self.add_option(0, gui.Option("Voltar", self.back))

    def run(self):
        print(f"""{self.create_line()}
{self.centralize_str(self.frequency_data.table_name)}
{self.frequency_data}
{self.show_options()}
""")
        self.select_option(self.select_option_by_input())

    def change_table_name(self):
        self.frequency_data.table_name = input("Digite o novo nome: ")

    def change_data_name(self):
        self.frequency_data.data_name = input("Digite o novo nome: ")

    def add_data(self):
        self.frequency_data.add_data_by_input()

    def remove_data(self):
        self.frequency_data.remove_data_by_input()

    def back(self):
        from .menu_principal import MenuPrincipal
        self.change_gui(MenuPrincipal())