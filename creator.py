import os
from pathlib import Path
import re
from cleaning_utils import replace_arabic_char, clear_stop_char



def cleaner(text: str) -> str:
    """Cleaning every word"""
    processed_text = replace_arabic_char(text)
    processed_text = clear_stop_char(processed_text)
    processed_text = processed_text.replace("\t", " ").replace("\n", " ").strip()
    processed_text = processed_text.replace("\u200c", " ")  # Nim-fasele
    processed_text = re.sub(" +", " ", processed_text)  # space cleaner
    processed_text = processed_text.strip()

    return processed_text


data_path = f'{Path(__file__).parent}/data/'

files_list = os.listdir(data_path)

all_words = []


# Reading the files and cleaning
for file in files_list:
    with open(data_path + file, 'r', encoding="utf-8") as stop_file:
        for line in stop_file:
            cleaned_word = cleaner(line)
            if cleaned_word == "" or cleaned_word == " ":
                continue
            all_words.append(cleaner(line))


# Removing duplicates
all_words = set(all_words)

with open("preprocessed-stops-verbs.dat", "w", encoding="utf-8") as proc_file:
    for item in all_words:
        proc_file.write(item + "\n")

print(f"Total stop words = {len(all_words)}")