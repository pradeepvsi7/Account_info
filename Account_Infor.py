class Account():
	"""docstring for Account"""
	def __init__(self, account_no,balance):
		self.account_no = account_no
		self.balance = balance
	def add_balance(self,amt):
		self.balance = self.balance + amt
		return self.balance
	def transfer(self,account,amt):
		self.balance-=amt
		account.balance = account.balance + amt
		return self.balance
	
A1 = Account(12345,25000)
A2 = Account(6789,1000)
A1.transfer(A2,10000)
print(f"Balance of A - account is {A1.balance}")
print(f"Balance of B - account is {A2.balance}")



