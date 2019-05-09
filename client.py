import socket
import sys

def main():
    # Cria socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "localhost"
    port = 5000

    try:
        # Tenta conectar com ip e porta
        soc.connect((host, port))
    except:
        # Erro de conexão
        print("Connection error")
        sys.exit()

    print("Enter 'quit' to exit")
    message = input(" -> ")

    # envia a mensagem enquanto nao for a mensagem quit
    while message != 'quit':
        soc.sendall(message.encode("utf8"))
        if soc.recv(5120).decode("utf8") == "-":
            pass

        message = input(" -> ")
        
    # se for quit envia a mensagem quit para o servidor fechar a conexão
    soc.send(b'--quit--')

if __name__ == "__main__":
  main()