class MpesaTransaction:
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.amount = amount

    def process_transaction(self):
        raise NotImplementedError("subclass to use this method")


class DepositTransaction(MpesaTransaction):
    def process_transaction(self):
        print(f"Deposit transaction with ID {self.transaction_id} processed. Amount {self.amount}")


class WithdrawalTransaction(MpesaTransaction):
    def process_transaction(self):
        print(f"Withdrawal transaction with ID {self.transaction_id} processed. Amount {self.amount}")


class PaymentTransaction(MpesaTransaction):
    def __init__(self, transaction_id, amount, recepient):
        super().__init__(transaction_id, amount)
        self.recepient = recepient

    def process_transaction(self):
        print(
            f"Payment transaction with ID{self.transaction_id} processed. Amount {self.amount}.Recepient { self.recepient}")


deposit = DepositTransaction("DHTY", 2000)
deposit.process_transaction()
withdraw = WithdrawalTransaction("AINH", 1000)
withdraw.process_transaction()
payment = PaymentTransaction("CBUB", 500, "Bob")
payment.process_transaction()
