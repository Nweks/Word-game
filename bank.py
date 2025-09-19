class Bank:
    def __init__(self, name):
        self.name = name

    def bank_details(self):
        return 'loan_bank_name: %s' %(self.name)


    def personal_details(self):
        name = input('Enter your name: ')
        age = int(input('Enter your age(must be over 18): '))
        if age < 18:
            print('You are not qualified for this loan')
            
        bvn = int(input('Enter your bvn: '))
        collateral = input('Enter the collateral: ')
        print('You have succesfully entered your details')

    def Terms_and_conditions(self):
         print('Welcome to Fair money loan services, we are glad you chose us to be your number 1 loan app. By clicking yes below you have agreed to borrow a loan from us which will be paid back in due time. \n We also like to inform you that failure to pay back in due time will result to seizure of the collateral listed above .')
         Agreement = input('Yes or No')
         if Agreement == 'no':
             print('You are not qualified for this loan')

         else:
             print('You are qualified for the loan') 

    def borrow(self):
        amount = int(input('Enter the amount you want to borrow (must not be more than 1,000,00): '))
        print(f'You have successfully borrow {amount} naira')

    def pay_back(self):
        principal =  int(input('Entered the amount you borrowed in Naira (Must not be more than 1,ooo,ooo): '))
        due_date = int(input('Enter when you will be paying back(3months, 6 months, 12months): '))
        rate = 0.2 #20% annual rate

        time_in_months = due_date/12

        interest = principal * rate * time_in_months    

        total_payment = principal + interest

        print(f'Total payment after {due_date} month is {total_payment} Naira  ')           
    
            


    