def classify_numbers():
    while True:
        s = input("Enter a number (or type 'exit' if you want to quit): ")
        
        if s.lower() == "exit":
            print("Exiting the program.")
            break
        num = float(s)
        if num > 0:
            print(f"{num} is positive.")
        elif num< 0:
            print(f"{num} is negative.")
        else:
            print("The number is zero.")

classify_numbers()