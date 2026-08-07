from . import gui
class MenuPrincipal(gui.GUI):
    def __init__(self):
        super().__init__()
        self.add_option(1, gui.Option("Criar Nova Tabela", self.new_table))
        self.add_option(0, gui.Option("Fechar o Programa", quit))

    def run(self):
        print(f"{self.create_line()}\n{self.centralize_str("Tabela de frequência de dados")}\n{self.show_options()}")
        self.select_option(self.select_option_by_input())
        print(self.create_line())
        
    def new_table(self):
        from .criar_tabela import CriarTabela
        self.change_gui(CriarTabela())
