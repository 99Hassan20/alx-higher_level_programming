#!/usr/bin/python3
"""module to write a file"""


def write_file(filename="", text=""):
    """
        write_file writes a string to a text file.
        Args:
            filename (str): name of file.
            text (str): text to be written.
        Returns: number of bytes written.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
