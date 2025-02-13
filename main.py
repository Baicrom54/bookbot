def main():
    with open("books/frankstein.txt") as f:
        content_file=f.read()
    n_words=count_words(content_file)
    char_num=count_char(content_file)
    print("--- Begin report of books/frankenstein.txt ---\n")
    print(f"{n_words} was found in the document\n")
    for key in char_num:
        if key.isalpha():
            print(f"The '{key}' was found {char_num[key]} times")


def count_words(string):
    return len(string.split())

def count_char(string):
    char_list=list(string)
    char_set=set(char_list)
    char_dict= {}
    for i in range(0,len(char_list)):
        if char_list[i].lower() not in char_dict:
            char_dict[f"{char_list[i].lower()}"]=1
        else:
            char_dict[f"{char_list[i].lower()}"]+=1
    return char_dict


main()
   