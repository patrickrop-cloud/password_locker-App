#!/usr/bin/env python3.8
import random
import string
from user import User

#create account
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
    acc.save_acc

    

