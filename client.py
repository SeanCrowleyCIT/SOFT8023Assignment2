import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

fullMsg = ''
while True:
    msg = s.recv(1024)
    if len(msg) <= 0:
        break
    fullMsg += msg.decode("utf-8")
    print(msg.decode("utf-8"))

print(fullMsg)


def menu():
    print("HR system 1.0")
    while True:
        id = input("Please enter Employee ID")
        choice = input("Salary(S) or Leave Query(L)")
        if choice == 'S':
            print("todo")
        elif choice == 'L':
            print('todo')
        else:
            'Invalid Query please type "S" or "L"'



def main():
    menu()


main()