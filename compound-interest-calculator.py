# Enter the interest rate (%) as a float (ex. 4% = .04).

P = int(input("What is the principal? \n \n")) 
n = int(input("How many compoundings per year? \n \n"))
r = float(input("What is the interest rate? \n \n"))
t = int(input("How many years will your money be compounded for? \n \n"))

Total_money_compounded = P * ( ((1 + (r/n)) ** (n * t)) )

print("The total amount of money you will have in", t, "years is :", Total_money_compounded)
