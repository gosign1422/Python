print("Welcome to the tip calculator.")
bill = float(input("Enter the amount of your bill: $"))
tip = int(input("How much tip do you want to give?(Eg.5 10 15) "))
people = int(input("Among how many people do you want to split the bill? "))
bill1 = (bill+bill*(tip/100))/people
final_bill = round(bill1,2)
print(f"Each person has to pay: ${final_bill}")