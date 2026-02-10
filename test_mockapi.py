# test_mockapi.py
"""
Tests for MockApi module.
"""

import unittest
from mockapi import MockApi

class TestMockApi(unittest.TestCase):
    """Test cases for MockApi class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MockApi()
        self.assertIsInstance(instance, MockApi)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MockApi()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
