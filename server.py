import socket
import threading
import time
from models import Aluno, Turma

SERVER_PORT = 12000
HEADER_SIZE = 10
BUFFER_SIZE = 64

# Transforma a string com os dados das turmas em uma lista de objetos com os dados desta string.
def decode_turmas(string):
    turmas = []
    for t in string.split("\n"):
        dados = t.split("#")
        if(len(dados) >= 3):
            alunos = []
            for aluno in dados[2:]:
                alunos.append(Aluno(aluno))

            turmas.append(Turma(nome=dados[0], ano=dados[1], alunos=alunos))
    
    return turmas

def connection(connection_socket, addr):
    print("Conexão vinda de {}".format(addr))

    # Obtendo o tamanho da mensagem que será recebida.
    data = connection_socket.recv(BUFFER_SIZE)
    msg_len = int(data[:HEADER_SIZE])

    # Recebendo a mensagem.
    msg = data[HEADER_SIZE:].decode('utf-8')
    while len(msg) < msg_len:
        data = connection_socket.recv(BUFFER_SIZE)
        msg += data.decode('utf-8')
    
    connection_socket.close()

    turmas = decode_turmas(msg)
    show_turmas_data(turmas)
    
# Exibe os resultados dos cálculos realizados sobre a lista de turmas passada.
def show_turmas_data(turmas):
    print("\nQuantidade de turmas: {}\n"
        "Nome da turma com mais alunos: {}\n"
        "Ano da turma mais antiga: {}\n"
        "Quantidade média de alunos por turma: {}".format(len(turmas), turma_max_alunos(turmas).nome, oldest_turma(turmas).nome, mean_alunos(turmas)))

# Retorna a turma com mais alunos.
def turma_max_alunos(turmas):
    max = turmas[0]
    for turma in turmas:
        if(len(turma.alunos) > len(max.alunos)):
            max = turma
    return max

# Retorna a turma mais antiga.
def oldest_turma(turmas):
    oldest = turmas[0]
    for turma in turmas:
        if(turma.ano < oldest.ano):
            oldest = turma
    return oldest

# Retorna a média de alunos por turma.
def mean_alunos(turmas):
    sum = 0
    for turma in turmas:
        sum += len(turma.alunos)
    return sum / len(turmas)

def server():

    # Configurando o socket servidor.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', SERVER_PORT))
    server_socket.listen(0)

    while True:
        # Aguandando uma conexão.
        connection_socket, addr =  server_socket.accept()
        # Iniciando uma thread para processar a conexão.
        th = threading.Thread(target=connection, args=(connection_socket, addr))
        th.start()

def main():
    try:
        # Iniciando uma thread deamon para executar o servidor, para que assim seja possível encerrar o programa como CTRL+C.
        th = threading.Thread(target=server)
        th.daemon = True
        th.start()

        # Loop para que a thread principal não encerre, encerrando assim posteriormente a thread deamon do servidor.
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()