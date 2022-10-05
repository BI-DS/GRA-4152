##
#  This program simulates a bank with checking and savings accounts.
#

from accounts import CheckingAccount, SavingsAccount

# Create accounts.
ACCOUNTS_SIZE = 10
accounts = []
for i in range(ACCOUNTS_SIZE // 2) :
   accounts.append(CheckingAccount())
   
for i in range(ACCOUNTS_SIZE // 2) :
   account = SavingsAccount()
   account.setInterestRate(0.75)
   accounts.append(account)

# Execute commands.
done = False
while not done :
   action = input("D)eposit  W)ithdraw  M)onth end  Q)uit: ")
   action = action.upper()
   if action == "D" or action == "W" :  # Deposit or withdrawal.
      num = int(input("Enter account number: "))
      amount = float(input("Enter amount: "))

      if action == "D" :
         accounts[num].deposit(amount)
      else :
         accounts[num].withdraw(amount)

      print("Balance:", accounts[num].getBalance())
   elif action == "M" :   # Month end processing.
      for n in range(len(accounts)) :
         accounts[n].monthEnd()
         print(n, accounts[n].getBalance())
   elif action == "Q" :
      done = True

