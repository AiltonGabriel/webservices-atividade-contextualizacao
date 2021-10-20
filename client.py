import socket
from datetime import datetime
from models import Aluno, Turma

SERVER_NAME = '127.0.0.1'
SERVER_PORT = 12000
HEADER_SIZE = 10
BUFFER_SIZE = 64

# Transforma uma lista de turmas em uma string para o envio.
def encode_turmas(turmas):
    msg = ""
    for turma in turmas:
        msg += "{}#{}".format(turma.nome, turma.ano)
        for aluno in turma.alunos:
            msg += "#{}".format(aluno.nome)
        msg += "\n"
    return msg

# Envia a lista de turmas passada para o servidor.
def send_turmas(turmas):
    # Transformando a lista de turmas em uma string.
    msg = encode_turmas(turmas)

    try:
        # Iniciando a conexão com o servidor.
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_NAME, SERVER_PORT))

        # Inserindo o cabeçalho com o tamanho da mensagem.
        msg = f"{len(msg):<{HEADER_SIZE}}" + msg
        # Enviando a mensagem para o servidor.
        client_socket.sendall(msg.encode('utf-8'))

        client_socket.close()

    except:
        print("\nErro na comunicação com o servidor!\n")

# Exibe um menu com as opções passadas e retorna o número da opção escolhida.
def menu_opcoes(opcoes, msg_erro = "Opção inválida!"):
    while True:
        try:
            menu = ""
            for i, opcao in enumerate(opcoes):
                menu += "{} - {}\n".format(i + 1, opcao)

            opcao = int(input(menu + "\nOpção escolhida: "))
            print()

            if(opcao > 0 and opcao <= len(opcoes)):
                return opcao
                
        except ValueError:
            pass

        print(msg_erro)

# Lê os dados de uma turma.
def ler_turma():
    turma = Turma()
    turma.nome = ler_nome("Digite o nome da turma: ")
    turma.ano = ler_ano("Digite o ano da turma: ")
    turma.alunos = []
    print("\nAlunos da turma: \n")
    while True:
        turma.alunos.append(ler_aluno())
        
        print()

        if(menu_opcoes(["Adicionar outro aluno", "Finalizar cadastro da turma"]) == 2):
            break
    return turma
        
    
def ler_nome(msg = "Digite o nome: ", msg_erro = "Este campo não pode ser vazio!"):
    while True:
        nome = input(msg)
        if(len(nome) > 0):
            break
        else:
            print(msg_erro)
    return nome

def ler_ano(msg = "Digite o ano: ", msg_erro = "Ano inválido!"):
    while True:
        try:
            ano = int(input(msg))
            if(ano <= datetime.now().year):
                break
        except ValueError:
            pass 

        print(msg_erro)
    
    return ano

# Lê os dados de um aluno.
def ler_aluno():
    aluno = Aluno()
    aluno.nome = ler_nome("Digite o nome do aluno: ")
    return aluno

def main():
    try:
        turmas = []
        print()
        while True:
            turmas.append(ler_turma())

            if(menu_opcoes(["Cadastrar outra turma", "Finalizar cadastro"]) == 2):
                break
            
        send_turmas(turmas)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()