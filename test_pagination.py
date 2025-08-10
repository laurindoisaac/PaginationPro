# test_pagination.py
"""
Tests for Pagination module.
"""

import unittest
from pagination import Pagination

class TestPagination(unittest.TestCase):
    """Test cases for Pagination class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Pagination()
        self.assertIsInstance(instance, Pagination)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Pagination()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
