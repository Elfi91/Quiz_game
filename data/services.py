from typing import List, Dict, Union
from .repository import open_resource_file, get_data

def get_separator_index(content: str) -> int:
    '''Finds the index of the separator character (£) in the question content.'''
    try:
        return content.index("£")
    except ValueError:
        raise ValueError("Invalid format: the £ is missing.")

def extract_question(content: str, index: int) -> str:
    '''Extracts the question text using the separator index.'''
    return content[0:index]

def extract_answer(content: str, index: int) -> str:
    '''Extracts the correct answer string using the separator index and strips whitespace.'''
    return content[index+1:].strip()

def get_question_list(URL: str) -> list[str]:
    '''Reads the index file (questions.txt) and returns a list of individual question filenames.'''
    text = get_data(URL)
    questions_list = text.splitlines()
    return questions_list

def get_question_content(URL: str) -> str:
    '''Retrieves the complete raw text content from a single question file.'''
    content = get_data(URL)
    return content
    
def generate_statistics(final_results: dict[int, dict[str, str | bool]]) -> dict[str, int]:
    '''Calculates and returns the final count of correct and incorrect answers.'''
    statistics: dict[str, int] = {}

    correct_answers: int = 0
    incorrect_answers: int = 0

    for result in final_results.values(): 
        if result["correct_answer"]:
            correct_answers += 1
        else:
            incorrect_answers += 1

    statistics["correct_answers"] = correct_answers
    statistics["incorrect_answers"] = incorrect_answers
    return statistics