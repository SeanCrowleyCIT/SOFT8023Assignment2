import socket
import employees




#network logic
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been made")
    clientsocket.send(bytes("Welcome to the server", "utf-8"))
    clientsocket.close()
    break


def menu():
    print("HR system 1.0")


def main():
    dic = input('Select Year')
    employee = input('Select Player ID')
    test = employees.getTotalSalary(dic, employee)
    print(test)


main()
