from typing import List

file_data = []
directory_tree = {}
directory_sizes = {}

def main():
    file_data = read_file('filesystem-puzzle-input.txt')
    output_array = command_parse(file_data)
    directory_tree_builder(output_array)
    directory_size_calulation()
    find_directories_max_size_1000()
    
def read_file(file_path: str) -> List[List[str]]:
    with open(file_path) as input_file:
        for line in input_file.readlines():
            split_line_list = []
            for item in line.strip().split(' '):
                split_line_list.append(item)
            file_data.append(split_line_list)
    return file_data

def command_parse(file_data: List[List[str]]) -> dict:
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

def directory_tree_builder(output_array: List[List[str]]) -> dict:
    path = ""
    global directory_tree
    
    for item in output_array:
        command = item['command']
        if command[0] == 'cd':
            if command[1] == '..':
                path = "/".join(path.split("/")[:-1])
            elif command[1] == '/':
                path = "/home"
            else:
                path = path + "/" + command[1]
                directory_tree[path] = {}
        else:
            if command[0] == 'ls' and item['output'] is not None:
                directory_tree[path] = item['output']

def directory_size_calulation():
    global directory_sizes
    global directory_tree
        
    for key in directory_tree:
        if key not in directory_sizes:
            directory_sizes[key] = 0
        temp_path = key
        while temp_path != "":
            for item in directory_tree[key]:
                if item[0] != "dir":
                        directory_sizes[temp_path] += int(item[0])
            temp_path = temp_path[:temp_path.rindex("/")]

def find_directories_max_size_1000():
    value_of_small_size_dirs = 0
    for key, value in directory_sizes.items():
        if value < 100000:
            value_of_small_size_dirs += value
    print(f"Total size of all directories whose disk usage is less than 100000 = {value_of_small_size_dirs}")
     

if __name__ == "__main__":
    main()
    
