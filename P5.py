print("Table codes: A = add, S = subtract, M = multiply, D = divide")

run_program = True

while run_program:
    action = input("Select table code: ").upper()
    num = float(input("Enter number for table: "))
    
    if action == 'A':
        print("Add")
        for i in range(1, 11):
            print(f"{num + i} = {num} + {i}")
    elif action == 'S':
        print("Subtract")
        for i in range(1, 11):
            print(f"{num - i} = {num} - {i}")
    elif action == 'M':
        print("Multiply")
        for i in range(1, 11):
            print(f"{num * i} = {num} * {i}")
    elif action == 'D':
        print("Divide")
        for i in range(1, 11):
            if i != 0:
                print(f"{num / i} = {num} / {i}")
            else:
                print("Cannot divide by zero.")
    
    run_again = input("---done\nDo you want to run again? (y/n): ").lower()
    if run_again != 'y':
        run_program = False

