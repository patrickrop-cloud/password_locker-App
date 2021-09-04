import unittest #importing unit test module
from user import User 

class TestUser(unittest.TestCase):
    '''
    This is a test class that defines test cases for user class behaviours
    Args:
        unittest.Testcase:Testcase class that helps in creating test cases.
    '''


    def setUp(self):
        '''
        SetUp method is used to run before a test case.
        '''

        self.new_user = User('patrick', '123')

    def test_init(self):
        '''
        This is a test case to test whether the object is initilized properly.

        '''
        self.assertTrue(self.new_user.username, 'patrick')
        self.assertTrue(self.new_user,'password')






