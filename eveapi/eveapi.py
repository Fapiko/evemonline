from account import Account


class EveAPI:
    def __init__(self, key_id, verification_code):
        self.keyId = key_id
        self.verificationCode = verification_code
        self.account = Account(self)
