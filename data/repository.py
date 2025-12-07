from typing import TextIO

def open_resource_file(file_path: str) -> TextIO:
    '''
    Retrieves an IO object of text type from a specific file.
    '''
    return open(file_path, "r")

def send_questions(file_path: str) -> TextIO:
    '''
    This function seems redundant, but keeping the structure if used elsewhere
    '''
    return open(file_path, "r")