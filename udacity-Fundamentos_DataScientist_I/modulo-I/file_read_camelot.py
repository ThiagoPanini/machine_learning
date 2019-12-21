with open('camelot.txt') as song:
	print('Método .read()')
	print(song.read())
	print()
with open('camelot.txt') as song:
	print('Método .readlines()')
	print(song.readlines())
	print()
with open('camelot.txt') as song:
	print('Método .readline()')
	print(song.readline())

camelot_lines = []
with open('camelot.txt') as f:
	print('Lendo com laço for e adicionando elementos à lista (quebra por "c.return")')
	for line in f:
		camelot_lines.append(line.strip())
print(camelot_lines)
