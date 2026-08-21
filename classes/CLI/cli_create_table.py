from . import cli
from . import cli_frequency_table_input as cli_fb_input
from .. import frequency_table as fb

class CLICreateTable(cli.CLI):
    def __init__(self):
        super().__init__()
        
        self.frequency_table: fb.FrequencyTable = fb.FrequencyTable(table_name="Tabela 1")
        self.fb_input: cli_fb_input.CLIFrequencyTableInput = cli_fb_input.CLIFrequencyTableInput(self.frequency_table)

        self.add_option(1, cli.Option("Mudar nome da tabela", self.fb_input.change_table_name))
        self.add_option(2, cli.Option("Mudar nome do dado", self.fb_input.change_data_name))
        self.add_option(3, cli.Option("Adicionar dado", self.fb_input.add_data))
        self.add_option(4, cli.Option("Remover dado", self.fb_input.remove_data))
        self.add_option(5, cli.Option("Criar Tabela", self.create_table))
        self.add_option(0, cli.Option("Voltar", self.back))
        
    def run(self):
        datas_str: str = self.all_data_values()
        data_name: str = self.frequency_table.data_name

        print(f"""{self.create_line()}
{self.centralize_str(self.frequency_table.table_name)}
Nome dos dados: {data_name if data_name != "" else "Nenhum nome definido."}
Dados: {datas_str if datas_str != "" else "Nenhum dado inserido."}

{self.show_options()}
""")
        self.select_option(self.select_option_by_input())


    def all_data_values(self) -> str:
        all_data: str = ""
        for i in range(len(self.frequency_table.data)):
            all_data += str(self.frequency_table.data[i].value)
            if i != len(self.frequency_table.data) - 1:
                all_data += ", "
        return all_data


    def create_table(self):
        from .cli_tabela import CLIFrequencyTable
        from .. import table_db as _db

        db: _db.TableDB = _db.TableDB()

        datas: list[tuple] = []
        for d in self.frequency_table.data:
            datas.append((d.value, d.f,))
        
        db_id: int = db.add_table(self.frequency_table.table_name, self.frequency_table.data_name, datas)

        self.change_gui(CLIFrequencyTable(self.frequency_table, db_id))


    def back(self):
        from .cli_main_menu import CLIMainMenu
        self.change_gui(CLIMainMenu())