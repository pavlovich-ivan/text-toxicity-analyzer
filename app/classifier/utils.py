import re
import contractions
import nltk
from nltk.corpus import stopwords


nltk.download('stopwords')

stop_words = set(stopwords.words("english"))

def convert_to_lower(text: str) -> str:
  return text.lower()

def remove_links(text: str) -> str:
  text = re.sub(r"http\S+", "", text)
  return text

def remove_spaces(text: str) -> str:
  return " ".join(text.split())

def fix_contractions(text: str) -> str:
  try:
    return contractions.fix(text)
  except:
    print(text)
    return text

def remove_symbols_and_digits(text: str) -> str:
  text = re.sub(r"[^\w\s]|[\d]", "", text)
  return text

def remove_stopwords(text: str) -> str:
  filtered_list_text = [word for word in text.split() if word not in stop_words]
  return " ".join(filtered_list_text)

def clear_text(text: str) -> str:
  text = convert_to_lower(text)
  text = remove_links(text)
  text = fix_contractions(text)
  text = remove_symbols_and_digits(text)
  text = remove_stopwords(text)
  text = remove_spaces(text)
  return text

