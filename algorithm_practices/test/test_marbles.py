import sys
import pytest
from io import StringIO
from marbles import MarblesBoard, gen_matrix, Dir, RedMarbleExit, BlueMarbleExit


@pytest.fixture()
def case2():
    return (("7 7\n"
             "#######\n"
             "#...RB#\n"
             "#.#####\n"
             "#.....#\n"
             "#####.#\n"
             "#O....#\n"
             "#######\n"), 5)


@pytest.fixture
def create_matrix(monkeypatch):

    def fun(test_input: str, width, height):
        monkeypatch.setattr('sys.stdin', StringIO(test_input))
        return MarblesBoard(gen_matrix(width, height))

    return fun


# def test_create(monkeypatch, create_matrix, case2):
#     test_input, _ = case2
#     monkeypatch.setattr('sys.stdin', StringIO(test_input))
#     h, w = map(int, sys.stdin.readline().split())
#     b = MarblesBoard(gen_matrix(w, h))
#     assert b._xy_red == [4, 1]
#     assert b._xy_blue == [5, 1]
#     assert b._xy_hole == (1, 5)
#     assert str(b) == test_input[4:].strip()
#     return b


def test_moveL(create_matrix):
    test_input = ("#####\n"
                  "#.RO#\n"
                  "#..B#\n"
                  "#####\n")
    expected = ("#####\n"
                "#R.O#\n"
                "#B..#\n"
                "#####")
    matrix = create_matrix(test_input, 5, 4)
    matrix.move(Dir.L)
    assert str(matrix) == expected


def test_moveR(create_matrix):
    test_input = ("#####\n"
                  "#.R.#\n"
                  "#O.B#\n"
                  "#####\n")
    expected = ("#####\n"
                "#..R#\n"
                "#O.B#\n"
                "#####")
    matrix = create_matrix(test_input, 5, 4)
    matrix.move(Dir.R)
    assert str(matrix) == expected


def test_moveU(create_matrix):
    test_input = ("#####\n"
                  "#.RO#\n"
                  "#B..#\n"
                  "#####\n")
    expected = ("#####\n"
                "#BRO#\n"
                "#...#\n"
                "#####")
    matrix = create_matrix(test_input, 5, 4)
    matrix.move(Dir.U)
    assert str(matrix) == expected


def test_moveD(create_matrix):
    test_input = ("#####\n"
                  "#.RO#\n"
                  "#..B#\n"
                  "#####\n")
    expected = ("#####\n"
                "#..O#\n"
                "#.RB#\n"
                "#####")
    matrix = create_matrix(test_input, 5, 4)
    matrix.move(Dir.D)
    assert str(matrix) == expected


def test_stuck_by_wall(create_matrix):
    test_input = ("######\n"
                  "#.RO.#\n"
                  "#.#B.#\n"
                  "#....#\n"
                  "######\n")
    expected = ("######\n"
                "#.RO.#\n"
                "#.#..#\n"
                "#..B.#\n"
                "######")
    matrix = create_matrix(test_input, 6, 5)
    matrix.move(Dir.D)
    assert str(matrix) == expected


def test_stuck_by_red(create_matrix):
    test_input = ("########\n"
                  "#.BR#.O#\n"
                  "########\n")
    expected = ("########\n"
                "#.BR#.O#\n"
                "########")
    matrix = create_matrix(test_input, 8, 3)
    matrix.move(Dir.R)
    assert str(matrix) == expected


def test_stuck_by_blue(create_matrix):
    test_input = ("########\n"
                  "#.BR#.O#\n"
                  "########\n")
    expected = ("########\n"
                "#BR.#.O#\n"
                "########")
    matrix = create_matrix(test_input, 8, 3)
    matrix.move(Dir.L)
    assert str(matrix) == expected


def test_red_exit(create_matrix):
    test_input = ("#####\n"
                  "#.RO#\n"
                  "#..B#\n"
                  "#####\n")
    matrix = create_matrix(test_input, 5, 4)
    with pytest.raises(RedMarbleExit):
        matrix.move(Dir.R)


def test_blue_exit(create_matrix):
    test_input = ("#####\n"
                  "#.RO#\n"
                  "#..B#\n"
                  "#####\n")
    matrix = create_matrix(test_input, 5, 4)
    with pytest.raises(BlueMarbleExit):
        matrix.move(Dir.U)


def test_both_exit(create_matrix):
    test_input = ("##########\n"
                  "#.O....RB#\n"
                  "##########\n")
    matrix = create_matrix(test_input, 10, 3)
    with pytest.raises(BlueMarbleExit):
        matrix.move(Dir.L)


def test_both_exit2(create_matrix):
    test_input = ("########\n"
                  "#......#\n"
                  "#.BR.O.#\n"
                  "########\n")
    matrix = create_matrix(test_input, 8, 4)
    with pytest.raises(BlueMarbleExit):
        matrix.move(Dir.R)


def test_search_routes_1(create_matrix):
    test_input = ("#####\n"
                  "#..B#\n"
                  "#.#.#\n"
                  "#RO.#\n"
                  "#####\n")
    matrix = create_matrix(test_input, 5, 5)
    assert len(matrix.search_routes()) == 1


