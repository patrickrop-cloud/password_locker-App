import unittest #importing unit test module
from user import User #importing the user class

class TestUser(unittest.TestCase):
    '''
    This is a test class that defines test cases for user class behaviours
    Args:
        unittest.Testcase:Testcase class that helps in creating test cases.
    '''


    def setUp(self):
        '''
        SetUp method is used to run before each test case.
        '''

        self.new_user = User('patrick', '0000') #creating user object



    def test_init(self):
        '''
        This is a test case to test whether the object is initilized properly.

        '''
        self.assertTrue(self.new_user.username, 'patrick')
        self.assertTrue(self.new_user.password,'0000')



    def test_save_acc(self):
        '''
        test_save_user test case to test if the user object is saved into user list.
        '''

        self.new_user.save_acc() #saving the new user
        self.assertEqual(len(User.user_List),1)

    def tearDown(self):
        '''
        This is a method to clean up after each testcase has run.
        '''

        User.user_List = []


    def test_display_acc(self):
        '''
        The method returns the list of saved accounts.
        '''
        self.assertEqual(User.display_acc(),User.user_List) #displaying users list.



    def test_delete_acc(self):
        '''
        test_delete account to test if we can remove an account from our user list
        '''
        self.new_user.save_acc()
        test_user = User("Test","acc") #new acc
        test_user.save_acc()

        self.new_user.delete_acc() #deleting a user account
        self.assertEqual(len(User.user_List),1)

    # def test_save_multiple_acc(self):
    #     '''
    #     test_save_multiple_user to check if we can save multiple user objects to our user_list
    #     '''


if __name__ == '__main__':
    unittest.main()
