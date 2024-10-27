folder_name = "exopt"

# Reading content from optim.xyz
optim_file_name = "optim.xyz"
optim_file_path = f"{folder_name}/{optim_file_name}"

# Read the content of the optim.xyz file
with open(optim_file_path, 'r') as optim_file:
    optim_content = optim_file.read()
    last_frame_index = optim_content.rfind('frame')

    if last_frame_index != -1:
        # Find the index of the next newline character after 'frame'
        next_newline_index = optim_content.find('\n', last_frame_index)

        # Check if a newline character is found
        if next_newline_index != -1:
            # Extract the content starting from the line after 'frame'
            extracted_lines = optim_content[next_newline_index + 1:].split('\n')[:28]
        else:
            print("'frame' found, but newline character not found after it.")
    else:
        print("'frame' not found in the file.")

# Reading content from gs.com
gscom_file_name = "es.com"
gscom_file_path = f"{gscom_file_name}"

# Read the content of the gs.com file
with open(gscom_file_path, 'r') as gscom_file:
    gscom_content = gscom_file.readlines()

# Find the line containing 'freq=(savenm,hpmodes)'
freq_line_index = -1
for i, line in enumerate(gscom_content):
    if 'freq=(savenm,hpmodes)' in line:
        freq_line_index = i
        break

# Check if the line is found
if freq_line_index != -1:
    # Replace lines in gs.com with the extracted lines from optim.xyz
    gscom_content[freq_line_index + 5: freq_line_index + 33] = extracted_lines

    # Save the modified content back to gs.com
    with open(gscom_file_path, 'w') as gscom_file:
        for line in gscom_content:
            gscom_file.write(line.strip() + '\n')  # Ensure each line ends with a newline character

    print("Changes saved to es.com.")
else:
    print("'freq=(savenm,hpmodes)' not found in the gs.com file.")

