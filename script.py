def tax():
    """
    Calculates the tax amount based on the level of income.
    
    """
    s = float(input("Please input your Salary (NOK):"))
    
    if s <= 0:
        print("You do not need to pay tax. Work Harder!!!!!!")
    elif s <= 100_000:
        tax = s * 0.02
        print (f"Your tax amount is {tax:.2f}")
    else :
        tax = s * 0.15
        print(f"Your tax amount is {tax:.2f}")

tax()