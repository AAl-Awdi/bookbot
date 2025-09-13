from stats import *
import sys




def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def print_sorted(dict_list):
    for pair in dict_list:
        print(f"{pair["char"]}: {pair["num"]}")

def main(path):
    book_text = get_book_text(path)
    frq = freaquency(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    print_sorted(sort_dict(frq))
    print("============= END ===============")

# ----------------------------------------------------------------------
# Entry‑point handling – this is where we use sys.argv
# ----------------------------------------------------------------------
if __name__ == "__main__":
    # sys.argv[0] is the script name, sys.argv[1] should be the path.
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)          # exit with a non‑zero status to signal error
    # If we get here we have exactly one user‑supplied argument.
    book_path = sys.argv[1]
    main(book_path)