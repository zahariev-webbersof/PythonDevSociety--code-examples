def compound_interest(principal, rate, time):
    amount = principal * (1 + rate/100) ** time
    return amount

principal = 1000
rate = 5
time = 5

future_value = compound_interest(principal, rate, time)
print("Future value:", future_value)
