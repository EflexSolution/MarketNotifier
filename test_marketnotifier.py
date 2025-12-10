# test_marketnotifier.py
"""
Tests for MarketNotifier module.
"""

import unittest
from marketnotifier import MarketNotifier

class TestMarketNotifier(unittest.TestCase):
    """Test cases for MarketNotifier class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MarketNotifier()
        self.assertIsInstance(instance, MarketNotifier)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MarketNotifier()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
