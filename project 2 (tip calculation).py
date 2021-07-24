#this code written by aadithyan
print("welcome to tip calculator")
bill_amount = float(input("what is the total bill? $"))
percentage_tip =float(input("what percentage tip would you like to give? 10 , 12 or 15 "))
split_bill = int(input("how many people to split the bill? : "))
per_tip = percentage_tip /100
mult_per_bill = bill_amount * per_tip
main_per_tip = mult_per_bill + bill_amount
split_bill = main_per_tip /split_bill
round_number = round(split_bill,2)
print(f"${round_number}")