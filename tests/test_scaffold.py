import os
from bs4 import BeautifulSoup
from unittest import TestCase
from codeeval_scaffold.scaffold import scaffold, scrape


class TestScaff(TestCase):
    def test_scrape(self):
        with open(os.path.join(os.path.dirname(__file__), '1.html')) as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            description, input, output, title = scrape(soup)
            self.assertEqual('Fizz Buzz', title)
        with open(os.path.join(os.path.dirname(__file__), '23.html')) as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            description, input, output, title = scrape(soup)
            self.assertEqual('Multiplication Tables', title)

    def test_scaffold(self):
        with open(os.path.join(os.path.dirname(__file__), '1.html')) as f:
            scaffold(1, f.read(), output_dir='target/1')
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
