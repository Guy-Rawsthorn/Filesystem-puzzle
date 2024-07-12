from typing import List

file_data = []

class FilesystemPuzzle:
    def __init__(self):
        self.directory_tree = {}
        self.directory_sizes = {}

    def start(self):
        file_data = self.read_file('filesystem-puzzle-input.txt')
        output_array = self.command_parse(file_data)
        self.directory_tree_builder(output_array)
        self.directory_size_calulation()
        self.find_directories_max_size_1000()
        self.find_smalled_dir_to_delete_for_update()
        
    def read_file(self, file_path: str) -> List[List[str]]:
        with open(file_path) as input_file:
            for line in input_file.readlines():
                split_line_list = []
                for item in line.strip().split(' '):
                    split_line_list.append(item)
                file_data.append(split_line_list)
        return file_data

    def command_parse(self, file_data: List[List[str]]) -> dict:
        output_array = []
        current_command = None
        current_outputs = None
        for line in file_data:
            if line[0] == "$":
                if current_command is not None:
                    output_array.append({"command": current_command, "output": current_outputs})
                current_command = line[1:]
                current_outputs = None
            else:
                if current_outputs is None:
                    current_outputs = [line]
                else:
                    current_outputs.append(line)
                    
        if current_command is not None:
            output_array.append({"command": current_command, "output": current_outputs})
            
        return output_array

    def directory_tree_builder(self, output_array: List[List[str]]) -> dict:
        path = ""
        
        for item in output_array:
            command = item['command']
            if command[0] == 'cd':
                if command[1] == '..':
                    path = "/".join(path.split("/")[:-1])
                elif command[1] == '/':
                    path = "/home"
                else:
                    path = path + "/" + command[1]
                    self.directory_tree[path] = {}
            else:
                if command[0] == 'ls' and item['output'] is not None:
                    self.directory_tree[path] = item['output']

    def directory_size_calulation(self):
        for key in self.directory_tree:
            if key not in self.directory_sizes:
                self.directory_sizes[key] = 0
            temp_path = key
            while temp_path != "":
                for item in self.directory_tree[key]:
                    if item[0] != "dir":
                            self.directory_sizes[temp_path] += int(item[0])
                temp_path = temp_path[:temp_path.rindex("/")]

    def find_directories_max_size_1000(self):
        value_of_small_size_dirs = 0
        for _, value in self.directory_sizes.items():
            if value < 100000:
                value_of_small_size_dirs += value
        print(f"Total size of all directories whose disk usage is less than 100000 = {value_of_small_size_dirs}")


    def find_smalled_dir_to_delete_for_update(self):      
        size_of_home_dir = self.directory_sizes['/home']
        max_size_of_home_dir = (70000000 - 30000000)
        if (size_of_home_dir > max_size_of_home_dir):
            bytes_to_delete = size_of_home_dir - max_size_of_home_dir
            deletable_directories = {}
            for key, value in self.directory_sizes.items():
                if bytes_to_delete <= value:
                    deletable_directories[key] = value
            smallest_dir_key = min(deletable_directories, key=deletable_directories.get)
            smallest_dir_value = deletable_directories[smallest_dir_key]
            smallest_directory_key_value = (smallest_dir_key, smallest_dir_value)
            print(f"Please delete - {smallest_directory_key_value} - in order to update.")
        else:
            print(f"File system has enough space for update - Free space: {70000000 - size_of_home_dir} ")

def main():
    filesystem_puzzle = FilesystemPuzzle()
    filesystem_puzzle.start()

if __name__ == "__main__":
    main()
