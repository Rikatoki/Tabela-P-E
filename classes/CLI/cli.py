class Option:
    name: str = ""
    func: function = None

    def __init__(self, name: str, func:function):
        self.name = name
        self.func = func

    def get_name(self):
        return self.name

    def run(self):
        if self.func:
            return self.func()

# Classe modelo para a criação da interface do programa.
class CLI:
    manager: CLIManager
    
    def __init__(self):
        self.options: dict[int, Option] = {}

    # Essa função deverá ser chamada para iniciar a parte do programa.
    def run(self) -> None:
        print("Nenhuma interface criada.")

    def change_gui(self, new_gui: CLI) -> None:
        self.manager.change_gui(new_gui)

    def show_options(self) -> str:
        if len(self.options) == 0:
            return "Nenhuma opção disponível."
        text: str = ""
        for k, v in self.options.items():
            v: Option
            text += f"{k} - {v.get_name()}\n"
        return text.strip()

    def select_option_by_input(self) -> int | None:
        option: int = None
        try:
            option = int(input("Selecione uma opção: "))
        except ValueError:
            print("Digite apenas números inteiros.")
        return option

    def select_option(self, _option: int):
        option: Option = self.options.get(_option)
        if option == None:
            return print("Opção inválida.") 
        return option.run()

    def add_option(self, pos: int, option: Option):
        self.options[pos] = option

    def remove_option(self, option: int):
        self.options.pop(option)
    
    def create_line(self, multiplier: int = 25) -> str:
        return "===" * multiplier

    def centralize_str(self, string: str, size:int = 75) -> str:
        return f"{string:^{size}}"

class CLIManager:
    current_gui: CLI = None

    def update(self):
        self.current_gui.run()

    def change_gui(self, new_gui: CLI):
        if self.current_gui != None:
            del self.current_gui
        self.current_gui = new_gui