def test_search_routes_2(create_matrix):
    test_input = ("#######\n"
                  "#...RB#\n"
                  "#.#####\n"
                  "#.....#\n"
                  "#####.#\n"
                  "#O....#\n"
                  "#######\n")
    matrix = create_matrix(test_input, 7, 7)
    assert len(matrix.search_routes()) == 5


def test_search_routes_3(create_matrix):
    test_input = ("#######\n"
                  "#..R#B#\n"
                  "#.#####\n"
                  "#.....#\n"
                  "#####.#\n"
                  "#O....#\n"
                  "#######\n")
    matrix = create_matrix(test_input, 7, 7)
    assert len(matrix.search_routes()) == 5


def test_search_routes_4(create_matrix):
    test_input = ("##########\n"
                  "#R#...##B#\n"
                  "#...#.##.#\n"
                  "#####.##.#\n"
                  "#......#.#\n"
                  "#.######.#\n"
                  "#.#....#.#\n"
                  "#.#.#.#..#\n"
                  "#...#.O#.#\n"
                  "##########\n")
    matrix = create_matrix(test_input, 10, 10)
    assert len(matrix.search_routes()) == 0


def test_search_routes_5(create_matrix):
    test_input = ("#######\n"
                  "#R.O.B#\n"
                  "#######\n")
    matrix = create_matrix(test_input, 7, 3)
    assert len(matrix.search_routes()) == 1


def test_search_routes_6(create_matrix):
    test_input = ("##########\n"
                  "#R#...##B#\n"
                  "#...#.##.#\n"
                  "#####.##.#\n"
                  "#......#.#\n"
                  "#.######.#\n"
                  "#.#....#.#\n"
                  "#.#.##...#\n"
                  "#O..#....#\n"
                  "##########\n")
    matrix = create_matrix(test_input, 10, 10)
    assert len(matrix.search_routes()) == 7


def test_search_routes_7(create_matrix):
    test_input = ("##########\n"
                  "#.O....RB#\n"
                  "##########\n")
    matrix = create_matrix(test_input, 10, 3)
    print(matrix)
    assert len(matrix.search_routes()) == 0


def test_search_routes_8(create_matrix):
    test_input = ("#######\n"
                  "#R....#\n"
                  "#.....#\n"
                  "#..O..#\n"
                  "#..B..#\n"
                  "#######")
    matrix = create_matrix(test_input, 7, 6)
    assert len(matrix.search_routes()) == 3


def test_search_routes_8_1(create_matrix):
    test_input = ("#######\n"
                  "#R....#\n"
                  "#.....#\n"
                  "#..O..#\n"
                  "#..B..#\n"
                  "#######")
    expected = ("#######\n"
                "#R....#\n"
                "#.....#\n"
                "#..O..#\n"
                "#B....#\n"
                "#######")
    matrix = create_matrix(test_input, 7, 6)
    matrix.move(Dir.L)
    assert str(matrix) == expected


def test_search_routes_8_2(create_matrix):
    test_input = ("#######\n"
                  "#R....#\n"
                  "#.....#\n"
                  "#..O..#\n"
                  "#B....#\n"
                  "#######")
    expected = ("#######\n"
                "#.....#\n"
                "#.....#\n"
                "#R.O..#\n"
                "#B....#\n"
                "#######")
    matrix = create_matrix(test_input, 7, 6)
    matrix.move(Dir.D)
    print(str(matrix))
    assert str(matrix) == expected


def test_search_routes_8_3(create_matrix):
    test_input = ("#######\n"
                  "#.....#\n"
                  "#.....#\n"
                  "#R.O..#\n"
                  "#B....#\n"
                  "#######")
    matrix = create_matrix(test_input, 7, 6)
    with pytest.raises(RedMarbleExit):
        matrix.move(Dir.R)


def test_search_routes_9(create_matrix):
    test_input = ("#####\n"
                  "#OBR#\n"
                  "#####\n")
    matrix = create_matrix(test_input, 5, 3)
    assert len(matrix.search_routes()) == 0


def test_search_routes_10(create_matrix):
    test_input = ("#######\n"
                  "#.RB###\n"
                  "#.#.#O#\n"
                  "#.....#\n"
                  "#######\n")
    matrix = create_matrix(test_input, 7, 6)
    assert len(matrix.search_routes()) == 4


# def test_search_routes_11(create_matrix):
#     test_input = ("############# \n"
#                   "#.RB#########\n"
#                   "#.#.........#\n"
#                   "#.#.#######.#\n"
#                   "#.#.#.....#.#\n"
#                   "#.#.#..O#.#.#\n"
#                   "#.#.#####.#.#\n"
#                   "#.#.......#.#\n"
#                   "#.#########.#\n"
#                   "#...........#\n"
#                   "#############")
#     matrix = create_matrix(test_input, 7, 6)
#     assert len(matrix.search_routes()) == 0

# def test_search_routes_12(create_matrix):
#     test_input = ("#######\n"
#                   "#.RB###\n"
#                   "#.#.#O#\n"
#                   "#.....#\n"
#                   "#######\n")
#     matrix = create_matrix(test_input, 5, 7)
#     assert len(matrix.search_routes()) == 4

# def test_search_routes_8(create_matrix):
#     test_input = ("#######\n"
#                   "#R....#\n"
#                   "#.....#\n"
#                   "#..O..#\n"
#                   "#..B..#\n"
#                   "#######")
#     matrix = create_matrix(test_input, 7, 6)
#     assert len(matrix.search_routes()) == 3
