import unittest
from user import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user and credentials class behaviours.

    Args: 
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Setup method to run before each test case
        '''
        self.new_user = User("Liz", "Kimita", "Shiko", "shikolove")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Liz")
        self.assertEqual(self.new_user.last_name,"Kimita")
        self.assertEqual(self.new_user.user_name, "Shiko")
        self.assertEqual(self.new_user.password, "shikolove")

if __name__ == '__main__':
    unittest.main()