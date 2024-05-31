import os

def list_files_and_directories(root_dir):
    file_structure = {}
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            dir_full_path = os.path.join(dirpath, dirname)
            file_structure[dir_full_path] = []
        for filename in filenames:
            file_full_path = os.path.join(dirpath, filename)
            dir_only = os.path.dirname(file_full_path)
            if dir_only not in file_structure:
                file_structure[dir_only] = []
            file_structure[dir_only].append(filename)
    return file_structure

def save_to_file(file_structure, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for dirpath, files in file_structure.items():
            f.write(f'Directory: {dirpath}\n')
            for file in files:
                f.write(f'    {file}\n')
            f.write('\n')

if __name__ == '__main__':
    root_directory = r'C:\Users\luccas.faustino\Desktop'
    output_file = 'file_structure.txt'
    file_structure = list_files_and_directories(root_directory)
    save_to_file(file_structure, output_file)
    print(f'Report saved to {output_file}')