#This script loops through folders (1-60 here) to go into each log 
# file and check if it has completed

import os

def contains_job_finished(lines):
    for line in reversed(lines):
        if 'Normal termination' in line:
            return True
    return False

def check_log_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if lines:
            if not contains_job_finished(lines[-5:]):  # Check the last 5 lines, you can adjust this number
                print("Warning: " + file_path + " does not contain 'Job finished' in the last few lines.")
        else:
            print(file_path + " is empty.")

for folder_num in range(1, 61):
    folder_path = str(folder_num)

    # Check if the folder exists
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        log_file_path = os.path.join(folder_path, 'es.log')

        # Check if the log file exists
        if os.path.exists(log_file_path) and os.path.isfile(log_file_path):
            check_log_file(log_file_path)
        else:
            print(log_file_path + " not found.")
    else:
        print(folder_path + " not found or not a directory.")

