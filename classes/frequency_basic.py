# Classe que conterá o valor do dado e suas frequências.
class DataFrequency:
    def __init__(self, data: float, absolute_frequency: int = 1):
        self.data: float = data
        # Frequência Absoluta
        self.f: int = absolute_frequency
        # Frequência Acumulativa
        self.fa: int = self.f
          # Frequência Relativa
        self.fr: float = self.f / self.fa

# Classe que conterá uma lista de dados e o organizará de ordem crescente e cada dado conterá sua frequência absoluta, relativa e acomulativa.
class FrequencyBasic:
    # Faz a configuração inicial da classe. Determina o nome do dado que está sendo trabalhado.
    def __init__(self, table_name:str = "", _data_type: str = ""):
        self.table_name: str = table_name.strip()
        self.data_type = _data_type.strip()
        self.data: list[DataFrequency] = []

    # Retorna uma representação dos dados em formato de tabela.
    def __str__(self) -> str:
        text: str = f"{self.data_type.capitalize()}\n  Data  | Frequência Absoluta | Frequência Acumulativa | Frequência Relativa \n"
        for i in self.data:
            text += f"{i.data:^8}|{i.f:^21}|{i.fa:^24}|{i.fr:^21}\n"
        return text
    
    # Ordena a lista de dados do menor até o maior.
    def _sort_data_list(self):
        if len(self.data) <= 1:
            return None
        self.data.sort(key= lambda i: i.data)

    # Retorna o DataFrequency do dado, caso ele existe na lista.
    def _get_data(self, data: float) -> DataFrequency:
        for i in self.data:
            if i.data == data:
                return i

    # Adiciona um dado na lista.
    def add_data(self, data: float, quantity: int = 1) -> None:
        if quantity <= 0:
            return
        _data: DataFrequency = self._get_data(data)
        if _data:
            _data.f += quantity
        else:
            self.data.append(DataFrequency(data, quantity))
        self.update()

    def add_data_by_input(self):
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
        self.add_data(data, quantity)

    # Remove um dado da lista.
    def remove_data(self, data: float, quantity: int = 1) -> None:
        _data = self._get_data(data)
        if quantity <= 0 and _data == None:
            return
        _data.f -= quantity
        if _data.f <= 0:
            self.data.remove(_data)
        self.update()

    def remove_data_by_input(self):
        data: float = None
        quantity: int = None
        while data == None:
            try:
                data = float(input("Digite o valor do dado à remover: "))
            except ValueError:
                print("Digite apenas números.")
        if self._get_data(data) == None:
            return print("Valor não encontrado na tabela.")
        while quantity == None or quantity < 0:
            try:
                quantity = int(input(f"Remover em quantas vezes o dado ({data})? "))
            except ValueError:
                print("Digite apenas númeoros inteiros igual ou acima 0.")
            if quantity < 0:
                print("Digite apenas númeoros inteiros igual ou acima 0.")
        self.remove_data(data, quantity)

    def get_all_data_string(self) -> str:
        all_data: str = ""
        for i in range(len(self.data)):
            all_data += str(self.data[i].data)
            if i != len(self.data) - 1:
                all_data += ", "
        return all_data

    # Atualiza os dados, requer ser chamado após cada mudança em self.data.
    def update(self):
        total_data: int = len(self.data)
        if total_data == 0:
            return
        self._sort_data_list()
        total_values: int = 0 
        for i in self.data:
            total_values += i.f 
        self.data[0].fa = self.data[0].f
        self.data[0].fr = self.data[0].f / total_values
        if total_data == 1:
            return
        for i in range(1, total_data):
            data: DataFrequency = self.data[i]
            data.fa = data.f + self.data[i-1].fa
            data.fr = data.f / total_values
