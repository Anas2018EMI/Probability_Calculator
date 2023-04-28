import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = []
        for key, value in kwargs.items():
            for rep in range(value):
                self.contents += [key]

    def draw(self, num_balls):
        if num_balls > len(self.contents):
            return self.contents
        else:
            output = []
            for draw in range(num_balls):
                random_index = random.randint(0, len(self.contents)-1)
                output += [self.contents[random_index]]
                self.contents.pop(random_index)

            return output


def experiment(hat: Hat, expected_balls: dict, num_balls_drawn, num_experiments):
    m = 0
    for exp in range(num_experiments):
        # print(f"Experiment n° {exp+1}:")
        hat_copy = copy.deepcopy(hat)
        random_draw = hat_copy.draw(num_balls_drawn)
        # print(random_draw)
        no_duplicates = list(dict.fromkeys(random_draw))
        no_duplicates_dict = {}
        for color in no_duplicates:
            no_duplicates_dict[color] = random_draw.count(color)
        # print(no_duplicates_dict)

        is_valid = []
        for expected_ball in expected_balls:
            try:
                if no_duplicates_dict[expected_ball] >= expected_balls[expected_ball]:
                    is_valid += [True]
                else:
                    is_valid += [False]
            except:
                is_valid += [False]
        print(is_valid)

        if not False in is_valid:
            m += 1
            print(m)
        print()

    return m/num_experiments


# hat = Hat(black=6, red=4, green=3)
# print(hat.contents)
# probability = experiment(hat=hat,
#                          expected_balls={"red": 2, "green": 1},
#                          num_balls_drawn=5,
#                          num_experiments=2500)


hat = Hat(blue=3, red=2, green=6)
print(hat.contents)
probability = experiment(hat=hat, expected_balls={
                         "blue": 2, "green": 1}, num_balls_drawn=4, num_experiments=1000)

#
print(probability)
