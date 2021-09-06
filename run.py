#!/usr/bin/env python3.8
import random
# import string
from user import User
from credentials import Logins #importing credential class.

#create a user account
def create_acc(username,password):
    '''
    This function creates a new user account.
    '''
    new_acc = User(username,password)
    return new_acc

    #save new account
def save_accs(acc):
    '''
    This is a method to save a newly created account.
    '''
    acc.save_acc()

#function to verify user account
def verify_acc(username,password):
    '''
    this is a function to verify an account.
    '''
    check_acc = Logins.check_acc(username,password)
    return check_acc

    #display account
def display_acc():
    '''
    This method displays user accounts.
    '''
    return User.display_acc()


def main():
    print("Hello, welcome to your password locker. Enter your name")
    username = input()
    print(f"Hello {username}. What would you like to do?")
    print('\n')


    while True:
        print("Use the short codes below: \n ca - create new acc, del - delete, da - display acc, lg - login, exit - exit password locker")
        short_code = input().lower().strip()


        if short_code == 'ca':
            print("Create a new account")
            username = input()

            print("Create Password")
            password = input()

            print('Confirm password')
            confirm_password = input()

            while confirm_password !=password:
                print("Wrong password")
                print("Enter password")
                password = input()
                print("confirm password")
                confirm_password = input()
                # print(f"Succesful! A new account has been created for: {username} with password {password}")
                # print('\n')

            else:
                print(f"Succesful! {username} account created succesfully!")
                print('\n')

            save_accs(create_acc(username,password))
            print('\n')
            print(f"New Acc {username}  with password {password} created")
            print('\n')
            
       
            print("Welcome to your account. Proceed to login")
            print("username")
            entered_username = input()
            
            print("Password")
            entered_password = input()


          
            while entered_username != username or entered_password != password:
                  print("Invalid username or password")
                  print("username")
                  username = input()
                  
                  print("password")
                  password = input()
            else:
                print("\n")
                print("successfull login")

        elif short_code =='lg':
            print("Welcome")
            print("Username")
            default_username = input()
            print("Password")
            default_password = input()
            print("\n")
            
            while default_username != 'newuser' or default_password != '12345':
                print("Wrong username or password?")
                print("Use username newuser and password 12345 to login") 
                print("\n")
                
                print("Enter Username")
                default_username =input()
                
                print("Enter password")
                default_password = input()
            else:
                print('successful login')


        elif short_code == 'da':
                if display_acc():
                    print("Here is a list of all your accs created and passwords")
                    print('\n')
                
                    for acc in save_accs():
                        print(f"{acc.username} {acc.password}")
                        print('\n')

                else:
                    print('\n')
                    print("Can't find account")
                    print('\n')
        elif short_code == 'del':
                print('Enter the username to delete')
                username = input()

              
                User.delete_acc(username)
                print(f"Your acc {username} has been deleted successfully") 
               
                
        elif short_code == 'exit':
            print("***Thank you for choosing password locker...***")
        else:print("I really din't pick that.Please use the short codes")


if __name__=='__main__':
    main()
            
    
