from .. import frequency_table as fb

class CLIFrequencyTableInput():
    TABLE_NAME_TOTAL_CHAR: int = 50
    DATA_NAME_TOTAL_CHAR: int = 30
    
    def __init__(self, frequency_table: fb.FrequencyTable):
        super().__init__()
        self.frequency_table: fb.FrequencyTable = frequency_table

    def is_valid_table_name(self, new_name: str) -> bool:
        return new_name != None and new_name != "" and len(new_name) <= self.TABLE_NAME_TOTAL_CHAR

    def is_valid_data_name(self, new_name:str) -> bool:
        return new_name != None and new_name != "" and len(new_name) <= self.DATA_NAME_TOTAL_CHAR

    def change_table_name(self):
        new_name: str = ""
        while not self.is_valid_table_name(new_name):
            new_name = input("Digite o novo nome: ").strip().title()
            if not self.is_valid_table_name(new_name):
                print(f"Não deixe o texto vazio ou com mais de {self.TABLE_NAME_TOTAL_CHAR} caracteres.")
        self.frequency_table.table_name = new_name

    def change_data_name(self):
        new_name: str = ""
        while not self.is_valid_data_name(new_name):
            new_name = input("Digite o novo nome: ").strip().capitalize()
            if not self.is_valid_data_name(new_name):
                print(f"Não deixe o texto vazio ou com mais de {self.TABLE_NAME_TOTAL_CHAR} caracteres.")
        self.frequency_table.data_name = new_name

    def add_data(self):
        data: float = None
        frequency: int = None
        while data == None:
            try:
                data = float(input("Digite o valor do dado: "))
            except ValueError:
                print("Digite apenas números.")
        while frequency == None or frequency < 0:
            try:
                frequency = int(input(f"Quantas vezes o valor ({data}) ocorre? "))
            except ValueError:
                print("Digite apenas númeoros inteiros igual ou acima 0.")
            if frequency < 0:
                print("Digite apenas númeoros inteiros igual ou acima 0.")
        self.frequency_table.add_data(data, frequency)

    def remove_data(self):
        data: float = None
        frequency: int = None
        while data == None:
            try:
                data = float(input("Digite o valor do dado à remover: "))
            except ValueError:
                print("Digite apenas números.")
        if self.frequency_table.get_data(data) == None:
            return print("Valor não encontrado na tabela.")
        while frequency == None or frequency < 0:
            try:
                frequency = int(input(f"Remover em quantas vezes o valor ({data})? "))
            except ValueError:
                print("Digite apenas númeoros inteiros igual ou acima 0.")
            if frequency < 0:
                print("Digite apenas númeoros inteiros igual ou acima 0.")
        self.frequency_table.remove_data(data, frequency)