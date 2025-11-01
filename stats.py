def word_count(book):
      count = book.split()
      return len(count)


def each_character_count(so):

      letter  = {}
      for ch in so:

            lowered = ch.lower()
            if lowered not in letter:
             letter[lowered] = 1
            else:
              letter[lowered] += 1
      return letter
def sort_list(so):    
    def sort_on(item):
        return item["num"]
    dic_list = []
    
    for key, value in so.items():
            entry = {"char": key, "num": value}
            dic_list.append(entry)
    sorted_list = dic_list.sort(key=sort_on, reverse = True)
    return dic_list
             





