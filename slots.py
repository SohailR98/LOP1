def deposit(): 
    while True: 
        amount = input("Please enter an amount to play with : ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break

            else: 
                print("Please enter an amount greater than 0")

        else: 
            print("Please eneter a valid number")


    return amount

def main(): 

    balace = deposit()

    print("Your current balance is : ",balace)


main()