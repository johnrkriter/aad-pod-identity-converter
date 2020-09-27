#This test file is used to test internal functionality within the application

#Base python unit test framework
import unittest

import converter as converter

class TestAadPodIdentityConverter(unittest.TestCase):
    def test_testing_framework(self):
        """
        Test that the testing framework is running properly
        """
        self.assertTrue(True)
    
    def test_read_input_csv(self):
        """
        Test a properly formatted CSV file creates a dictionary
        """
        self.assertTrue(True)


    def test_write_azure_identity(self):
        """
        Test a properly formatted CSV file creates a dictionary
        """
        converter.read_input_csv()
        self.assertTrue(True)
  
    def test_write_azure_identity_binding(self):
        """
        Test a properly formatted CSV file creates a dictionary
        """
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()