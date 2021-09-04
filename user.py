#user.py
class User:
    '''
    This is a class that generates new user instance.
    '''

    def __init__(self, username, password):
        '''
        properties of instance in user class.
        '''

        self.username = username
        self.password = password

    user_List = [] #This is an empty user list.

    def save_acc(self):
        '''
        This method saves new user to user list.
        '''

        User.user_List.append(self)



        


