from typing import List
from .repository import open_resource_file

def get_separator_index(content: str) -> int:
    '''Returns the index of the separator character (£) in the content. '''
    return content.index("£")

def extract_question(content: str, index: int) -> str:
    '''Extracts the question text (substring before the separator index).'''
    return content[0:index]

def extract_answer(content: str, index: int) -> str:
    '''Extracts and strips the correct answer (substring after the separator).'''
    return content[index+1:].strip()

def get_question_list(file_path: str) -> list[str]:
    '''Reads the index file (e.g., questions.txt) and returns a list of cleaned question filenames.'''
    questions_list: list[str] = []
    with open_resource_file(file_path) as f:
        for i in f:
            questions_list.append(i.strip())
    return questions_list 

def get_question_content(file_path: str) -> str:
    '''Retrieves the complete raw text content of a single question resource file.'''
    with open_resource_file(file_path) as file:
        content = file.read()
        return content