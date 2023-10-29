print("welcome to tip calculator")
bill = float(input("what is the total bill? Rs: "))
tip = int(input("how much tip you want to give ? 10, 12, 15"))
people = int(input("no of people going to split"))
bill_with_tip = tip/100 * bill + bill
print(bill_with_tip)
bill_per_person = bill_with_tip/people
print(bill_per_person)
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Bill per person is {final_amount} Rs :")
