from api_key_info import APIKeyInfo


class Account:
    def __init__(self, api_parent):
        """
        :type api_parent: EveAPI
        :param api_parent:
        :rtype
        :return:
        """
        self.apiParent = api_parent

    def api_key_info(self):
        pass