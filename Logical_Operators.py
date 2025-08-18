# Logical Operators

has_high_income = True
has_good_credit = False

# AND Operation where both conditions must be True
if has_high_income and has_good_credit:
    print("Eligible for Loan")

else:
    print("Not Eligible for Loan")


can_fight_crime = True
wears_a_cape = False

# OR Operation where at least on condition must be True
if can_fight_crime or wears_a_cape:
    print("Is a Superhero")

else:
    print("Not a Superhero")


# NOT Operation, simply changing one variable from True to False and Vice-Versa

got_good_marks = True
failed_at_any_subject = False

if got_good_marks and not failed_at_any_subject:
    print("Is the topper of the class")

else:
    print("Is not the Topper of the class")
