# smart inventory auditor
# initialize count 0
inventory = 0
failed_count = 0

# user input (cont loop)
while True:
    user_input = input("Enter stock quantity:\n")

# quit
    if user_input == "quit":
        break

# if not int
    if not user_input.isdigit():
        print("Error")
        failed_count += 1
        continue

# running total of inventory
    stock_value = int(user_input)
    inventory += stock_value
    print("Stock Quantity:", stock_value)

# overstock and count failed
    if stock_value > 500:
        print("Alert", failed_count)
        failed_count += 1
        break

    # total unit process:v
    # num of fail/rej entry:fail user input
    print("Total Units Processed:", stock_value)
    print("Number of Failed/Rejected Entries", failed_count)
