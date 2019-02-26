# DOESN'T PASS TESTS

class Solver:
    def __init__(self):
        (self.numberOfAttractions, self.attractionsPerDay) = tuple(map(int, input().split(" ")))
        self.values = list(map(int, input().split(" ")))
        self.numberOfDays = int(self.numberOfAttractions / self.attractionsPerDay) + 1  # +1 because truncated

    def solve(self):
        wiggle_room = self.numberOfDays * self.attractionsPerDay - self.numberOfAttractions
        print(self.recursive(1, wiggle_room, 0))

    def recursive(self, day_number, wiggle_room, index):
        if day_number == self.numberOfDays:
            return max(self.values[index:])

        height_score = 0
        for numberOfAttractionsInDay in range(self.attractionsPerDay - wiggle_room, self.attractionsPerDay + 1):
            height_score_for_number_of_attractions_in_day = \
                max(self.values[index: index + numberOfAttractionsInDay]) + \
                self.recursive(
                    day_number + 1,
                    wiggle_room - self.attractionsPerDay + numberOfAttractionsInDay,
                    index + numberOfAttractionsInDay
                )

            height_score = max(height_score, height_score_for_number_of_attractions_in_day)

        return height_score


def main():
    Solver().solve()


if __name__ == "__main__":
    main()
