#!/usr/bin/python3
"""Search and update module"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, 'r', encoding='utf-8') as file:
        list_of_lines = []
        while True:
            line = file.readline()
            if line == "":
                break
            list_of_lines.append(line)
            if search_string in line:
                list_of_lines.append(new_string)
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(list_of_lines)
