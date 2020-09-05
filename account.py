class Account:
    """
    Class that generates new instances of contacts.
    """

    account_list = []  # Empty contact list

    def __init__(self, details, login_username, password):

        self.details = details
        self.login_username = login_username
        self.password = password

    def save_account(self):
        """Add an account to the account list"""
        Account.account_list.append(self)

    def delete_account(self):
        """Remove an account from the account list"""
        Account.account_list.remove(self)

    @classmethod
    def display_all_accounts(cls):
        """Return all the accounts in the account list"""
        return cls.account_list

    @classmethod
    def account_exists(cls, details):
        """Check if an account exists"""
        for account in cls.account_list:
            # added if check
            if account.details == details:
                return True
        return False

    @classmethod
    def find_account_by_details(cls, details):
        """Search for an account with details in the account list. Returns the matching account if an account is found"""
        for account in cls.account_list:
            if account.details == details:
                return account
