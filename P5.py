def generate_table(operation, number):
    table = []
    for i in range(1, 11):
        if operation == 'A':  
            result = number + i
            table.append(f"{number} + {i} = {result}")
        elif operation == 'S':  
            result = number - i
            table.append(f"{number} - {i} = {result}")
        elif operation == 'M':  
            result = number * i
            table.append(f"{number} * {i} = {result}")
        elif operation == 'D':  
            if i != 0:  
                result = number / i
                table.append(f"{number} / {i} = {result}")
    return table

print("Table codes: A = add, S = subtract, M = multiply, D = divide")
table_code = input("Select table code: ").upper()

if table_code in ['A', 'S', 'M', 'D']:
    number = float(input("Enter number for table: "))
    operation = {'A': 'Add', 'S': 'Subtract', 'M': 'Multiply', 'D': 'Divide'}[table_code]
    print(operation)
    
    for item in generate_table(table_code, number):
        print(item)
    print("---done")
else:
    print("Invalid table code. enter A, S, M, or D.")

print("Table codes: A = add, S = subtract, M = multiply, D = divide")

print("Table codes: A = add, S = subtract, M = multiply, D = divide")

run_program = True

while run_program:
    action = input("Select table code: ")
    num = float(input("Enter number for table: "))
    
    if action.upper() == 'A':
        print("Add")
        for i in range(1, 11):
            result = num + i
            print(f"{result} = {num} + {i}")
    elif action.upper() == 'S':
        print("Subtract")
        for i in range(1, 11):
            result = num - i
            print(f"{result} = {num} - {i}")
    elif action.upper() == 'M':
        print("Multiply")
        for i in range(1, 11):
            result = num * i
            print(f"{result} = {num} * {i}")
    elif action.upper() == 'D':
        print("Divide")
        for i in range(1, 11):
            if i != 0:
                result = num / i
                print(f"{result} = {num} / {i}")
            else:
                print("Cannot divide by zero.")
    
    run_again = input("---done\nDo you want to run again? (y/n): ")
    if run_again.lower() != 'y':
        run_program = False
        
        
print("Table codes: A = add, S = subtract, M = multiply, D = divide")

while True:
    action = input("Select table code: ")
    num = float(input("Enter number for table: "))
    
    if action.upper() == 'A':
        print("Add")
        for i in range(1, 11):
            result = num + i
            print(f"{result} = {num} + {i}")
    elif action.upper() == 'S':
        print("Subtract")
        for i in range(1, 11):
            result = num - i
            print(f"{result} = {num} - {i}")
    elif action.upper() == 'M':
        print("Multiply")
        for i in range(1, 11):
            result = num * i
            print(f"{result} = {num} * {i}")
    elif action.upper() == 'D':
        print("Divide")
        for i in range(1, 11):
            if i != 0:
                result = num / i
                print(f"{result} = {num} / {i}")
            else:
                print("Cannot divide by zero.")
    
    run_again = input("---done\nDo you want to run again? (y/n): ")
    if run_again.lower() != 'y':
        break
