from stats import word_count, each_character_count,sort_list
import sys
def get_book_text(workspace):
    with open (workspace) as f:
         contents = f.read()
    return contents
def main():
     if len (sys.argv) < 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)

     path = sys.argv[1]
     book = get_book_text(path )
     num_count = word_count(book)
     print(book)
     character_count = each_character_count(book)
     print(f" Found {num_count} total words")
 
     listed = sort_list(character_count)
     for item in listed:
          ch = item["char"]
          num = item["num"]
          
          print(f"{ch}: {num}")






main()

