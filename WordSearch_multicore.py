import concurrent.futures
from WordSearch import *
from main import LoadWordList, read_as_one_string

def getallsubstring(word_list, MAX_WORD_LENGTH):
    dict = {}

    for word in word_list:
        for i in range(len(word)):
            for x in range(i, len(word) + 1):
                # only add the substring if it is not already in the dictionary and the length is greater than 1 and less than the max word length
                if word[i:x] not in dict and len(word[i:x]) > 1 and len(word[i:x]) <= MAX_WORD_LENGTH:
                    dict[word[i:x]] = True
    return dict



class WordSearch:
    dict = {}
    grid_length = 0
    row_length = 0
    transposed_grid=""
    default_grid_first = []
    transposed_grid_first = []
    MAX_WORD_LENGTH = 24

    def __init__(self, grid):
        regex = "/^[A-Z]+"

        # remove all non alphanumeric characters and whitespace
        grid = grid.replace(regex, "").replace(" ", "")

        while len(grid) % math.sqrt(len(grid)) != 0:
            grid = grid[:-1]

        self.grid = grid
        self.transposed_grid=get_transposed_gridstring(grid, int(math.sqrt(len(grid))))[0]
        self.grid_length = len(grid)
        self.row_length = int(math.sqrt(self.grid_length))
        self.default_grid_first = self.seperate_words(grid)
        self.transposed_grid_first = self.seperate_words(self.transposed_grid)

        self.dict = {}

    def seperate_words(self, word):
        seperated_words = []
        # split the string every row_length characters
        for i in range(0, self.grid_length, self.row_length):
            seperated_words.append(word[i:i + self.row_length])

        return seperated_words


    def is_present(self, word, ):

        if type(self.dict.get(word)) == bool:
            return True
        else:
            return False



def main():
    ws=WordSearch(read_as_one_string("C:/Users/yahie/PycharmProjects/Pexip_homework/resources/10kword.txt"))
    words_to_find = LoadWordList("C:/Users/yahie/PycharmProjects/Pexip_homework/resources/1millionwords.txt")

    with concurrent.futures.ProcessPoolExecutor() as executor:

        f1 = executor.submit(getallsubstring, ws.default_grid_first, ws.MAX_WORD_LENGTH)
        f2 = executor.submit(getallsubstring, ws.transposed_grid_first, ws.MAX_WORD_LENGTH)
        ws.dict.update(f1.result())
        ws.dict.update(f2.result())


    for word in words_to_find:
        if ws.is_present(word):
            print("found {}".format(word))


if __name__ == '__main__':
    start_time = time.time()

    main()

    print("--- %s seconds ---" % (time.time() - start_time))
