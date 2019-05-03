import socket

def chat_client():

    # Criar o socket
    client_sock = socket.socket()

    # Conectar ao servidor com ip e porta
    client_sock.connect(('localhost', 9000))

    message = input(" -> ")

    # Envia e recebe mensagem enquanto a mensagem for diferente de see ya 
    while message.lower().strip() != 'see ya':

        # Envia a mensagem ao servidor
        client_sock.send(message.encode())

        # Recebe mensagem do servidor e nao aceita dados maior que 1024 bytes
        data = client_sock.recv(1024).decode()

        # Imprime mensagem do Servidor
        print('Mensagem do Servidor: '+data)

        # Prepara para enviar nova mensagem
        message = input(" -> ")

    # Fecha conexao
    client_sock.close()

if __name__ == '__main__':
    chat_client()
