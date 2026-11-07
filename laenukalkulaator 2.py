def new_loan():
    while True:

        try:
         amount = float(input("Whats the loaned amount?: "))
         interest = float(input("Whats the interest rate? "))
         time = float(input("Whats the time the loan was taken (years)? "))

        except ValueError:
            print("Only takes numbers!")
            continue

        if amount < 0 or interest < 0 or time < 0:
            print("error, please try again!")
            
        else:
            print("loan info inputted!")
            return amount, interest, time

def loan_amount(amount):
    print("Loan amount is", amount, "euros")

def payback_information(amount, interest, time):
    payback_amount = amount * ((interest/100) + 1)
    monthly_payment = amount/time/12
    print("payback amount is", round(payback_amount, 2), "euros")
    print("monthly payment is", round(monthly_payment, 2), "euros")

def is_error(amount, time):
    if amount == 0 or time == 0:
        return True
    else:
        return False

#initial values

amount = 0
interest = 0
time = 0

print("Welcome to loan program")

while True:
    print("How can we help?")

    menu = input(

        "1 for new loan, 2 for loan amount"
        "3 for payback information, 4 to clean loan"
        "5 for summary, else for exit: "
        
    )

    if menu == "1":
        amount, interest, time = new_loan()

    elif menu == "2":
        if is_error(amount, time):
            print("Enter new loan!")
        else:
            loan_amount(amount)

    elif menu == "3":
        if is_error(amount, time):
            print("Enter new loan!")
        else:
            payback_information(amount, interest, time)
    elif menu == "4":
        if amount + interest + time == 0:
            pass
        else:
         amount = 0
         interest = 0
         time = 0
         print("loan cleaned!")

    elif menu == "5":

        if is_error(amount, time):
            print("Enter new loan")
            pass
        else:
            print("The complete summary of the loan:")
            print("The loan amount is", loan_amount(amount))
            print("The payback amount is", payback_information(amount, interest, time))


    else:
        print("Thank you for using this program")
        break
