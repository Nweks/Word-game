class account:

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

    def details(self):
        return 'Account_name: %s\nAccount_balance: %s' %(self.owner, self.balance)

    def deposit(self):
        deposit = int(input('please enter the amount: '))
        self.balance += deposit 

        print('Deposit Accepted')
        print('Thank you for banking with us')

    def withdrawal(self):
        withdrawal = int(input('How much do you want to withdraw: '))
        
        if withdrawal > self.balance:
            print('Insufficient Funds')
            withdrawal = int(input('Enter a new amount: '))
            
        if withdrawal  < self.balance:
            print('Withdrawal successful')
            print('Thanks for banking with us')

        self.balance -= withdrawal

        

        


                  
                  
        