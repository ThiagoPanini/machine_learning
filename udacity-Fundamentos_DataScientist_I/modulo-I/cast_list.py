def create_cast_list(filename):
	cast_list = []
	full_data = []
	while True:
		try:
			with open(filename) as f:
				data = f.read()
				rows = data.split('\n')
				for row in rows:
					split_row = row.split(',')
					full_data.append(split_row)
				for cast_name in full_data:
					cast_list.append(cast_name[0])
				return cast_list
				break
		except FileNotFoundError:
			print("Arquivo não encontrado ou inexistente.")
			r = input('Deseja especificar novamente o nome do arquivo? [S/N] ').strip().upper()
			while r not in 'SN':
				r = input('Entrada inválida. Digite [S/N]: ')
			if r in 'N':
				print('Encerrando programa.')
				break
			else:
				filename = input('Digite o nome (+ extensão) do arquivo: ')
				continue
		"""else:
			pass
		finally:
			print('Fim do programa.')
			print('Printando "data"')
			print(data)
			print('\n')
			print('Printando "rows"')
			print(rows)
			print('\n')
			print('Printando "rows[0]"')
			print(rows[0])
			print('\n')
			print('Printando "split_row"')
			print(split_row)
			print('\n')
			print('Printando "full_data"')
			print(full_data)
			print('\n')
			print('Printando "cast_list"')
			print(cast_list)
			print('\n')
			print('Printando "cast_list"[0]')
			print(cast_list[0])"""
	

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
	print(actor)		