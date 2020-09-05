#!/usr/bin/env python3.8
from account import Account


def create_account(details, login_username, password):
    new_account = Account(details, login_username, password)
    return new_account


def save_account(account):
    account.save_account()


def delete_account(account):
    account.delete_account()


def find_account_by_details(details):
    return Account.find_account_by_details(details)


def account_exists(details):
    return Account.account_exists(details)


def display_all_accounts():
    return Account.display_all_accounts()


def main():
    print(Account.display_all_accounts.__doc__)
    print(
        "Hey there!Welcome to your account list. I have all details concerning your various accounts and I am here to ensure that your credentials are maintained"
    )
    user_name = input()
    print(f"Hey there {user_name}. How would you like to proceed?")
    print("\n")
    while True:
        print(
            "Use these short codes : ca - create a new account, dc - display accounts, fa - find an account, da - delete an account, ex- exit the account list"
        )

        short_code = input()

        if short_code == "ca":
            print("New Account Credentials")
            print("-" * 10)

            print("Details ...")
            details = input()

            print("Login username ...")
            login_username = input()

            print("Password ...")
            password = input()

            save_account(create_account(details, login_username, password))
            print("\n")
            print(f"New Account {details} {login_username} {password} created")
            print("\n")

        elif short_code == "dc":
            if display_all_accounts():
                print("Here is a list of all your accounts with their credentials")
                print("\n")

                for account in display_all_accounts():
                    print(
                        f"{account.details} {account.login_username} {account.password}"
                    )

                    print("\n")
                else:
                    print("\n")
                    print(
                        "You do not seem to have any accounts along with their credentials saved yet"
                    )

        elif short_code == "fa":
            print(
                "Please enter the details or the name of the account you wish to search for"
            )

            search_details = input()
            if account_exists(search_details):
                search_account = find_account_by_details(search_details)

                print(f"{search_account.details} {search_account.login_username}")
                print("-" * 20)

                print(f"password ... {search_account.password}")
            else:
                print("That account and its credentials does not exist")
        elif short_code == "da":

            print("Enter the account you wish to delete")
            print("\n")
            search_details = input()
            if account_exists(search_details):
                search_account = find_account_by_details(search_details)
                # changed here
                Account.account_list.remove(search_account)
            else:
                print("Account not found")
        elif short_code == "ex":
            print("Bye .....")
            break
        else:
            print("I really didn't get that.Please use the short codes")


if __name__ == "__main__":
    main()
