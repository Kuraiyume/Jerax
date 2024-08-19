banner = """
⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⣿⣷⣤⣴⣦⣀⣠⣶⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣄⡀⠀⣼⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⣿⣿⣿⣿⣿⣿⣿⡾⢛⠋⡛⠻⣿⣿⣿⣿⣧⣴⣶⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣽⡏⠰⡈⢆⢡⣷⢀⠻⣿⣿⣿⣿⣇⡀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢻⣿⣿⣿⣻⣿⠄⢣⠘⡄⢺⡏⢄⢣⡌⠻⣿⣿⣿⣿⣿⣿⣷⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣷⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣀⣸⣿⣿⣿⣿⣿⡏⢄⠣⢌⣹⠇⡌⣼⢇⠱⡈⠿⣿⣿⣿⡿⠿⠛⠛⠛⠛⠛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠹⢿⣿⣿⣿⣷⣿⣿⣦⠑⣂⡿⠰⡐⡿⢈⠆⡑⢢⢙⡿⢉⠐⡠⠑⣈⠂⠥⠘⡀⢃⠰⠀⡌⠙⠯⣉⢩⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠹⣿⣿⣿⣽⣿⣷⣜⠏⡰⢱⡟⡠⢊⠔⣡⡿⢁⠂⡡⠄⢡⠠⠌⢠⠁⠒⡈⠄⡡⢀⠃⠤⣹⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣻⣿⣿⣿⣿⣿⣷⣤⠹⢇⠰⡁⢎⣾⠁⠂⡔⠠⠘⡀⢂⠌⠄⠌⠡⡐⢈⡐⠄⢊⣼⣿⣿⣿⣿⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⠛⠛⢻⣿⣿⣯⣿⣿⣷⣌⠢⠑⢬⡇⠌⠡⠠⠑⢂⢁⢢⡈⠌⡐⠡⠠⢁⡐⠈⢼⣿⣿⣿⣿⡿⢁⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣻⣿⣿⣿⣿⣿⣧⣍⢾⠃⠌⢂⡁⢎⣶⣿⣯⣭⡘⠰⡡⢁⠂⠤⢉⠈⠿⣿⣿⠟⢀⠂⠄⠛⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⡙⢹⣿⣿⣿⣿⣿⣿⠈⠔⠂⢤⣿⣿⣿⣿⣿⣅⠀⠹⠄⡘⢀⢂⠡⠂⢄⠠⢈⠄⠊⠌⡐⢉⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⡇⣾⣿⣿⡿⣿⣿⣿⡈⠄⢃⠘⣿⣿⣿⣿⣿⣿⠀⢠⠃⠄⠃⠄⡂⢉⠄⢂⠡⢈⠌⡐⢈⠄⡘⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣓⡘⠿⣿⢷⠙⠛⣻⠡⢈⠄⢊⡘⢿⢿⠿⠟⠃⢠⠞⣨⠐⡉⡐⢈⠤⠈⡄⢂⡁⢂⠌⠄⡂⠔⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⠱⢈⠐⠂⢾⣁⣂⣽⣆⠂⣌⣼⠇⠠⢉⠐⡀⠉⠤⢈⠳⠇⡐⠠⢁⠂⡡⠐⡠⠐⠂⠌⡐⠐⡨⠐⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠂⠌⣁⠂⡉⢹⣟⣿⣻⡯⠁⠌⢂⡁⠢⢈⢁⠒⠠⠒⡀⠆⣁⠂⠡⠄⡑⠠⠑⣈⠐⡈⠔⠠⠑⢂⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣧⠌⣀⠒⡈⡐⠻⣮⡷⠃⠌⢂⠡⠠⠑⣀⠊⠄⡑⠠⢁⠂⠤⢈⠁⠆⡐⠡⠌⣀⠂⠡⠌⢂⠡⢂⠘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣤⠒⠠⠐⠡⣀⠐⡈⠔⡈⠤⠑⡈⠄⠌⡐⢈⡁⢂⠡⠒⡈⠰⠈⢄⡁⠆⠠⠌⠡⣈⠐⡐⡈⠌⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡈⠅⠒⡀⢂⠁⠆⠰⠀⡅⠂⠌⠒⡈⠄⠰⠈⢄⠡⠐⠡⠌⢠⠐⡈⢡⠈⠔⡀⠒⢠⠐⡈⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠠⢁⠂⢿⡆⠌⡁⢺⠇⡁⢊⠐⣄⠉⠄⠃⡄⠊⠌⡐⠌⡀⠆⡁⢂⠌⡐⠠⠉⠄⢂⠁⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠘⣧⠒⡈⠄⢶⢀⠡⡞⡐⠠⢁⣞⠂⢌⠘⢠⠐⣡⡬⠴⢒⠃⡐⡈⠄⢂⠌⠡⠘⡈⠄⢊⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠹⣧⠀⢀⣤⠾⢷⡐⡈⢼⡆⢸⡇⠡⢘⣼⢳⡿⣦⠈⣤⠿⢁⢂⠁⠆⡈⠔⠠⢁⠊⠄⡡⠡⢐⠈⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢃⢹⡷⠋⢄⠂⠜⠹⢶⠾⢁⠚⢿⡴⠟⢡⣿⠓⠸⣿⠋⡐⠄⢂⠉⡐⡐⠨⠐⠡⡈⢄⡛⢁⠂⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢰⠀⡂⠿⠈⢄⡈⢂⡁⢂⠐⠂⡌⠠⠐⡈⠴⣿⢀⠡⠘⣆⠰⢈⠂⢡⠐⣀⠃⠡⢒⡼⠋⡐⠈⣴⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡀⠆⡁⢂⠡⢂⠐⡠⠐⡈⠄⠃⡄⠡⢁⠂⢼⣿⠀⠂⡅⢂⡐⠂⠌⢤⣒⠠⠬⠓⡉⠄⢒⣠⡿⠛⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠷⠶⠶⢧⠶⡶⢶⠶⡷⢶⠾⡶⢶⠷⡶⠾⠼⢿⣠⣁⣐⣠⣀⣉⣒⣰⣂⣦⣥⣖⣴⠮⠿⠳⠶⠾⠴⠿⠿⠿⠳⠶⣦⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣦⣶⣼⡟⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠀⠀⠀⠀⠀⠀⠀⠀
-------------------------------------------------
- JERAX TCP CHATROOM (Server)                   |
- FOR PUPSMB INFORMATION TECHNOLOGY ONLY        |
- DEVELOPED BY: Veilwr4ith                      |
-------------------------------------------------
"""
import socket
import threading
from datetime import datetime
import sys

