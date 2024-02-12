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

  # Print done
  print("Done!")
  
  # No need to ask for next iteration

print("Goodbye!")

def generate_table():
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

  # Print done
  print("Done!")

generate_table()
print("Goodbye!")

def generate_table():
  action = input("Select table code (A = add, S = subtract, M = multiply, D = divide): ").upper()
  try:
    number = float(input("Enter number for the table: "))
  except ValueError:
    print("Invalid input. Please enter a number.")
    return

  # Use if statements to perform the operation based on action
  if action == "A":
    operation = " + "
  elif action == "S":
    operation = " - "
  elif action == "M":
    operation = " * "
  elif action == "D":
    operation = " / "
  else:
    print("Invalid action. Please choose A, S, M, or D.")
    return

  # Generate and print the table
  for i in range(1, 11):
    result = number * (i / 10) if action == "D" else eval(f"{number}{operation}{i}")
    print(f"{result:.1f} = {number}{operation}{i}")

print("Welcome to the Table Generator!")
generate_table()  # Call the function once
print("Done! Thank you for using the Table Generator.")


