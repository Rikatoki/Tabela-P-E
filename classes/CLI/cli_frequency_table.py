from . import cli
from . import cli_frequency_table_input as fb_input
from .. import frequency_table as fb

class CLIFrequencyTable(cli.CLI):
    def __init__(self, frequency_table: fb.FrequencyTable, db_id: int):
        super().__init__()
        self.frequency_table: fb.FrequencyTable = frequency_table
        self.db_id = db_id
        self.fb_input:fb_input.CLIFrequencyTableInput = fb_input.CLIFrequencyTableInput(self.frequency_table)

        self.add_option(1, cli.Option("Mudar nome da tabela", self.fb_input.change_table_name))
        self.add_option(2, cli.Option("Mudar nome dos dados", self.fb_input.change_data_name))
        self.add_option(3, cli.Option("Adicionar dado", self.fb_input.add_data))
        self.add_option(4, cli.Option("Remover dado", self.fb_input.remove_data))
        self.add_option(5, cli.Option("Salvar a tabela.", self.save))
        self.add_option(0, cli.Option("Voltar", self.back))

    def run(self):
        print(f"""{self.create_line()}
{self.centralize_str(self.frequency_table.table_name)}
{self.frequency_table}
{self.show_options()}
""")
        self.select_option(self.select_option_by_input())

    def save(self):
        from .. import table_db as _db
        db: _db.TableDB = _db.TableDB()
        datas: list[tuple] = []
        for d in self.frequency_table.data:
            datas.append((d.value, d.f,))

        db.modify_table_names(self.db_id, self.frequency_table.table_name, self.frequency_table.data_name)
        db.modify_table_datas(self.db_id, datas)
        print("Mudanças aplicadas com sucesso.")

    def back(self):
        from .cli_main_menu import CLIMainMenu
        self.change_gui(CLIMainMenu())