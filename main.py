import sys
import os
from stats import get_book_text, count_word, count_char, output


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    text_cont = get_book_text(file_path)
    word_count = count_word(text_cont)
    
    char_dic = count_char(text_cont)
    char_dic = dict(sorted(char_dic.items(), key=lambda item: item[1], reverse=True))

    output(word_count,char_dic,file_path)

if __name__ == "__main__":
    main()