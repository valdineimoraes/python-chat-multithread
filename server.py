import socket
# from socket import *

def chat_server():
    
    # Criar o socket
    server_socket = socket.socket()

    # Escutar a porta 9000 e localhost
    server_socket.bind(('localhost', 9000))

    # Quantidade de clientes que o servidor escuta
    server_socket.listen(1)

    # Aceitar a nova conexao
    conn, address = server_socket.accept()

    print("Conectado a: "+str(address))

    while True:
        # recebe fluxo de dados e nao aceita pacote maior que 1024 bytes
        data = conn.recv(1024).decode()
        
        # Se nao tiver nenhum dados ele para
        if not data:
            break

        # Se tiver dados do usuario ele imprime    
        print(" Mensagem do Usuario: "+str(data))

        # Enviar Dados ao cliente
        message = input(' -> ')
        conn.send(message.encode())

    # Fecha a conexao
    conn.close()

if __name__ == '__main__':
    chat_server()