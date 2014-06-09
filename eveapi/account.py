class Account:
    def __init__(self, key_id, verification_code):
        """
        Returns information about the API key and a list of the characters exposed by it.
        :type key_id: int
        :param key_id:
        :type verification_code: str
        :param verification_code:
        :return:
        """
        self.keyId = key_id
        self.verificationCode = verification_code

