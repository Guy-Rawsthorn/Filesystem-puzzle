# test_math_operations.py
import unittest
import filesystem_puzzle
class TestNoSpaceOnDiskPuzzle(unittest.TestCase):
    
    def setUp(self):
        self.expected_file_data = [['$', 'cd', '/'], ['$', 'ls'], 
            ['dir', 'dpllhlcv'], ['284723', 'hznrlfhh.tnz'], ['$', 'cd', 'dpllhlcv'],
            ['$', 'ls'], ['11223', 'bplz.rdp'], ['dir', 'gpmlznd']]
        
        self.expected_output_array = [{'command': ['cd', '/'], 'output': None}, 
            {'command': ['ls'], 'output': [['dir', 'dpllhlcv'], ['284723', 'hznrlfhh.tnz']]},
            {'command': ['cd', 'dpllhlcv'], 'output': None}, {'command': ['ls'], 'output': 
            [['11223', 'bplz.rdp'], ['dir', 'gpmlznd']]}]
        
        self.expected_directory_tree = {'/home': [['dir', 'dpllhlcv'], ['284723', 'hznrlfhh.tnz']], 
            '/home/dpllhlcv': [['11223', 'bplz.rdp'], ['dir', 'gpmlznd']]}
        
        self.expected_directory_size = {'/home': 295946, '/home/dpllhlcv': 11223}
        
    def test_read_file(self):
        file_data = filesystem_puzzle.read_file(file_path="test.txt")
        assert file_data == self.expected_file_data

    def test_output_array(self):
        output_array = filesystem_puzzle.command_parse(file_data=self.expected_file_data)
        assert output_array == self.expected_output_array
    
    def test_directory_tree_builder(self):
        filesystem_puzzle.directory_tree_builder(self.expected_output_array)
        assert filesystem_puzzle.directory_tree == self.expected_directory_tree
    
    def test_directory_sizes(self):
        filesystem_puzzle.directory_tree = self.expected_directory_tree
        filesystem_puzzle.directory_size_calulation()
        assert filesystem_puzzle.directory_sizes == self.expected_directory_size


if __name__ == '__main__':
    unittest.main()