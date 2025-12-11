from typing import TextIO

def open_resource_file(file_path: str) -> TextIO:
    '''Opens a file handle (TextIO) for reading from the specified path.'''
    try:
        return open(file_path, "r")
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: the file {file_path} was not found")
    except PermissionError:
        raise PermissionError(f"Error: You don't have permission to read {file_path}")

def send_questions(file_path: str) -> TextIO:
    '''Opens a file handle; currently redundant but reserved for output functionality.'''
    return open(file_path, "r")