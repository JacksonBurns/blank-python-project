import re
import fileinput

gh_uname = 'test gh_uname'  # input("GitHub username: ")
usr_name = 'test usr_name'  # input("Your name: ")
prj_name = 'test prj_name'  # input("Name of the project: ")
pypi_name = 'test pypi_name'  # input("Name for the PyPI package: ")
slogan = 'test slogan'  # input("Slogan for your project: ")

project_files = [
    'setup.py',
    'README.md',
    'test/test_blankpythonproject.py',
    'blankpythonproject/__init__.py',
    'blankpythonproject/blankpythonproject.py',
    '.github/workflows/run_unix_tests.yml',
]

for filename in project_files:
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            if re.search("blankpythonproject", line):
                print(line.replace('blankpythonproject', prj_name), end='')
            elif re.search("JacksonBurns", line):
                print(line.replace('JacksonBurns', gh_uname), end='')
            elif re.search("Jackson Burns", line):
                print(line.replace('Jackson Burns', usr_name), end='')
            elif re.search("blpyproj", line):
                print(line.replace('blpyproj', pypi_name), end='')
            else:
                print(line, end='')

# rename image

# rename test_blankpythonproject.py

# rename example notebook

# rename source directory

# rename main file
