def main():
  print ('\n\nThis is a monthly payment loan calculator\n')

  principal = float(input('Input the loan amount: '))
  apr = float(input('Input the annual interest rate: '))
  years = int(input('Input the amount of years: '))

  montly_interest_rate = apr / 1200
  amount_of_months = years * 12
  monthly_payment = principal * montly_interest_rate / (1 - (1 + montly_interest_rate) ** (- amount_of_months))

  print('The monthly payment for this loan is: %.2f' % monthly_payment)


while True:
  main()