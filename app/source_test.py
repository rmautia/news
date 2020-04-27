import unittest
from models import Source

Source = Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test behaviour of the source class
    '''
    def setUp(self):
        '''
        Method to run before every Test
        '''
        self.new_source= Source( "ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.","http://abcnews.go.com","2020-04-26T23:53:06Z","general", "Your aunt's YouTube videos about how coronavirus is a bioweapon")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
    unittest.main()
