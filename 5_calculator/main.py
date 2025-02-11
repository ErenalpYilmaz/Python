from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
      return n1 * n2

def divide(n1,n2):
    return n1 / n2
print(logo)

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
isDone = False
result = 0
while not isDone:
    if result == 0:
        num = float(input("What's the first number?:"))
    else:
        num = result
    for keys in operations:
        print(keys)
    operation_symbol = input("Pick an operation:")
    num2 = float(input("What's the next number?:"))

    if operation_symbol in operations:
        function = operations[operation_symbol]
        result = function(num,num2)
        print(f"{num},{operation_symbol} {num2} = {result}")
    else:
        print("Gecersiz islem")
    continue_calculate = input(f"Type 'y' to continue calculating with {result},type 'quit' to stop calculate,or type 'n' to start a new calculation:")
    if continue_calculate == "n":
        result = 0
    elif continue_calculate == "stop":
        break
    else:
        continue