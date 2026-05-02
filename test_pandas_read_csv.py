import unittest
import pandas as pd
import numpy as np
import sys
from io import StringIO

# Note: These tests assume the CSV file exists at the specified path
# For production use, consider using mock data or fixtures


class TestPandasReadCSV(unittest.TestCase):
    """Test suite for pandas CSV reading and data processing"""
    
    @classmethod
    def setUpClass(cls):
        """Load test data once for all tests"""
        try:
            cls.df_Students_Information = pd.read_csv("C:/Workspace/StudentsInformation.csv")
        except FileNotFoundError:
            print("Warning: StudentsInformation.csv not found. Some tests will be skipped.")
            cls.df_Students_Information = None
    
    def test_dataframe_loaded(self):
        """Test that CSV file is successfully loaded into DataFrame"""
        self.assertIsNotNone(self.df_Students_Information)
        self.assertGreater(len(self.df_Students_Information), 0)
    
    def test_required_columns_exist(self):
        """Test that required columns exist in the dataset"""
        if self.df_Students_Information is None:
            self.skipTest("CSV file not available")
        
        required_columns = ['First name', 'Second name', 'Last name', 'Age']
        for col in required_columns:
            self.assertIn(col, self.df_Students_Information.columns)
    
    def test_column_selection(self):
        """Test selecting specific columns from DataFrame"""
        if self.df_Students_Information is None:
            self.skipTest("CSV file not available")
        
        df_display = self.df_Students_Information[['First name', 'Second name', 'Last name']]
        self.assertEqual(len(df_display.columns), 3)
        self.assertListEqual(list(df_display.columns), 
                           ['First name', 'Second name', 'Last name'])
    
    def test_column_name_uppercase_conversion(self):
        """Test converting column names to uppercase"""
        if self.df_Students_Information is None:
            self.skipTest("CSV file not available")
        
        df_display = self.df_Students_Information[['First name', 'Second name', 'Last name']]
        df_display.columns = df_display.columns.str.upper()
        
        expected_columns = ['FIRST NAME', 'SECOND NAME', 'LAST NAME']
        self.assertListEqual(list(df_display.columns), expected_columns)
    
    def test_mean_age_calculation(self):
        """Test calculation of mean age from Age column"""
        if self.df_Students_Information is None:
            self.skipTest("CSV file not available")
        
        age = self.df_Students_Information['Age']
        mean_age = np.mean(age)
        
        # Mean age should be a positive number
        self.assertGreater(mean_age, 0)
        # Mean age should be within reasonable student age range
        self.assertGreater(mean_age, 10)
        self.assertLess(mean_age, 100)
    
    def test_age_column_contains_numbers(self):
        """Test that Age column contains numeric data"""
        if self.df_Students_Information is None:
            self.skipTest("CSV file not available")
        
        age = self.df_Students_Information['Age']
        self.assertTrue(pd.api.types.is_numeric_dtype(age))
    
    def test_dataframe_to_string_formatting(self):
        """Test DataFrame to_string output formatting"""
        if self.df_Students_Information is None:
            self.skipTest("CSV file not available")
        
        df_display = self.df_Students_Information[['First name', 'Second name', 'Last name']]
        df_display.columns = df_display.columns.str.upper()
        
        output = df_display.to_string(index=False)
        
        # Output should be a string with content
        self.assertIsInstance(output, str)
        self.assertGreater(len(output), 0)
        # Output should not contain index column numbers
        self.assertNotIn('0', output.split('\n')[1][:5])


if __name__ == '__main__':
    unittest.main()
