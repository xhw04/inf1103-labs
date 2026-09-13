
# smart inventory auditor
# inventory is 0
inventory = 0
# user input
user_input = input("Enter stock quantity:")
while user_input != "quit":
    # if str/neg int
    if user_input.isdigit():
        value = int(user_input)
        print("Stock Quantity:", value)
        if value > 500:
            print("Alert")
            break
    else:
        print("Error")
    break

else:
    # reporting
    print("Total Units Processed", value)
    print("Number of Failed/Rejected Entries", user_input)
