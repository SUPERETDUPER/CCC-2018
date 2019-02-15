class Script:
    piecesByEndingDigit = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    pairsOfEndingDigits = {
        0: [(0, 0), (1, 9), (2, 8), (3, 7), (4, 6), (5, 5)],
        1: [(0, 1), (2, 9), (3, 8), (4, 7), (5, 6)],
        2: [(0, 2), (1, 1), (3, 9), (4, 8), (5, 7), (6, 6)],
        3: [(1, 2), (0, 3), (4, 9), (5, 8), (6, 7)],
        4: [(2, 2), (1, 3), (0, 4), (5, 9), (6, 8), (7, 7)],
        5: [(2, 3), (1, 4), (0, 5), (6, 9), (7, 8)],
        6: [(3, 3), (2, 4), (1, 5), (0, 6), (7, 9), (8, 8)],
        7: [(3, 4), (2, 5), (1, 6), (0, 7), (8, 9)],
        8: [(4, 4), (3, 5), (2, 6), (1, 7), (0, 8), (9, 9)],
        9: [(4, 5), (3, 6), (2, 7), (1, 8), (0, 9)],
    }

    def run(self):
        n = int(input())

        pieces = sorted(map(int, input().split(sep=" ")))

        list(map(self.sort_by_last_number, pieces))

        fence_lengths = {}  # Length of fence : number of such fences

        smallest_height = pieces[0] + pieces[1]
        largest_height = pieces[-1] + pieces[-2]

        for height in range(smallest_height, largest_height + 1):
            number_of_boards = 0

            for (first_ending_digit, second_ending_digit) in self.pairsOfEndingDigits[height % 10]:
                len_of_first_ending_digits = len(self.piecesByEndingDigit[first_ending_digit])
                len_of_second_ending_digit = len(self.piecesByEndingDigit[second_ending_digit])

                if len_of_first_ending_digits == 0 or len_of_second_ending_digit == 0:
                    continue

                reverse_index = len_of_second_ending_digit - 1

                for firstIndex in range(len_of_first_ending_digits):

                    if first_ending_digit == second_ending_digit:
                        if firstIndex >= reverse_index:
                            break

                    first_piece = self.piecesByEndingDigit[first_ending_digit][firstIndex]

                    while True:
                        if reverse_index < 0:
                            break

                        second_piece = self.piecesByEndingDigit[second_ending_digit][reverse_index]

                        if second_piece < first_piece:
                            break

                        current_height = first_piece + second_piece

                        if current_height > height:
                            reverse_index -= 1
                        elif current_height < height:
                            break
                        elif current_height == height:
                            # print(currentHeight)
                            # print(index)
                            # print(reverseIndex)
                            # print()
                            number_of_boards += 1
                            reverse_index -= 1
                            break

                    if second_piece < first_piece or reverse_index < 0:
                        break

            if number_of_boards > 0:
                # print(height)
                # print(number_of_boards)
                # print()
                if number_of_boards in fence_lengths:
                    fence_lengths[number_of_boards] += 1
                else:
                    fence_lengths[number_of_boards] = 1

        # print(fence_lengths)

        longest = sorted(fence_lengths.keys(), reverse=True)[0]

        print(str(longest) + " " + str(fence_lengths[longest]))

    def sort_by_last_number(self, value):
        self.piecesByEndingDigit[value % 10].append(value)


def main():
    Script().run()


if __name__ == "__main__":
    main()
