def generate_table():
  action = input("Select table code (A = add, S = subtract, M = multiply, D = divide): ").upper()
  try:
    number = float(input("Enter number for the table: "))
  except ValueError:
    print("Invalid input. Please enter a number.")
    return

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

  for i in range(1, 11):
    result = number * (i / 10) if action == "D" else eval(f"{number}{operation}{i}")
    print(f"{result:.1f} = {number}{operation}{i}")

print("Welcome to the Table Generator!")
generate_table()
print("Done! Thank you for using the Table Generator.")


