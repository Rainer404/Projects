print('\nIncome Tax Calculator\n')

# inputs

grossincome = float(input('Enter the gross income: '))
numdependents = int(input('Enter the number of dependents: '))

# tax laws

flat_tax_rate = 0.20
standard_deduction = 10000
dependent_deduction = 3000

# deduction total

total_deduction = standard_deduction + (dependent_deduction * numdependents)

# tax amount

income_tax = (grossincome - total_deduction) * flat_tax_rate

print(f"The income tax is ${income_tax:.2f}")


