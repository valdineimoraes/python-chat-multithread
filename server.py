import socket
import sys
import traceback
from threading import Thread


def main():
    start_server()


def start_server():
    host = "localhost"
    port = 5000

    # cria o socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # a flag diz ao kernel para reutilizar o socket local no estado TIME_WAIT, 
    # sem esperar que seu timeout natural expire
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket criado")

    try:
        # tenta escutar o ip e a porta
        soc.bind((host, port))
    except:
        # nao conseguiu escutar a porta e ip e sai do sistema
        print("Erro ao conectar com Bind: " + str(sys.exc_info()))
        sys.exit()

    # usa até 5 pedidos na fila
    soc.listen(5)    
    print("Socket ")

    # Loop para pegar as conexões
    while True:
        # aceita a conexão 
        connection, address = soc.accept()
        ip, port = str(address[0]), str(address[1])
        print("Connectado com o cliente IP: " + ip + ":" + port)

        try:
            # Inicia Nova thread do metodos client_thread e seus argumentos
            Thread(target=client_thread, args=(connection, ip, port)).start()
        except:
            # Não coseguiu iniciar a thread
            print("Thread não foi iniciada.")
            traceback.print_exc()
            
    # Finaliza conexão
    soc.close()

# método cliente com flag is_active e recebe as mensagens com tamanho definido 
def client_thread(connection, ip, port, max_buffer_size = 5120):
    is_active = True

    # escuta a flag se for True
    while is_active:
        
        # recebe dados do metodo receive_input 
        client_input = receive_input(connection, max_buffer_size)
        
        # se mensagem do receive_input for quit ele fecha a conexão com o cliente
        if "--QUIT--" in client_input:
            print("Client is requesting to quit")
            connection.close()
            print("Connection " + ip + ":" + port + " closed")
            is_active = False
        else:
            # se a mensagem nao for quit ele envia a mensagem para ser processada
            print("Processed result: {}".format(client_input))
            connection.sendall("-".encode("utf8"))

# metodo receive_input verifica se a mensagem esta no tamanho definido
def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)

    if client_input_size > max_buffer_size:
        print("The input size is greater than expected {}".format(client_input_size))

    decoded_input = client_input.decode("utf8").rstrip()  # decode and strip end of line
    result = process_input(decoded_input)

    return result

# metodo para processar a mensagem - colocando somente Hello na mensagem do cliente
def process_input(input_str):
    print("Processing the input received from client")

    return "Hello " + str(input_str).upper()

if __name__ == "__main__":
    main()