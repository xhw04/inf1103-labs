# smart inventory auditor
# initialize count 0
inventory = 0
failed_count = 0

# user input (cont loop)
user_input = input("Enter stock quantity:\n")
while user_input != "quit":

    # if str/neg int
    if user_input.isdigit():
        value = int(user_input)

        # running total of inventory
        inventory += value
        print("Stock Quantity:", inventory)

        # overstock and count failed
        if value > 500:
            print("Alert", failed_count)
            failed_count += 1
            break

    else:
        print("Error")
        failed_count += 1
        break

    break

    # total unit process:v
    # num of fail/rej entry:fail user input
print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_count)
