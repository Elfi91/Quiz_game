# Importing
from typing import List, Dict, Union
from pathlib import Path
from data.repository import get_data
from requests.exceptions import HTTPError

from data.services import (
    get_question_list,
    get_question_content, 
    get_separator_index, 
    extract_question, 
    extract_answer,
    generate_statistics,
)

from ui.console import (
    show_question,
    show_feedback,
    print_question_indicator,
    collect_user_answer,
    validate_choice,
    get_updated_counter,
    get_current_question_number
)

from data.constants import BASE_URL, LISTA_DOMANDE_URL, BASE_DOMANDA_SINGOLA_URL

print("Welcome to the quiz game")


# --- UTILITY FUNCTIONS  ---
def is_answer_correct(choice: str, correct_answer: str) -> bool:
    '''Checks if the user's input matches the correct answer (case-insensitive).'''
    if choice.upper() == correct_answer.upper():
        return True
    else:
        return False

def generate_feedback(is_correct: bool) -> str:
    '''Returns a success or failure message based on the quiz result.'''
    if is_correct == True:
        return "You nailed it!"
    else:
        return "You didn't get it right."


# --- MAIN EXECUTION LOGIC ---
def main():
    '''Orchestrates the entire quiz flow, including iteration, processing, and final output.'''
    index_url = LISTA_DOMANDE_URL

    try:
        list_of_questions = get_question_list(index_url)
    except HTTPError as e:
        print(f"Critical error: Could not find the question list at {index_url}")
        print("The game cannot start")
        return
    except Exception as e:
        print(f"Unexpected error loading list {e}")
        return
    
    final_results: dict[int, dict] = {}
    question_and_answer: dict[str, str] = {"question" : None, "answer" : None}
    
    current_question_counter: int = 0
    list_length: int = len(list_of_questions)

    while current_question_counter < list_length:
        file_name = list_of_questions[current_question_counter]
        question_url = f"{BASE_DOMANDA_SINGOLA_URL}/{file_name}"

        try:
            content = get_question_content(str(question_url))
            separator_index: int = get_separator_index(content)

            question_and_answer["question"] = extract_question(content, separator_index)
            question_and_answer["answer"] = extract_answer(content, separator_index)

            current_question_number: int = get_current_question_number(current_question_counter)
            print_question_indicator(current_question_number, list_length)
            show_question(question_and_answer["question"])

            user_answer: str = collect_user_answer()

            is_answer_valid: bool = validate_choice(user_answer)

            if is_answer_valid:
                result: dict[str, str | bool] = {}
                is_correct: bool = is_answer_correct(user_answer, question_and_answer["answer"])
                feedback = generate_feedback(is_correct)
                result["question"] = list_of_questions[current_question_counter]
                result["correct_answer"] = is_correct

                final_results[current_question_counter] = result

                show_feedback(feedback)
        
            else: 
                feedback = "Invalid answer. Enter only the response among the listed options."
                show_feedback(feedback)
                continue
                
        except HTTPError:
            print(f"Skipping question {file_name}: Web resource not found (404).")
            current_question_counter += 1
            continue

        except ValueError:
            print(f"Error: Corrupted format in question {file_name} (missing separator. Skip)")
            current_question_counter += 1
            continue

        except Exception as e:
            print(f"An unknown error occurred: {e}")
            break

        if current_question_counter < list_length - 1:
            input_prev_next: str = input("Type 'P' to go to the previous question or any other key to continue: ")
            current_question_counter = get_updated_counter(current_question_counter, input_prev_next)
        else:
            current_question_counter = current_question_counter + 1
        

    if final_results:
        statistics: dict[str, int] = generate_statistics(final_results)
    
        print("*"*30)
        print("Game finished. Here are the results:")
        print("*"*30)

        print(f"Correct answers: {statistics['correct_answers']}")
        print(f"Incorrect answers: {statistics['incorrect_answers']}")   
    else:
        print("Game Over. No questions were answered successfully.")

# Entry point del nostro programma
main()