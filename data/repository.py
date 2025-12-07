from typing import TextIO

def open_resource_file(file_path: str) -> TextIO:
    '''Opens a file handle (TextIO) for reading from the specified path.'''
    return open(file_path, "r")

def send_questions(file_path: str) -> TextIO:
    '''Opens a file handle; currently redundant but reserved for output functionality.'''
    return open(file_path, "r")