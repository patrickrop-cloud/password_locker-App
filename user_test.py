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

        self.new_user = User('patrick', '123') #creating user object

    def test_init(self):
        '''
        This is a test case to test whether the object is initilized properly.

        '''
        self.assertTrue(self.new_user.username, 'patrick')
        self.assertTrue(self.new_user,'password')

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into user list.
        '''

        self.new_user.save_acc() #saving the new user
        self.assertEqual(len(User.user_List),1)







if __name__ == '__main__':
    unittest.main()
