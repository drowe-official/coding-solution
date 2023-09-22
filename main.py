from enum import Enum
## Assumption: Rovers can visit and end their journey on the same coordinates, without interfering with each other


# The robot moves 1 square based on the direction they're facing, so we just track these transformation
# changes for each direction
class Transformations(Enum):
    N = (0, 1)
    E = (1, 0)
    S = (0, -1)
    W = (-1, 0)

    def rotate_clockwise(self):
        movements = list(Transformations)
        current_val_index = movements.index(self)
        return movements[(current_val_index + 1) % 4]

    def rotate_anticlockwise(self):
        movements = list(Transformations)
        current_val_index = movements.index(self)
        return movements[(current_val_index - 1) % 4]


class WallE:
    def __init__(self, x, y, heading):
        self.coords = (int(x), int(y))
        self.heading = heading

    def move(self):
        self.coords = (self.coords[0] + self.heading.value[0], self.coords[1] + self.heading.value[1])

    def rotate(self, direction):
        if direction == "left":
            self.heading = self.heading.rotate_anticlockwise()
        else:
            self.heading = self.heading.rotate_clockwise()


def main():
    with open("input.txt") as f:
        # No need for max parameters- the rover instructions are assumed to all be valid
        max_x, max_y = f.readline().split(" ")

        while robot_info := f.readline().strip():
            robot_x, robot_y, robot_heading = robot_info.strip().split(" ")
            robot = WallE(robot_x, robot_y, Transformations[robot_heading])

            instructions = f.readline().strip().split(" ")
            for instruction in instructions:
                if instruction == "M":
                    robot.move()
                elif instruction == "L":
                    robot.rotate("left")
                else:
                    robot.rotate("right")
            print(robot.coords[0], robot.coords[1], robot.heading.name)


main()
