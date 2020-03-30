""""		descricao do segundo parametro da funcao "open"
r = somente leitura
w = escrita, caso ja exista ele será apagado e sera criado um novo
a = leitura e escrita adicionando um novo conteudo no fim do arquivo
r+ = leitura e escrita
w+ = escrita, o modo w+ como w tambem apagada o conteudo do arquivo anterior
a+ = leitura e escrita, abre o arquivo para atualizacao 

		descricao dos principais metodos da funcao "open"

readlines() = retorna uma lista de linhas (return list)
read() = retorna uma string com o objeto todo (return string)
write() = escreve um conteudo no arquivo (return void)
close() = fecha o arquivo (return void) """

r_file= open("D:\Projetos\Desenvolvimento\Java\MASSA-TESTE\FILE-PROCESSOR\Input\ARQUIVO_PROCESSOR_08032020235558.txt") 

lines = r_file.readlines()

for line in lines:
	print(line)

r_file.close()	

w_file = open("D:\Projetos\Desenvolvimento\Java\MASSA-TESTE\FILE-PROCESSOR\Input\PYTHON_FILE.txt", "a")

w_file.write("Arquivo criado pelo python \n")

w_file.close()