clients = {}
server_socket = None

def handle_client(client_socket):
    try:
        nickname = client_socket.recv(1024).decode('utf-8')
        clients[client_socket] = nickname
        print(f"[+] Nickname set: {nickname}")

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                formatted_message = f"[{timestamp}] {nickname}: {message}"
                print(formatted_message)
                broadcast(formatted_message, client_socket)
            else:
                remove_client(client_socket)
                break
    except ConnectionResetError:
        print(f"[-] Client {clients.get(client_socket, 'unknown')} disconnected abruptly.")
        remove_client(client_socket)
    except Exception as e:
        print(f"[-] Error handling client: {e}")
        remove_client(client_socket)

def broadcast(message, sender_socket):
    clients_to_notify = list(clients.keys())
    for client in clients_to_notify:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"[-] Error sending message to client: {e}")
                remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        nickname = clients.pop(client_socket)
        print(f"[-] {nickname} has left the chat.")
        client_socket.close()

def start_server():
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(5)
    print(banner)
    print("[+] Server started. Waiting for connections...")
    
    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"[+] Accepted connection from {addr}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
    except KeyboardInterrupt:
        print("\n[-] Server Terminating...")
    finally:
        for client in clients.keys():
            client.close()
        if server_socket:
            server_socket.close()
        print("[+] Server has been shut down.")
        sys.exit(0)

if __name__ == "__main__":
    start_server()

