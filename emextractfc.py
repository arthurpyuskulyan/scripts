import os
import glob

def extract_rest_of_file(file_name, start_string, output_file):
    found_start = False
    lines_to_skip = 2
    result = []

    with open(file_name, 'r') as file:
        for line in file:
            if lines_to_skip <= 0:
                result.append(line.strip())

            if start_string in line:
                found_start = True
                lines_to_skip = 2

            if found_start:
                lines_to_skip -= 1

    with open(output_file, 'w') as output:
        output.write('\n'.join(result))

    print("Extraction from {} saved to {}".format(file_name, output_file))


start_string = 'Intensity:'     # Replace with your start string
num_files = 100  # Number of files to process

for i in range(1, 2):
    file_name = 'emvibronic.log'
    output_file = 'em.txt'.format(i)
    extract_rest_of_file(file_name, start_string, output_file)

for i in range(1, 2):
    file_name = 'em.txt'.format(i)
    if os.path.isfile(file_name):
        with open(file_name, 'r+') as file:
            content = file.read()
            modified_content = content.replace('D', 'E')
            file.seek(0)
            file.write(modified_content)
            file.truncate()

for i in range(1, 2):
    file_name = 'em.txt'.format(i)
    file_paths = glob.glob(file_name)

    if file_paths:
        with open(file_paths[0], 'r') as file:
            lines = file.readlines()

        end_line = len(lines)  # Initialize end_line to the length of lines
        for idx, line in enumerate(lines):
            if 'Electric dipole moment' in line:
                end_line = idx
                break

        extracted_lines = lines[:max(end_line - 5, 0)]
        extracted_content = ''.join(extracted_lines)

        output_file = 'em.txt'.format(i)  # New file name for each file
        with open(output_file, 'w') as output:
            output.write(extracted_content)

        print("Extraction from {} saved to {}".format(file_name, output_file))

