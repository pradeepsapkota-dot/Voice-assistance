import re 
from bs4 import BeautifulSoup
import markdown2



def extract_yt_term(query):
    """Extracts the search term for YouTube from the query."""
    pattern = r'play\s+(.*)\s+on\s+youtube'
    """ Uses regex to find the term between 'play' and 'on youtube' """
    match = re.search(pattern, query, re.IGNORECASE)
    if match:
        return match.group(1)
    

# Remove unwanted words from query

def remove_words(input_string, words_to_remove):
    # Split the input string into words
    words = input_string.split()

    # Remove unwanted words
    filtered_words = []
    for word in words:
        if word.lower() not in words_to_remove:
            filtered_words.append(word)


    # Join the remaining words back into a string
    result_string = ' '.join(filtered_words)

    return result_string

def markdown_to_text(md):
    html = markdown2.markdown(md)
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text().strip()




