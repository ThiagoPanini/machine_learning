

names = input('Digite os nomes: ')  # capture e processe o input para uma lista de nomes
names = names.split(", ")
assignments = input('Digite as quantidade de tarefas para cada aluno: ') # capture e processe o input para uma lista do número de tarefas
assignments = assignments.split(", ")
grades = input('Digite as notas de cada um: ') # capture e processe o input para uma lista de notas
grades = grades.split(", ")

# string de mensagem a ser usada para cada aluno
# DICA: use .format() com esta string no seu loop for
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# escreva um loop for que realize uma iteração em cada conjunto de nomes, tarefas e notas para imprimir a mensagem de cada aluno
for i in range(len(names)):
	print(message.format(names[i], assignments[i], grades[i], (int(grades[i]) + 2 * (int(assignments[i])))))