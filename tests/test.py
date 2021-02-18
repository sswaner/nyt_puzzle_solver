import unittest
import os
import datetime

#import vertex
from nytpuzzlesolver.vertex.main import solve_puzzle

class Test_Set(unittest.TestCase):
    expected = {'best_answer': ('acronyms', 'staind'),
                'error': '',
                'matching_words': 335,
                'process_time': datetime.timedelta(microseconds=191975),
                'results': [('card', 'discriminatory'),
                            ('mind', 'discriminatory'),
                            ('stand', 'discriminatory'),
                            ('diamond', 'discriminatory'),
                            ('yard', 'discriminatory'),
                            ('raid', 'discriminatory'),
                            ('strand', 'discriminatory'),
                            ('maid', 'discriminatory'),
                            ('staind', 'discriminatory'),
                            ('candid', 'discriminatory'),
                            ('amid', 'discriminatory'),
                            ('acronyms', 'staind'),
                            ('nord', 'discriminatory'),
                            ('discard', 'discriminatory'),
                            ('discriminatory', 'yard'),
                            ('discriminatory', 'ymca'),
                            ('arid', 'discriminatory'),
                            ('sind', 'discriminatory')],
                'status': 'success',
                'total_options': 18}

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 3)), 6, "Should be 6")

    def test_puzzle(self):
      test1 = main.solve_puzzle('adsrmntryico')
      
      self.assertListEqual(self.expected['results'], test1['results'])
      self.assertEqual(self.expected['matching_words'], test1['matching_words'])
      self.assertTupleEqual(self.expected['best_answer'], test1['best_answer'])
      self.assertAlmostEqual(200000, test1['process_time'].microseconds, delta=100000)

    def test_data(self):
      assert(os.path.isfile('./vertex_words.txt'))
      
      f = open('../vertex_words.txt')
      
if __name__ == '__main__':
    unittest.main()
    print("All tests passed")