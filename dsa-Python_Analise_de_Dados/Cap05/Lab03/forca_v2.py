# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
from random import randint

# Board (tabuleiro) - Lista de strings que definem o status do jogador durante o jogo
board = ['''
>>>>>>>>> Tema: Animais <<<<<<<<<

+---+
|   |
	|
	|
	|
	|
=========''', '''

+---+
|   |
O   |
	|
	|
	|
=========''', '''

+---+
|   |
O   |
|   |
	|
	|
=========''', '''

 +---+
 |   |
 O   |
/|   |
	 |
	 |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
	 |
	 |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
	 |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
	 |
=========''']

# Definindo classe geral (pai) que especifica os jogos (projeto: implementar mais jogos além da Forca)
class Jogos():
    """ Método Construtor da classe Jogos"""
    def __init__(self, nome, participantes=1): # Default de participantes para implementação apenas da Forca
        self.nome = nome
        self.participantes = participantes

    """Getters e Setters"""
    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setParticipantes(self):
        participantes = int(input('Número de participantes: '))
        self.participantes = participantes

    def getParticipantes(self):
        return self.participantes

"""Definindo classe filha para especificar o jogo Forca"""
class Forca(Jogos):
    def __init__(self, tema, palavra='', erros=0, tabuleiro=board, nome='Forca', participantes=1):
        """Método construtor para os atributos 'palavra' e 'tabuleiro'"""
        self.tema = tema
        self.palavra = palavra
        self.erros = erros
        self.tabuleiro = tabuleiro
        Jogos.__init__(self, nome, participantes)

    def setTema(self, tema):
        """Método modificador para setar atributo 'tema'"""
        self.tema = tema

    def getTema(self):
        """Método acessor para acessar o atributo 'tema'"""
        return self.tema

    def setPalavra(self, palavra):
        """Método modificador para setar atributo 'palavra'"""
        self.palavra = palavra.upper()

    def getPalavra(self):
        """Método acessor para acessar o atributo 'palavra'"""
        return self.palavra

    def setErros(self, erros):
        """Método para contabilizar a quantidade de erros do jogador"""
        self.erros = erros

    def getErros(self):
        """Método para acessar a quantidade de erros do jogador"""
        return self.erros

    def sorteiaPalavra(self):
        """Método para sortear uma palavra dentro do arquivo 'animais.txt' e a atribui ao parâmetro 'palavra'"""
        with open(self.getTema().lower()+'.txt', 'rt') as file:  # Abre o arquivo "animais.txt" em modo de edição
            arquivo = file.readlines()  # Lê o arquivo e joga pra variável "arquivo"
            palavra = arquivo[randint(0, len(arquivo)-1)]  # Sorteia um item da lista "arquivo" e joga na var "palavra"
        self.setPalavra(palavra)  # Seta a palavra no atributo "palavra" do objeto

    def imprimePalavra(self, acertos):
        """Método para esconder e imprimir a palavra sorteada no prompt"""
        print('Palavra:', end=' ')
        for char in self.getPalavra():  # Para cada caractere na palavra sorteada...
            if char != '\n':  # Se o caracter diferente de "enter"...
                print(char + ' ' if char in acertos else char.replace(char, '_ '), end='')
                # Printa a letra se ela estiver na lista de acertos, caso contrário a substitui por _ (esconde)
        print('\n')

    def imprimeStatus(self, listaAcertos, listaErros):
        """Verificar se erro > 6 (ou 5) e dar continuidade ao jogo, imprimindo o tabuleiro"""
        erros = self.getErros()
        print(self.tabuleiro[erros])  # Imprime o status de acordo com a quantidade de erros (index do tabuleiro)
        self.imprimePalavra(listaAcertos)
        print('Palpites Corretos: ')
        for palpite in listaAcertos:
            print(palpite, end=' - ')  # Imprime os palpites corretos
        print('\n')
        print('Palpites Errados: ')
        for palpite in listaErros:
            print(palpite, end=' - ')  # Imprime os palpites errados
        print('\n')

    def palpite(self, listaAcertos, listaErros, qtdAcertos):
        """Método para gerenciar o input de palpite do usuário"""
        letra = input('Insira uma letra: ').upper()  # Pede uma letra (considera maiúscula e sem espaços)
        while letra.isspace():
            letra = input('Espaço não é válido. Digite uma letra: ').upper()
        while len(letra) > 1:
            letra = input('Frase ou letra duplicada digitada: Digite uma ÚNICA letra: ').upper()
        while letra.isnumeric():
            letra = input('Número não é válido. Digite uma letra: ').upper()
        while letra in listaAcertos or letra in listaErros:  # Verifica se o palpite já foi dado
            letra = input('Letra já informada. Dê outro palpite: ').strip().upper()  # Pede input novamente
        if letra in self.getPalavra():  # Verifica se a letra informada pertence a palavra sorteada
            listaAcertos.append(letra)  # Em caso positivo, adiciona a letra à lista de acertos
            qtdAcertos += self.getPalavra().count(letra.upper())
        else:
            listaErros.append(letra)  # Em caso negativo, adiciona a letra à lista de erros
            self.setErros(self.getErros()+1)  # Adicionalmente, adiciona 1 a quantidade de erros
        return qtdAcertos  # Variável para verificar vitória caso um animal possua letras repetidas


def cabecalho(texto):
    """Método para imprimir cabeçalhos"""
    print('-'*35)
    print('{:^35}'.format(texto).upper())
    print('-'*35)


def main():
    """Função principal"""
    # Criar menu de seleção com diversos Temas (futuro)

    # Cria o objeto jogo diretamente na classe filha "Forca"
    forca = Forca('animais')

    # Chama método sorteiaPalavra() para atribuir ao atributo 'palavra'
    forca.sorteiaPalavra()

    cabecalho('jogo da forca')
    palpitesCorretos = []
    palpitesErrados = []
    qtdAcertos = 0

    while True:
        forca.imprimeStatus(palpitesCorretos, palpitesErrados)
        qtdAcertos = forca.palpite(palpitesCorretos, palpitesErrados, qtdAcertos)
        if forca.getErros() == 6:
            forca.imprimeStatus(palpitesCorretos, palpitesErrados)
            print('Você perdeu! A palavra sorteda era: {}'.format(forca.getPalavra()))
            break
        if qtdAcertos == len(forca.getPalavra())-1:
            forca.imprimeStatus(palpitesCorretos, palpitesErrados)
            print('Você venceu! Parabéns!')
            break
    print('Foi um prazer jogar com você!')

"""----------------- PROGRAMA PRINCIPAL ------------------"""
main()







