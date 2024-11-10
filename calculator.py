def calculator():
        
    print("Select a operation based on your needs:")
    print("1. Addition:")
    print("2. Subtraction:")
    print("3. Multiplication:")
    print("4. Division:")
    print("4. Modulus:")

    def add(n,n1):
        return n+n1
    def sub(n,n1):
        return n-n1
    def mult(n,n1):
        return n*n1
    def div(n,n1):
        return n/n1
    def mod(n,n1):
        return n % n1
    while True:
            choice = input("Enter choice (1/2/3/4/5) or 'exit' to quit: ")
            
            if choice.lower() == 'exit':
                print("Exiting the calculator.")
                break
            
            if choice in ['1', '2', '3', '4','5']:
                    num = float(input("Enter a first number: "))
                    num1 = float(input("Enter a second number: "))
                    
                    if choice == '1':
                        print(f"Result: {add(num, num1)}")
                    elif choice == '2':
                        print(f"Result: {sub(num, num1)}")
                    elif choice == '3':
                        print(f"Result: {mult(num, num1)}")
                    elif choice == '4':
                        print(f"Result: {div(num, num1)}")
                    elif choice == '5':
                        print(f"Result: {mod(num, num1)}")
            else:
                print("Invalid choice. Please select a valid operation.")
calculator()