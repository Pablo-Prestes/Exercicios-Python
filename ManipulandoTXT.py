#Funções
def listar_arquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao abrir o arquivo')
    else:
        print(a.read())#Mostra tudo o que tem no arquivo
    finally:
        a.close()#fecha o arquivo independente de dar certo ou não


def cadastrar_jogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write(f'{nomeJogo}, {nomeVideogame} \n')
    finally:
        a.close()


def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x


def existe_arquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cria_arquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print(f'Arquivo {nomeArquivo} foi criado com sucesso ! \n')


#Programa Principal
arquivo = 'games.txt'
if existe_arquivo(arquivo):
    print('Arquivo localizado no computador ! \n')
else:
    print('Arquivo inexistente !')
    cria_arquivo(arquivo)

while True:
    print('Menu')
    print('1 - Cadastras novo item')
    print('2 -  Listar cadastro')
    print('3 - Sair \n')

    op = valida_int('Escola a opção desejada: ',1, 3)
    if op == 1:
        print('Opção de cadastrar novo item selecionada! ')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do vídeogame: ')
        cadastrar_jogo(arquivo,nomeJogo, nomeVideogame)

    elif op == 2:
        print('Opção de listar selecionada! \n')
        listar_arquivo(arquivo)
    elif op == 3:
        print('Encerrando programa...')
        break