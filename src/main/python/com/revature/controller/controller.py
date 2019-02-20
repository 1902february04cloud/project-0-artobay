from service.service import read_input, show_help, current_user

def parse_input():
    command = input("Aliyar's Bank--> ")
    params = command.split(' ')
    return params

def run():
    show_help()
    while True:
        input_params = parse_input()
        output = read_input(input_params)
        print(output)

