
# Start

import math

# allow the user to choose which calculations they would like to use
# the input shouldn't be case sensitive
choice_investment = "Investment  -   to calculate the amount of interest you'll earn on your investment."
choice_bond = "Bond        -   to calculate the amount you'll have to pay on a home loan.\n\nPlease choose either an investment or a bond: "
choice = input(f"We have two choices avaliable for you:\n\n{choice_investment}\n{choice_bond}").lower()

# I have used a while loop to counteract if an invalid choice has been inputted and to continue normally again after a correct input has been entered
while True:
  if choice == "investment":
    money = input("\nHow much money would you like to deposit?: ")
    money = float(money)
    interest_rate = input("\nWhat is the interest rate?: ")
    # I added an algorithm if a % sign is inputted that it wont affect the formula and output
    interest_rate = (interest_rate).strip("%")
    interest_rate = ((float(interest_rate))/100)
    years = float(input("\nHow many years are you planning to invest for?: "))
    interest = input("\nDo you want 'simple' or 'compound' interest?: ").lower()
    # the formula for simple interest is (total_amount = money * (1 + interest_rate * years))
    # the formula for compound interest is (total_mount = money * ((1 + interest_rate ) ** years))
    if interest == "simple" :
      total_amount = money * (1 + interest_rate * years)
      float("%.2f" % (total_amount))
      print(f"\n\nThe gross amount of money after investing will be £{total_amount}. ")
    elif interest == "compound":
      total_amount = (money * ((1 + interest_rate ) ** years))
      total_amount = float("%.2f" % (total_amount))
      print(f"\n\nThe gross amount of money after investing will be £{total_amount}. ")
    break

  elif choice == "bond":
    value = input("\nWhat is the value of the house in £'s'?: ")
    value = float(value)
    interest_rate = input("\nWhat is the interest rate?: ")
    # I again added my algorithm that if a % sign is inputted it wont affect the formula and output
    interest_rate = (interest_rate).strip("%")
    interest_rate = ((float(interest_rate))/100)
    months = input("\nWithin how many months do you plan to repay the bond?: ")
    months = int(months)
    monthly_interest_rate = (interest_rate / 12)
    total_per_month = (monthly_interest_rate * value) / (1 - (1 + monthly_interest_rate) ** (-months))
    total_per_month = float("%.2f" % (total_per_month))
    print(f"\n\nThe amount to pay each month will be £{total_per_month}. ")
    break

  else:    
    # this input function will keep repeating if an invalid choice is inputted, until a valid choice is inputted instead
    choice = input("\nEnter either 'investment' or 'bond': ")
    continue

# Stop 
