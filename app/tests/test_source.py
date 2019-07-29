import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('independent','Independent','US and China clashing at sea is only a matter of time','Defence secretaries Jim Mattis and Wei Fenghe expected to discuss conflict between two countries','https://www.independent.co.uk/news/world/asia/us-china-south-sea-navy-war-ship-tension-jim-mattis-wei-fenghe-a8625676.html')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))