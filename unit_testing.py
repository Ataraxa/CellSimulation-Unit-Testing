import unittest
import cellsim


class TissueTests(unittest.TestCase):

    def test_str_zero_matrix(self):
        tissue = cellsim.Tissue(0, 0)
        self.assertEqual(str(tissue), '')

    def test_default_setup(self):
        tissue = cellsim.Tissue()
        self.assertEqual(str(tissue), '.')
        self.assertEqual(tissue.rows, 1)
        self.assertEqual(tissue.cols, 1)
        self.assertEqual(tissue.cell_type, cellsim.Cell)

    def test_cancer_setup(self):
        tissue = cellsim.Tissue(3, 3, cellsim.Cancer)
        tissue[1][1].alive = True
        self.assertEqual(str(tissue[0][0]), '.')
        self.assertEqual(str(tissue[1][1]), 'X')

    def test_seed_file_empty(self):
        tissue = cellsim.Tissue(0, 0)
        tissue.seed_from_file('empty_file.txt', cellsim.Cancer)
        self.assertEqual(str(tissue), """""")

    def test_seed_file_single_row(self):
        tissue = cellsim.Tissue(0, 0)
        tissue.seed_from_file('single_row.txt', cellsim.Cell)
        self.assertEqual(str(tissue), """O..O..OOO.""")

    def test_seed_file_single_col(self):
        tissue = cellsim.Tissue(0, 0)
        tissue.seed_from_file('single_column.txt', cellsim.Cancer)
        self.assertEqual(str(tissue), """X\n.\nX\n.\n.\n.\nX""")

    def test_random_file(self):
        tissue = cellsim.Tissue(0, 0)
        tissue.seed_from_file('sample_matrix.txt', cellsim.Cell)
        self.assertEqual(str(tissue), """O..OOO..OO.O.OO.O..OO..OOOOOOOOOOOOO...O
..OO...O..O.....OO.OO...OO...OOOO...OO..
...O...OO..O.......OO..O.OOO...OOOO.....
O..OOO.OO.OOO.OO.OOOOOOOO..O..OOO.O...O.
..O.O.O.OO..O.O..OOO.O...O....OOO.OOO.OO
O..OOO..OO...O..O.O.OO.O...OOO....O.OOO.
..O..O.OOO...OO..O.OO.OO.OOOO.O.O..OOOO.
OO.O.OOO...OO.....O.OOOO.O...OOOO..OO...
OOOO.OO.O.O.O..O.O...OO..O.O.OO......OOO
..OO.....OOOOO.O.OOOOO.OO.OO...O..OOOOO.""")

    def test_seed_matrix_empty(self):
        input_matrix = [[]]
        tissue = cellsim.Tissue(0, 0)
        tissue.seed_from_matrix(input_matrix)
        self.assertEqual(str(tissue), '')

    def test_getter_setter_easy(self):
        tissue = cellsim.Tissue(6,3,cellsim.Cell)
        tissue[2][0] = cellsim.Cell(True)
        tissue[2][1] = cellsim.Cell(False)
        tissue[2][2] = cellsim.Cell(True)
        self.assertEqual(str(tissue[2][0]), 'O')
        tissue[4] = [cellsim.Cell(True), cellsim.Cell(True),cellsim.Cell(True)]
        self.assertEqual(tissue[4][1].alive, True)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TissueTests('test_str_easy'))
    suite.addTest(TissueTests('test_str_zero_matrix'))
    suite.addTest(TissueTests('test_seed_file_empty'))
    return suite


def main():
    runner = unittest.TextTestRunner(verbosity=2, descriptions=True)
    results = runner.run(suite())


if __name__ == '__main__':
    unittest.main()
