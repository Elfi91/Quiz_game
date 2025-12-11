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

from requests import get
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

def get_data(URL: str) -> str:
    if URL is None:
        raise ValueError("L'URL non può essere una stringa vuota")
    
    try:
        response = get(URL)

        response.raise_for_status()

        return response.text
    
    except HTTPError:
        raise HTTPError(f"Errore HTTP {response.status_code} su {URL})")
    
    except ConnectionError:
        raise ConnectionError(f"Connection failed for URL: {URL}")

    except Timeout:
        raise Timeout(f"Request timed out for URL:{URL}")

    except RequestException:
        raise RequestException(f"Errore HTTP for URL: {URL}")
