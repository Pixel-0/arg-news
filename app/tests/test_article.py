import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Independent','Defence secretaries Jim Mattis and Wei Fenghe expected to discuss conflict between two countries','https://www.independent.co.uk/news/world/asia/us-china-south-sea-navy-war-ship-tension-jim-mattis-wei-fenghe-a8625676.html','https://static.independent.co.uk/s3fs-public/thumbnails/image/2018/11/09/10/south-china-sea.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))