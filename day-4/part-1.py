#!/bin/python3
import re


class BingoBoard:
    def __init__(self, grid) -> None:
        self.grid = grid
        self.marks = []
        self.last_draw = None
        for row in grid:
            columns = []
            for _ in row:
                columns.append(0)
            self.marks.append(columns)

    def draw(self, num):
        self.last_draw = num
        for i, row in enumerate(self.grid):
            for j, column in enumerate(row):
                if column == num:
                    self.marks[i][j] = 1

    def calculate_score(self):
        unmarked_total = 0
        for i, row in enumerate(self.grid):
            for j, column in enumerate(row):
                if self.marks[i][j] == 0:
                    unmarked_total += int(column)

        return unmarked_total * int(self.last_draw)

    def check_win(self):
        row_win = False
        column_win = False
        diagonal_win = False

        column_totals = [0] * 5

        for row in self.marks:
            row_total = 0
            for j, column in enumerate(row):
                row_total += column
                column_totals[j] += column
            if row_total >= 5:
                row_win = True

        for column_total in column_totals:
            if column_total >= 5:
                column_win = True

        if diagonal_win or column_win or row_win:
            return True
        return False

    def __str__(self) -> str:
        board_str = ""
        for row in self.grid:
            row_str = ""
            for column in row:
                row_str += column + " "
            board_str += row_str + "\n"

        for row in self.marks:
            row_str = ""
            for column in row:
                row_str += str(column) + " "
            board_str += row_str + "\n"

        return board_str


def build_boards_from_file(filename):
    with open(filename) as input_file:
        bingo_draws = []
        boards = []
        current_board = []
        board_lines = 0
        for line in input_file:
            if len(bingo_draws) == 0:
                bingo_draws = line.replace("\n", "").split(",")
            elif line == "\n":
                pass
            else:
                line = re.sub("\s+", ",", line)
                line = line.replace("\n", "").split(",")
                if line[0] == "":
                    line.pop(0)
                if line[len(line) - 1] == "":
                    line.pop(len(line) - 1)

                current_board.append(line)
                board_lines += 1
                if board_lines == 5:
                    boards.append(BingoBoard(current_board))
                    current_board = []
                    board_lines = 0
    return bingo_draws, boards


def main():
    bingo_draws, boards = build_boards_from_file("input")

    score = None
    for draw in bingo_draws:
        if score == None:
            for board in boards:
                board.draw(draw)
                if board.check_win():
                    score = board.calculate_score()
    print(score)


if __name__ == "__main__":
    main()
