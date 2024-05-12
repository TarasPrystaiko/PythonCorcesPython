import os

def combine_files(source_directory, output_file):
    with open(output_file, 'w') as combined_file:
        for root, _, files in os.walk(source_directory):
            for file_name in files:
                if file_name.endswith('.txt'):
                    file_path = os.path.join(root, file_name)
                    if os.path.getsize(file_path) <= 120:
                        with open(file_path, 'r') as file:
                            content = file.read()
                            combined_file.write(f"{file_name}: {content}\n")

# Example usage:
source_directory = '/path/to/source_directory'
output_file = 'combined_files.txt'
combine_files(source_directory, output_file)
