# create account class with 2 attributes ie balance and account no.
# Create methods for debit and printing the balance

class account:
    def __init__(self, blnc, accno):
        self.blnc = blnc
        self.accno = accno
    
    def show_balance(self):
        print(f'Current Balance: {self.blnc}')
        
    def credit_balance(self):
        cr = int(input('Enter credit amount: '))
        self.blnc = self.blnc + cr
        print('*Credit Success*')
    
    def debit_balance(self):
        dr = int(input('Enter debit amount: '))
        self.blnc = self.blnc - dr
        print('*Debit Success*')

# Creating object then performing tasks: 
ramesh = account(3000, 'A134')
ramesh.show_balance()
print()
ramesh.credit_balance()
print()
ramesh.show_balance()
print()
ramesh.debit_balance()
print()
ramesh.show_balance()
print()


# additional feature which was not asked but I'm making because it's ' my life, my rules! '

while True: 
    pass # I'll do it later zzz...
