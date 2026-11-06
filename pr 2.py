while True:

    print("Welcome to the Pattern Generator and Number Analyzer!")
    print("Select an option:")
    print("1. Generate Pattern")
    print("2. Analyze Number")
    print("3. Exit")
    option = input("Enter your choice: ")
    if option == "1":
        rows = int(input("Enter the number of rows for the pattern: "))
        print("Pattern")
        for i in range(1, rows + 1):
            print("*" * i) 
    if option =="2":
        start = int(input("Enter your starting number: "))
        end = int(input("Enter your ending number: "))
        for number in range (start,end+1):
            if number % 2 == 0:
                print(f"{number} is Even")
            else:
                print(F"{number} is odd")
        print("sum of all number",sum(range(start,end)))
    if option == "3":
        print("Exiting the program. Goodbye!")
        break

    