# Classe que conterá o valor do dado e suas frequências.
class DataFrequency:
    def __init__(self, value: float, absolute_frequency: int = 1):
        self.value: float = value
        # Frequência Absoluta
        self.f: int = absolute_frequency
        # Frequência Acumulativa
        self.fa: int = self.f
          # Frequência Relativa
        self.fr: float = self.f / self.fa

# Classe que conterá uma lista de dados e o organizará de ordem crescente e cada dado conterá sua frequência absoluta, relativa e acomulativa.
class FrequencyTable:
    # Faz a configuração inicial da classe. Determina o nome do dado que está sendo trabalhado.
    def __init__(self, table_name:str = "", _data_name: str = ""):
        self.table_name: str = table_name.strip()
        self.data_name = _data_name.strip()
        self.data: list[DataFrequency] = []

    # Retorna uma representação dos dados em formato de tabela.
    def __str__(self) -> str:
        text: str = f"{self.data_name.capitalize()}\n  Data  | Frequência Absoluta | Frequência Acumulativa | Frequência Relativa \n"
        for i in self.data:
            text += f"{i.value:^8}|{i.f:^21}|{i.fa:^24}|{i.fr:^21}\n"
        return text
    
    # Ordena a lista de dados do menor até o maior.
    def _sort_data_list(self):
        if len(self.data) <= 1:
            return None
        self.data.sort(key= lambda i: i.value)

    # Retorna o DataFrequency do dado, caso ele existe na lista.
    def get_data(self, data: float) -> DataFrequency:
        for i in self.data:
            if i.value == data:
                return i

    # Adiciona um dado na lista.
    def add_data(self, data: float, quantity: int = 1) -> None:
        if quantity <= 0:
            return
        _data: DataFrequency = self.get_data(data)
        if _data:
            _data.f += quantity
        else:
            self.data.append(DataFrequency(data, quantity))
        self.update()

    # Remove um dado da lista.
    def remove_data(self, data: float, quantity: int = 1) -> None:
        _data = self.get_data(data)
        if quantity <= 0 and _data == None:
            return
        _data.f -= quantity
        if _data.f <= 0:
            self.data.remove(_data)
        self.update()

    # Retorna todos os dados numa lista de tuplas onde tuple(1,2) 1 - Valor, 2 - Frequência do valor.
    def get_all_datas(self) -> list[tuple]:
        datas: list[tuple] = []
        for data in self.data:
            datas.append((data.value, data.f))
        return datas

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
