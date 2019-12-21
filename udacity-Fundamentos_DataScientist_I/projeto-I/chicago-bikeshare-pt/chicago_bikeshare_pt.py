# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt
import statistics

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Ler os dados com csv.DictReader
print('Lendo o documento via DictReader...')
with open('chicago.csv', 'r') as file_read:
    named_list = [{k: v for k, v in row.items()} for row in csv.DictReader(file_read, skipinitialspace=True)]
print('Ok!')

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

# 1) Via data_list
"""for i in range(1, 21):
    print(data_list[i])"""


# 2) Via named_list (DictReader)
for i in range(20):
    print(f'{"AMOSTRA "}{i+1}: {named_list[i]}')
    print()

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

# 1) Via data_list
for i in range(20):
    print(f'{"Amostra "}{(i+1):2}: {data_list[i][6] if data_list[i][6] != "" else "Não informado"}')
print()

# 2) Via named_list (DictReader)
"""for i in range(20):
    print(f'{"Amostra"}{i+1}: {named_list[i]["Gender"] if named_list[i]["Gender"] != "" else "Não informado"}')"""

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem

def column_to_list(data, index):
    """
    Cria uma lista com todos os dados referentes a uma determinada coluna
    
    Argumentos:
    data -- Dataset no qual deseja-se extrair os campos (list)
    index -- Referência numérica do índice da coluna dentro do referido Dataset (int)
    
    Retorno:
    column_list -- Lista com todos os dados referentes ao campo em questão (list)
    """
    column_list = []
    for registro in data:
        try:
            column_list.append(registro[index])
        except IndexError:
            message = 'Para o data_set "data", selecione um "index" < {}.'.format(len(data[0]))
            return message
    return column_list

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0

gender_column_data = column_to_list(data_list, 6)

for gender in gender_column_data:
    if gender == 'Male':
        male += 1
    elif gender == 'Female':
        female += 1


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
    Cria uma lista com a quantidade de pessoas do gênero masculino e do gênero feminino
    
    Argumentos:
    data_list -- Dataset no qual deseja-se extrair os dados de gênero (list)
    
    Retorno:
    [male, female] -- Lista cujos elementos são números inteiros que representam a quantidade de pessoas do gênero masc (index[0]) e feminino (index[1]) (list)
    """
    male = 0
    female = 0    
    gender_column_data = column_to_list(data_list, 6)    
    for gender in gender_column_data:
        if gender == 'Male':
            male += 1
        elif gender == 'Female':
            female += 1
    return [male, female]

print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """
    Função que analisa o gênero mais popular presente em um determinado dataset
    
    Argumentos:
    data_list -- Dataset no qual deseja-se extrair os dados de gênero (list)
    
    Retorno:
    String -- Reposta em formato de string contendo o gênero mais popular presente no data_set.
    """
    male = 0
    female = 0   
    gender_column_data = column_to_list(data_list, 6)    
    
    gender = count_gender(data_list)
    
    if gender[0] > gender[1]:
        answer = 'Masculino'
    elif gender[1] > gender[0]:
        answer = 'Feminino'
    else:
        answer = 'Igual'
    
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

def count_user_types(data_list):
    """
    Cria uma lista com a quantidade de pessoas cujo tipo pode ser caracterizado entre 'Costumer' e 'Subscriber'
    
    Argumentos:
    data_list -- Dataset no qual deseja-se extrair os dados de gênero (list)
    
    Retorno:
    [male, female] -- Lista cujos elementos são números inteiros que contabilizam o tipo de usuário (list)
    """
    costumer = subscriber = 0
    
    user_types_data = column_to_list(data_list, 5)
    
    for user_type in user_types_data:
        if user_type == 'Customer':
            costumer += 1
        elif user_type == 'Subscriber':
            subscriber += 1
    return [costumer, subscriber]

user_types_list = column_to_list(data_list, 5)
#print(user_types_list[:40])
types = ['Customer', 'Subscriber']
quantity = count_user_types(data_list)
#print(f'Customers: {quantity[0]} \nSubscribers: {quantity[1]}')
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Categorias de Usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Categoria')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "A condição acima é falsa pois, na base de dados fornecida, há também entradas cujo gênero não foi especificado, ou seja, além de gêneros masculinos\
 e femininos, há valores vazios que devem ser contabilizados, dentro da lista de gêneros, por 'lista_generos.count('')'"
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
soma_trip = 0.

trip_flutu = []

for i in range(len(trip_duration_list)):
	trip_flutu.append(float(trip_duration_list[i]))
	if i == 0:
		min_trip = max_trip = trip_flutu[i]
	else:
		if trip_flutu[i] > max_trip:
			max_trip = trip_flutu[i]
		if trip_flutu[i] < min_trip:
			min_trip = trip_flutu[i]
	soma_trip += trip_flutu[i]

mean_trip = soma_trip / len(trip_duration_list)
sorteada = sorted(trip_flutu)
median_trip = sorteada[round((len(sorteada)+1)/2)]

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
user_types = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:

"""
Função de exemplo com anotações.
Argumentos:
    param1: O primeiro parâmetro.
    param2: O segundo parâmetro.
Retorna:
    Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    """
    Retorna duas listas, sendo a primeira com elementos únicos de determinada coluna de um data_set e, a segunda, com a contagem de cada um destes atributos'
    
    Argumentos:
    column_list -- lista contendo todas as aparições de determinado atributo em um dataset (list)
    
    Retorno:
    item_types -- lista com elementos únicos filtrados da lista column_list (list)
    count_items -- lista cujos índices apresentam a contagem de aparições de cada elemento único dentro da lista column_list (list)
    """
    item_types = []
    count_items = []
    for item in column_list:
      if item not in item_types:
        item_types.append(item)
    for item in item_types:
        count_items.append(column_list.count(item))
    return item_types, count_items

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------