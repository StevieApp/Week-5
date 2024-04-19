# Copyright 2024 Steve Nginyo
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# file_handling_assignment.py

lines_to_write = ['FIRST\n', 'SECOND\n', 'THIRD\n']
lines_to_append = ['FOURTH', 'FIFTH', 'SIXTH']

try:
    # Check if the file exists
    with open('./my_file.txt', 'w') as file:
        file.writelines(lines_to_write)

    # Reading the contents of "my_file.txt" and displaying them on the console
    with open('./my_file.txt', 'r') as file:
        print(file.read())

    # Opening "my_file.txt" in append mode ('a') and appending lines from the array to the existing content
    with open('./my_file.txt', 'a') as file:
        for line in lines_to_append:
            file.write(line + '\n')

except FileNotFoundError:
    print('The file you are trying to access does not exist.')
except PermissionError:
    print('You do not have the necessary permissions to access this file.')
finally:
    print('Execution of the script has completed.')
