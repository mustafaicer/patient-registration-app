from datetime import datetime
def login():
    quest = None
    while quest != "create" and quest != "read" and quest != "add" and quest != "quit":
        quest = input("\nNote page :\nFor create 'create'\nFor read 'read'\nFor add 'add'\nFor quit 'quit'\nEnter: ")
        if quest == "create":
            create_file_func()
        elif quest == "read":
            read_file_func()
        elif quest == "add":
            add_file_func()
        elif quest == "quit":
            quit()
        else:
            print("Please don't do this")

def create_file_func():
    create_file_name = input("Enter the file name you want to create along with its extension : ")
    date_now = datetime.now()
    date_now_string = "Date and time the file was created : " + date_now.strftime("%Y / %m / %d   %H : %M : %S") + "\n"
    with open(f"Notes\\{create_file_name}", "w") as create_file_var:
        create_file_var.write(date_now_string)

def add_file_func():
    add_file_name = input("Enter the file name you want to add text along with its extension : ")
    try:
        with open(f"Notes\\{add_file_name}", "a") as add_file_var:
            add_content = input(f"Add text to {add_file_var.name} file : ")
            add_content += "\n"
            add_file_var.write(add_content)
    except:
        print("File not found")
        login()

def read_file_func():
    read_file_name = input("Enter the file name you want to open along with its extension : ")
    try:
        with open(f"C:\\Users\\icerm\\Software\\Github\\projects-with-python\\notepad-app\\Notes\\{read_file_name}","r") as read_file_var:
            icerik = "\n" + read_file_var.read()
            print(icerik)
            input("Press enter for pass")
    except:
        print("File not found")
        login()

while True:
    login()