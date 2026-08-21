from .. import frequency_table as fb

class CLIFrequencyTableInput():
    def __init__(self, frequency_table: fb.FrequencyTable):
        super().__init__()
        self.frequency_table: fb.FrequencyTable = frequency_table

    def change_table_name(self):
        self.frequency_table.table_name = input("Digite o novo nome: ")

    def change_data_name(self):
        self.frequency_table.data_name = input("Digite o novo nome: ")

    def add_data(self):
        data: float = None
        quantity: int = None
        while data == None:
            try:
                data = float(input("Digite o valor do dado: "))
            except ValueError:
                print("Digite apenas números.")
        while quantity == None or quantity < 0:
            try:
                quantity = int(input(f"Quantas vezes o dado ({data}) ocorre? "))
            except ValueError:
                print("Digite apenas númeoros inteiros igual ou acima 0.")
            if quantity < 0:
                print("Digite apenas númeoros inteiros igual ou acima 0.")
        self.frequency_table.add_data(data, quantity)

    def remove_data(self):
        data: float = None
        quantity: int = None
        while data == None:
            try:
                data = float(input("Digite o valor do dado à remover: "))
            except ValueError:
                print("Digite apenas números.")
        if self.frequency_table.get_data(data) == None:
            return print("Valor não encontrado na tabela.")
        while quantity == None or quantity < 0:
            try:
                quantity = int(input(f"Remover em quantas vezes o dado ({data})? "))
            except ValueError:
                print("Digite apenas númeoros inteiros igual ou acima 0.")
            if quantity < 0:
                print("Digite apenas númeoros inteiros igual ou acima 0.")
        self.frequency_table.remove_data(data, quantity)