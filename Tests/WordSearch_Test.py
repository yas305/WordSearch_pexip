import unittest
import WordSearch
from main import LoadWordList, read_as_one_string

class MyTestCase(unittest.TestCase):



    def test_is_pressent(self):
        ws=WordSearch.WordSearch(read_as_one_string("C:/Users/yahie/PycharmProjects/Pexip_homework/resources/5x5grid.txt"))

        self.assertEqual(ws.is_present("pexip"), True)
        self.assertEqual(ws.is_present("apple"), True)
        self.assertEqual(ws.is_present("hello"), True)
        self.assertEqual(ws.is_present("world"), True)
        self.assertEqual(ws.is_present(None), False)

    def test_is_present_in_row(self):
        ws=WordSearch.WordSearch(read_as_one_string("C:/Users/yahie/PycharmProjects/Pexip_homework/resources/5x5grid.txt"))
        self.assertEqual(ws.is_present("pexip"), True)
        self.assertEqual(ws.is_present("Apple"), False)
        self.assertEqual(ws.is_present(""), False)
        self.assertEqual(ws.is_present(" "), False)
        self.assertEqual(ws.is_present("\n"), False)

    def test_medium_grid(self):
        ws= WordSearch.WordSearch(read_as_one_string("C:/Users/yahie/PycharmProjects/Pexip_homework/resources/26x26.txt"))
        self.assertEqual(ws.is_present("irjpostwonaddscogjsrxrqdia"), False)
        self.assertEqual(ws.is_present("irjpostwonaddscogjsrxrqd"), True)
        self.assertEqual(ws.is_present("rjpostwonaddscogjsrxrqdi"), True)
        self.assertEqual(ws.is_present("postwonaddscogjsrxrqdia"), True)
        self.assertEqual(ws.is_present("hello\n"), False)
        self.assertEqual(ws.is_present("hello"), True)


if __name__ == '__main__':
    unittest.main()
