# test_math_operations.py
import unittest
from filesystem_puzzle import FilesystemPuzzle

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
        
        self.filesystemPuzzle = FilesystemPuzzle()
        
    def test_read_file(self):
        file_data = self.filesystemPuzzle.read_file(file_path="test.txt")
        assert file_data == self.expected_file_data

    def test_output_array(self):
        output_array = self.filesystemPuzzle.command_parse(file_data=self.expected_file_data)
        assert output_array == self.expected_output_array
    
    def test_directory_tree_builder(self):
        self.filesystemPuzzle.directory_tree_builder(self.expected_output_array)
        assert self.filesystemPuzzle.directory_tree == self.expected_directory_tree
    
    def test_directory_sizes(self):
        self.filesystemPuzzle.directory_tree = self.expected_directory_tree
        self.filesystemPuzzle.directory_size_calulation()
        assert self.filesystemPuzzle.directory_sizes == self.expected_directory_size


if __name__ == '__main__':
    unittest.main()