import unittest
from account import Account

class TestAccount(unittest.TestCase):
    def tearDown(self):

        Account.account_list = []
    def setUp(self):
        self.new_account = Account("Twitter","Derek","Thrifty")
    def test_init(self):

        self.assertEqual(self.new_account.details,"Twitter")
        self.assertEqual(self.new_account.login_username,"Derek")
        self.assertEqual(self.new_account.password,"Thrifty")


    def test_save_account(self):
        self.new_account.save_account()
        self.assertEqual(len(Account.account_list),1)
    def test_save_multiple_contact(self):
        self.new_account.save_account()
        test_account = Account("FuzuAccount","DerickKK","kaihavertz")
        test_account.save_account()
        self.assertEqual(len(Account.account_list),2)
    def test_delete_account(self):
        self.new_account.save_account
        test_account = Account("FuzuAccount","DerickKK","kaihavertz")
        test_account.save_account()
        self.new_account.delete_account
        self.assertEqual(len(Account.account_list),1)

    def test_display_all_accounts(self):
        self.assertEqual(Account.display_all_accounts(),Account.account_list)


    def test_account_exists(self):
       self.new_account.save_account()
       test_account = Account("FuzuAccount","DerickKK","kaihavertz")
       test_account.save_account()
       account_exists = Account.account_exists("FuzuAccount")
       self.assertTrue(account_exists)
    def test_find_account_by_details(self):
       self.new_account.save_account()
       test_account = Account("FuzuAccount","DerickKK","kaihavertz")
       test_account.save_account()
       found_account = Account.find_account_by_details("FuzuAccount")

       self.assertEqual(found_account.details,test_account.details)






if __name__ == '__main__':
    unittest.main()
