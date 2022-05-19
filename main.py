from WordSearch import WordSearch
import time


def LoadWordList(FileName)->list:
    with open(FileName, 'r') as f:
        wordList = f.read().splitlines()

    wordList = list(set(wordList))
    return wordList

def read_as_one_string(file)->str:
    with open(file, 'r') as f:
        file_content = " ".join(f.readlines())
        #remove all whitespace
        file_content = "".join(file_content.split())
        #remove all newlines
        file_content = file_content.replace("\n", "")
    return file_content


def main():
    # gridString = read_as_one_string("wordlist10k.txt")
    ws=WordSearch(read_as_one_string("C:/Users/yahie/PycharmProjects/Pexip_homework/resources/10kword.txt"))
    words_to_find = LoadWordList("C:/Users/yahie/PycharmProjects/Pexip_homework/resources/1millionwords.txt")

    for word in words_to_find:
        if ws.is_present(word):
            print("found {}".format(word))


if __name__ == "__main__":
    start_time = time.time()

    main()

    print("--- %s seconds ---" % (time.time() - start_time))