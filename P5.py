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

print("Welcome to the Table Generator!")

# Get table action and number
action = input("Select table code (A = add, S = subtract, M = multiply, D = divide): ").upper()
try:
  number = float(input("Enter number for the table: "))
except ValueError:
  print("Invalid input. Please enter a number.")
  exit()

# Initialize an empty list to store results
results = []

# Use a for loop to iterate from 1 to 10
for i in range(1, 11):
  # Use if statements to perform the operation based on action
  if action == "A":
    result = number + i
  elif action == "S":
    result = number - i
  elif action == "M":
    result = number * i
  elif action == "D":
    if number == 0:
      print("Error: Cannot divide by zero.")
      break  # Exit the loop if division by zero
    else:
      result = number / i
  else:
    print("Invalid action. Please choose A, S, M, or D.")
    break  # Exit the loop if invalid action

  # Add the result to the list
  results.append(result)

# Print the table header
print(f"\n{action} table for {number:.1f}\n")

# Use a for loop to print each result with formatting
for i, result in enumerate(results):
  print(f"{result:.1f} = {number}{action}{i+1}")

# Thank the user
print("\nThank you for using the Table Generator!")

