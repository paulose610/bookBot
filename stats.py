def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def count_char(text_cont):
    char_dic = {}
    for c in text_cont:
        cur_c = c.lower()
        if cur_c.isalpha():
            if cur_c in char_dic:
                char_dic[cur_c]+=1
            else:
                char_dic[cur_c]=1
    
    return char_dic

def count_word(text_cont):
    return len(text_cont.split())


def output(wc,char_dic,file_path):
    print(f"""
============ BOOKBOT ============
          
Analyzing book found at {file_path}...

----------- Word Count ----------
Found {wc} total words

--------- Character Count -------
    """)
    
    for key,val in char_dic.items():
        print(f"{key}: {val}\n")
    print("============= END ===============")