import os
import sys

try:
    file_and_or_directories = ' '.join(sys.argv[1:])
except IndexError:
    file_and_or_directories = ''
# Start app
os.system(f'open -a "IntelliJ IDEA Community Edition" {file_and_or_directories}')
