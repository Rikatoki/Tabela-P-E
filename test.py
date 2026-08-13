from classes import frequency_table as frequency

print("teste 1")

teste = frequency.FrequencyTable("Pessoas")

teste.add_data(10)
teste.add_data(10)
teste.add_data(10)
teste.add_data(10)

teste.add_data(14, 3)


teste.add_data(5)
teste.add_data(5)
teste.add_data(5)

teste.add_data(40)

print(teste)

teste.remove_data(14)

print(teste)

