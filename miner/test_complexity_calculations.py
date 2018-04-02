import unittest
import complexity_calculations

class TestDescriptiveStats(unittest.TestCase):

    def setUp(self):
        pass

    def test_simple(self):
        source=['1', '2', '3', '4', '5']
        complexity_by_line = complexity_calculations.calculate_complexity_in('\n'.join(source))
        self.assertEqual(len(complexity_by_line), 5)
        
    def test_simple_one_empty_line(self):
        source=['1', '2', '4', '5']
        complexity_by_line = complexity_calculations.calculate_complexity_in('\n'.join(source))
        self.assertEqual(len(complexity_by_line), 4)
        
    def test_simple_two_empty_lines(self):
        source=['1', '2', '4']
        complexity_by_line = complexity_calculations.calculate_complexity_in('\n'.join(source))
        self.assertEqual(len(complexity_by_line), 3)
    
    def test_simple_zero_complexity(self):
        source=['1', '2', '3', '4', '5']
        complexity_by_line = complexity_calculations.calculate_complexity_in('\n'.join(source))
        self.assertEqual(sum(complexity_by_line), 0)

    def test_simple_one_complexity(self):
        source=['1', '2', '  3', '4', '5']
        complexity_by_line = complexity_calculations.calculate_complexity_in('\n'.join(source))
        self.assertEqual(sum(complexity_by_line), 1)

    def test_simple_two_complexity(self):
        source=['1', '2', '  3', '  4', '5']
        complexity_by_line = complexity_calculations.calculate_complexity_in('\n'.join(source))
        self.assertEqual(sum(complexity_by_line), 2)

    def test_tab_complexity(self):
        source=['1', '2', '\t3', '\t4', '5']
        complexity_by_line = complexity_calculations.calculate_complexity_in('\n'.join(source))
        self.assertEqual(sum(complexity_by_line), 2)
    
    def test_non_empty_line_star_comment(self):
        source=['1', '2', '* This is a comment', '4', '5']
        complexity_by_line = complexity_calculations.calculate_complexity_in('\n'.join(source))
        self.assertEqual(sum(complexity_by_line), 0)

    def test_non_empty_line_backslash_star_comment(self):
        source=['1', '2', '\* This is a comment', '4', '5']
        complexity_by_line = complexity_calculations.calculate_complexity_in('\n'.join(source))
        self.assertEqual(sum(complexity_by_line), 0)

    def test_empty_line_star_post_whitspace(self):
        source=['1', '2', '*     ', '4', '5']
        complexity_by_line = complexity_calculations.calculate_complexity_in('\n'.join(source))
        self.assertEqual(sum(complexity_by_line), 0)

    def test_empty_line_backslash_star_post_whitspace(self):
        source=['1', '2', '\*     ', '4', '5']
        complexity_by_line = complexity_calculations.calculate_complexity_in('\n'.join(source))
        self.assertEqual(sum(complexity_by_line), 0)

    def test_non_empty_line_star_pre_whitspace(self):
        source=['1', '2', '  *', '4', '5']
        complexity_by_line = complexity_calculations.calculate_complexity_in('\n'.join(source))
        self.assertEqual(sum(complexity_by_line), 1)

    def test_empty_line_backslash_star_pre_whitspace(self):
        source=['1', '2', '   \*', '4', '5']
        complexity_by_line = complexity_calculations.calculate_complexity_in('\n'.join(source))
        self.assertEqual(sum(complexity_by_line), 0)

    def test_empty_line_star(self):
        source=['1', '2', '*', '4', '5']
        complexity_by_line = complexity_calculations.calculate_complexity_in('\n'.join(source))
        self.assertEqual(sum(complexity_by_line), 0)

    def test_empty_line_backslash_star(self):
        source=['1', '2', '\*', '4', '5']
        complexity_by_line = complexity_calculations.calculate_complexity_in('\n'.join(source))
        self.assertEqual(sum(complexity_by_line), 0)

    def test_empty_line_backslash_star_star(self):
        source=['*', '*', '\*', '*', '\*']
        complexity_by_line = complexity_calculations.calculate_complexity_in('\n'.join(source))
        self.assertEqual(sum(complexity_by_line), 0)

if __name__ == '__main__':
    unittest.main()

