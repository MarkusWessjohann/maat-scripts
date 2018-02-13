import unittest
import desc_stats

class TestDescriptiveStats(unittest.TestCase):

    def setUp(self):
        pass

    def test_simple(self):
        stats = desc_stats.DescriptiveStats("Filename1", 0, [0,0,0,0,0,0])
        self.assertEqual(stats.name, "Filename1")
        self.assertEqual(stats.n_revs, 6)
        self.assertEqual(stats.total, 0)
        self.assertEqual(stats.code_lines, 6)

    def test_1_emptyLine(self):
        stats = desc_stats.DescriptiveStats("Filename2", 1, [0,0,0,0,0,0])
        self.assertEqual(stats.name, "Filename2")
        self.assertEqual(stats.n_revs, 6)
        self.assertEqual(stats.total, 0)
        self.assertEqual(stats.code_lines, 5)

    def test_3_emptyLine(self):
        stats = desc_stats.DescriptiveStats("Filename3", 3, [0,0,0,0,0,0])
        self.assertEqual(stats.name, "Filename3")
        self.assertEqual(stats.n_revs, 6)
        self.assertEqual(stats.total, 0)
        self.assertEqual(stats.code_lines, 3)

    def test_1_LineWithWhitespace(self):
        stats = desc_stats.DescriptiveStats("Filename4", 0, [0,4,0,0,0,0])
        self.assertEqual(stats.name, "Filename4")
        self.assertEqual(stats.n_revs, 6)
        self.assertEqual(stats.total, 4)
        self.assertEqual(stats.code_lines, 6)

    def test_2_LineWithWhitespace(self):
        stats = desc_stats.DescriptiveStats("Filename5", 0, [0,4,0,4,0,0])
        self.assertEqual(stats.name, "Filename5")
        self.assertEqual(stats.n_revs, 6)
        self.assertEqual(stats.total, 8)
        self.assertEqual(stats.code_lines, 6)

    def test_5_LineWithWhitespace(self):
        stats = desc_stats.DescriptiveStats("Filename6", 0, [2,4,8,4,2,0])
        self.assertEqual(stats.name, "Filename6")
        self.assertEqual(stats.n_revs, 6)
        self.assertEqual(stats.total, 20)
        self.assertEqual(stats.code_lines, 6)

    def test_4_empltyLines_5_LineWithWhitespace(self):
        stats = desc_stats.DescriptiveStats("Filename6", 5, [2,4,8,4,0,0,0,0,0])
        self.assertEqual(stats.name, "Filename6")
        self.assertEqual(stats.n_revs, 9)
        self.assertEqual(stats.total, 18)
        self.assertEqual(stats.code_lines, 4)


if __name__ == '__main__':
    unittest.main()

