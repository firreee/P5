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
