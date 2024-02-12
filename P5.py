print("Table codes: A = add, S = subtract, M = multiple, D = divide")

table = True

while table:
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

table = True

while table:
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

  # Ask for next iteration
  answer = input("Generate another table? (y/n): ").lower()
  table = answer == "y"

print("Goodbye!")

