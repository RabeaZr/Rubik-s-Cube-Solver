import random


class Cube:
    solution = []

    def __init__(self):
        self.white = ["w", "w", "w", "w", "w", "w", "w", "w", "w"]
        self.green = ["g", "g", "g", "g", "g", "g", "g", "g", "g"]
        self.orange = ["o", "o", "o", "o", "o", "o", "o", "o", "o"]
        self.blue = ["b", "b", "b", "b", "b", "b", "b", "b", "b"]
        self.red = ["r", "r", "r", "r", "r", "r", "r", "r", "r"]
        self.yellow = ["y", "y", "y", "y", "y", "y", "y", "y", "y"]

    def get_solution(self):
        return self.solution

    def print_cube(self):
        print("\n" + "this is your cube : ")
        print("white face : " + str(self.white))
        print("green face : " + str(self.green))
        print("orange face : " + str(self.orange))
        print("blue face : " + str(self.blue))
        print("red face : " + str(self.red))
        print("yellow face : " + str(self.yellow))
        print("\n")

    def print_solution(self, sol):
        sol.remove("T")
        for i in range(len(sol)):
            print(sol[i], end=" ")

    def my_scramble(self):
        self.white = ["o", "y", "o", "y", "r", "g", "r", "r", "w"]
        self.green = ["g", "o", "y", "w", "y", "w", "b", "g", "g"]
        self.orange = ["y", "o", "o", "w", "o", "o", "w", "w", "o"]
        self.blue = ["b", "g", "y", "o", "w", "y", "b", "b", "b"]
        self.red = ["w", "r", "g", "g", "g", "y", "w", "b", "r"]
        self.yellow = ["r", "r", "r", "b", "g", "b", "b", "r", "y"]

    def right_move(self):
        self.white[0], self.white[1], self.white[2], self.green[0], self.green[1], self.green[2], self.yellow[0], \
        self.yellow[1], self.yellow[2], self.blue[4], self.blue[5], self.blue[6] = self.green[0], self.green[1], \
                                                                                   self.green[2], self.yellow[0], \
                                                                                   self.yellow[1], self.yellow[2], \
                                                                                   self.blue[4], self.blue[5], \
                                                                                   self.blue[6], \
                                                                                   self.white[0], self.white[1], \
                                                                                   self.white[2]
        self.red[0], self.red[1], self.red[2], self.red[3], self.red[4], self.red[5], self.red[6], self.red[7] = \
            self.red[6], \
            self.red[7], self.red[0], self.red[1], self.red[2], self.red[3], self.red[4], self.red[5]
        self.solution.append("R")

    def right_prime_move(self):
        self.right_move()
        self.right_move()
        self.right_move()

    def left_move(self):
        self.white[6], self.white[5], self.white[4], self.blue[2], self.blue[1], self.blue[0], self.yellow[6], \
        self.yellow[5], \
        self.yellow[4], self.green[6], self.green[5], self.green[4] = self.blue[2], self.blue[1], self.blue[0], \
                                                                      self.yellow[6], \
                                                                      self.yellow[5], self.yellow[4], self.green[6], \
                                                                      self.green[5], self.green[4], self.white[6], \
                                                                      self.white[5], self.white[4]
        self.orange[0], self.orange[1], self.orange[2], self.orange[3], self.orange[4], self.orange[5], self.orange[6], \
        self.orange[7] = self.orange[6], self.orange[7], self.orange[0], self.orange[1], self.orange[2], self.orange[3], \
                         self.orange[4], self.orange[5]
        self.solution.append("L")

    def left_prime_move(self):
        self.left_move()
        self.left_move()
        self.left_move()

    def up_move(self):
        self.green[0], self.green[7], self.green[6], self.red[0], self.red[7], self.red[6], self.blue[0], self.blue[7], \
        self.blue[6], self.orange[0], self.orange[7], self.orange[6] = self.red[0], self.red[7], self.red[6], self.blue[
            0], \
                                                                       self.blue[7], self.blue[6], self.orange[0], \
                                                                       self.orange[7], self.orange[6], self.green[0], \
                                                                       self.green[7], self.green[6]
        self.white[0], self.white[1], self.white[2], self.white[3], self.white[4], self.white[5], self.white[6], \
        self.white[7] = self.white[6], self.white[7], self.white[0], self.white[1], self.white[2], self.white[3], \
                        self.white[4], self.white[5]
        self.solution.append("U")

    def up_prime_move(self):
        self.up_move()
        self.up_move()
        self.up_move()

    def down_move(self):
        self.green[2], self.green[3], self.green[4], self.orange[2], self.orange[3], self.orange[4], self.blue[2], \
        self.blue[3], \
        self.blue[4], self.red[2], self.red[3], self.red[4] = self.orange[2], self.orange[3], self.orange[4], self.blue[
            2], \
                                                              self.blue[3], self.blue[4], self.red[2], self.red[3], \
                                                              self.red[4], self.green[2], self.green[3], self.green[4]
        self.yellow[0], self.yellow[1], self.yellow[2], self.yellow[3], self.yellow[4], self.yellow[5], self.yellow[6], \
        self.yellow[7] = self.yellow[6], self.yellow[7], self.yellow[0], self.yellow[1], self.yellow[2], self.yellow[3], \
                         self.yellow[4], self.yellow[5]
        self.solution.append("D")

    def down_prime_move(self):
        self.down_move()
        self.down_move()
        self.down_move()

    def front_move(self):
        self.white[2], self.white[3], self.white[4], self.orange[0], self.orange[1], self.orange[2], self.yellow[6], \
        self.yellow[7], self.yellow[0], self.red[4], self.red[5], self.red[6] = self.orange[0], self.orange[1], \
                                                                                self.orange[2], self.yellow[6], \
                                                                                self.yellow[7], self.yellow[0], \
                                                                                self.red[4], self.red[5], self.red[6], \
                                                                                self.white[2], \
                                                                                self.white[3], self.white[4]
        self.green[0], self.green[1], self.green[2], self.green[3], self.green[4], self.green[5], self.green[6], \
        self.green[7] = self.green[6], self.green[7], self.green[0], self.green[1], self.green[2], self.green[3], \
                        self.green[4], self.green[5]
        self.solution.append("F")

    def front_prime_move(self):
        self.front_move()
        self.front_move()
        self.front_move()

    def back_move(self):
        self.white[0], self.white[7], self.white[6], self.red[2], self.red[1], self.red[0], self.yellow[4], self.yellow[
            3], \
        self.yellow[2], self.orange[6], self.orange[5], self.orange[4] = self.red[2], self.red[1], self.red[0], \
                                                                         self.yellow[4], self.yellow[3], self.yellow[2], \
                                                                         self.orange[6], self.orange[5], self.orange[4], \
                                                                         self.white[0], \
                                                                         self.white[7], self.white[6]
        self.blue[0], self.blue[1], self.blue[2], self.blue[3], self.blue[4], self.blue[5], self.blue[6], \
        self.blue[7] = self.blue[6], self.blue[7], self.blue[0], self.blue[1], self.blue[2], self.blue[3], self.blue[4], \
                       self.blue[5]
        self.solution.append("B")

    def back_prime_move(self):
        self.back_move()
        self.back_move()
        self.back_move()

    def random_scramble(self):
        x = scramble_gen()
        x = scramble_replace(x)
        x = valid(x)
        self.solution.append("\n\n" + "Scramble : ")
        for i in x:
            if i[0] == "R":
                if i[1] == "":
                    self.right_move()
                elif i[1] == "'":
                    self.right_prime_move()
                elif i[1] == "2":
                    self.right_move()
                    self.right_move()
            elif i[0] == "L":
                if i[1] == "":
                    self.left_move()
                elif i[1] == "'":
                    self.left_prime_move()
                elif i[1] == "2":
                    self.left_move()
                    self.left_move()
            elif i[0] == "U":
                if i[1] == "":
                    self.up_move()
                elif i[1] == "'":
                    self.up_prime_move()
                elif i[1] == "2":
                    self.up_move()
                    self.up_move()
            elif i[0] == "D":
                if i[1] == "":
                    self.down_move()
                elif i[1] == "'":
                    self.down_prime_move()
                elif i[1] == "2":
                    self.down_move()
                    self.down_move()
            elif i[0] == "F":
                if i[1] == "":
                    self.front_move()
                elif i[1] == "'":
                    self.front_prime_move()
                elif i[1] == "2":
                    self.front_move()
                    self.front_move()
            elif i[0] == "B":
                if i[1] == "":
                    self.back_move()
                elif i[1] == "'":
                    self.back_prime_move()
                elif i[1] == "2":
                    self.back_move()
                    self.back_move()

    def solve_cross(self):

        while self.yellow[1] != "y" or self.yellow[3] != "y" or self.yellow[5] != "y" or self.yellow[7] != "y":

            while self.white[1] == "y" or self.white[3] == "y" or self.white[5] == "y" or self.white[7] == "y":
                if self.white[1] == "y":
                    while self.yellow[1] == "y":
                        self.down_move()
                    self.right_move()
                    self.right_move()
                self.up_move()

            while self.green[1] == "y" or self.green[3] == "y" or self.green[5] == "y" or self.green[7] == "y":
                if self.green[5] == "y":
                    while self.yellow[5] == "y":
                        self.down_move()
                    self.left_move()
                    continue
                while self.yellow[7] == "y":
                    self.down_move()
                self.front_move()

            while self.orange[1] == "y" or self.orange[3] == "y" or self.orange[5] == "y" or self.orange[7] == "y":
                if self.orange[5] == "y":
                    while self.yellow[3] == "y":
                        self.down_move()
                    self.back_move()
                    continue
                while self.yellow[5] == "y":
                    self.down_move()
                self.left_move()

            while self.blue[1] == "y" or self.blue[3] == "y" or self.blue[5] == "y" or self.blue[7] == "y":
                if self.blue[5] == "y":
                    while self.yellow[1] == "y":
                        self.down_move()
                    self.right_move()
                    continue
                while self.yellow[3] == "y":
                    self.down_move()
                self.back_move()

            while self.red[1] == "y" or self.red[3] == "y" or self.red[5] == "y" or self.red[7] == "y":
                if self.red[5] == "y":
                    while self.yellow[7] == "y":
                        self.down_move()
                    self.front_move()
                    continue
                while self.yellow[1] == "y":
                    self.down_move()
                self.right_move()

    def solve_cross_official(self):
        counter = 0
        if self.green[3] == self.green[8]:
            counter += 1
        if self.orange[3] == self.orange[8]:
            counter += 1
        if self.blue[3] == self.blue[8]:
            counter += 1
        if self.red[3] == self.red[8]:
            counter += 1
        while counter != 4:
            while counter < 2:
                counter = 0
                self.down_move()
                if self.green[3] == self.green[8]:
                    counter += 1
                if self.orange[3] == self.orange[8]:
                    counter += 1
                if self.blue[3] == self.blue[8]:
                    counter += 1
                if self.red[3] == self.red[8]:
                    counter += 1
            if counter == 4:
                continue
            if self.green[3] == self.green[8] and self.blue[3] == self.blue[8]:
                self.right_move()
                self.down_move()
                self.down_move()
                self.right_prime_move()
                self.down_move()
                self.down_move()
                self.right_move()
            elif self.red[3] == self.red[8] and self.orange[3] == self.orange[8]:
                self.front_move()
                self.down_move()
                self.down_move()
                self.front_prime_move()
                self.down_move()
                self.down_move()
                self.front_move()
            elif self.orange[3] == self.orange[8] and self.blue[3] == self.blue[8]:
                self.right_move()
                self.down_move()
                self.right_prime_move()
                self.down_prime_move()
                self.right_move()
            elif self.blue[3] == self.blue[8] and self.red[3] == self.red[8]:
                self.front_move()
                self.down_move()
                self.front_prime_move()
                self.down_prime_move()
                self.front_move()
            elif self.red[3] == self.red[8] and self.green[3] == self.green[8]:
                self.left_move()
                self.down_move()
                self.left_prime_move()
                self.down_prime_move()
                self.left_move()
            elif self.green[3] == self.green[8] and self.orange[3] == self.orange[8]:
                self.back_move()
                self.down_move()
                self.back_prime_move()
                self.down_prime_move()
                self.back_move()
            counter = 4
            continue

    def solve_corners(self):
        # solving the corners using the fredrich method
        # try optimizing later
        
        while self.yellow[0] != "y" or self.green[2] != "g" or self.red[4] != "r" or self.green[4] != "g" or \
                self.yellow[6] != "y" or self.orange[2] != "o" or self.yellow[2] != "y" or self.red[2] != "r" or \
                self.blue[4] != "b" or self.yellow[4] != "y" or self.blue[2] != "b" or self.orange[4] != "o":
            while self.white[0] == "y" or self.white[2] == "y" or self.white[4] == "y" or self.white[6] == "y" or \
                    self.green[0] == "y" or self.green[6] == "y" or self.orange[0] == "y" or self.orange[6] == "y" or \
                    self.blue[0] == "y" or self.blue[6] == "y" or self.red[0] == "y" or self.red[6] == "y":
                while self.white[2] != "y" and self.green[0] != "y" and self.red[6] != "y":
                    self.up_move()
                while self.white[2] == "y" or self.green[0] == "y" or self.red[6] == "y":

                    while self.red[6] == "y":
                        if self.green[0] == self.green[3] and self.white[2] == self.red[3]:
                            self.right_move()
                            self.up_move()
                            self.right_prime_move()
                        else:
                            self.down_move()
                    while self.green[3] != self.green[8]:
                        self.down_move()

                    while self.green[0] == "y":
                        if self.red[6] == self.red[3] and self.white[2] == self.green[3]:
                            self.front_prime_move()
                            self.up_prime_move()
                            self.front_move()
                        else:
                            self.down_move()
                    while self.green[3] != self.green[8]:
                        self.down_move()

                    while self.white[2] == "y":
                        if self.red[6] == self.green[3] and self.green[0] == self.red[3]:
                            self.right_move()
                            self.up_move()
                            self.up_move()
                            self.right_prime_move()
                            self.up_prime_move()
                            self.right_move()
                            self.up_move()
                            self.right_prime_move()
                        else:
                            self.down_move()
                    while self.green[3] != self.green[8]:
                        self.down_move()

            if self.yellow[0] != "y" or self.red[4] != "r" or self.green[2] != "g":
                self.right_move()
                self.up_prime_move()
                self.right_prime_move()
                continue
            if self.green[4] != "g" or self.orange[2] != "o" or self.yellow[6] != "y":
                self.left_prime_move()
                self.up_prime_move()
                self.left_move()
                continue
            if self.orange[4] != "o" or self.blue[2] != "b" or self.yellow[4] != "y":
                self.left_move()
                self.up_move()
                self.left_prime_move()
                continue
            if self.blue[4] != "b" or self.red[2] != "r" or self.yellow[2] != "y":
                self.right_prime_move()
                self.up_move()
                self.right_move()
                continue

    def solve_edges(self):
        while self.green[1] != "g" or self.red[5] != "r" or self.green[5] != "g" or self.orange[1] != "o" or \
                self.orange[5] != "o" or self.blue[1] != "b" or self.blue[5] != "b" or self.red[1] != "r":

            while (self.white[1] == "w" or self.red[7] == "w") and (self.white[3] == "w" or self.green[7] == "w") and (
                    self.white[5] == "w" or self.orange[7] == "w") and (self.white[7] == "w" or self.blue[7] == "w"):

                if self.green[1] != "g" or self.red[5] != "r":
                    self.right_move()
                    self.up_prime_move()
                    self.right_prime_move()
                    self.up_prime_move()
                    self.front_prime_move()
                    self.up_move()
                    self.front_move()
                elif self.green[5] != "g" or self.orange[1] != "o":
                    self.left_prime_move()
                    self.up_move()
                    self.left_move()
                    self.up_move()
                    self.front_move()
                    self.up_prime_move()
                    self.front_prime_move()
                elif self.orange[5] != "o" or self.blue[1] != "b":
                    self.left_move()
                    self.up_prime_move()
                    self.left_prime_move()
                    self.up_prime_move()
                    self.back_prime_move()
                    self.up_move()
                    self.back_move()
                elif self.blue[5] != "b" or self.red[1] != "r":
                    self.right_prime_move()
                    self.up_move()
                    self.right_move()
                    self.up_move()
                    self.back_move()
                    self.up_prime_move()
                    self.back_prime_move()

            while self.red[7] != "r" and self.green[7] != "g" and self.orange[7] != "o" and self.blue[7] != "b":
                self.up_move()

            if self.red[7] == "r" and self.white[1] == "g":
                self.up_prime_move()
                self.front_prime_move()
                self.up_move()
                self.front_move()
                self.up_move()
                self.right_move()
                self.up_prime_move()
                self.right_prime_move()
            elif self.red[7] == "r" and self.white[1] == "b":
                self.up_move()
                self.back_move()
                self.up_prime_move()
                self.back_prime_move()
                self.up_prime_move()
                self.right_prime_move()
                self.up_move()
                self.right_move()
            elif self.green[7] == "g" and self.white[3] == "r":
                self.up_move()
                self.right_move()
                self.up_prime_move()
                self.right_prime_move()
                self.up_prime_move()
                self.front_prime_move()
                self.up_move()
                self.front_move()
            elif self.green[7] == "g" and self.white[3] == "o":
                self.up_prime_move()
                self.left_prime_move()
                self.up_move()
                self.left_move()
                self.up_move()
                self.front_move()
                self.up_prime_move()
                self.front_prime_move()
            elif self.orange[7] == "o" and self.white[5] == "g":
                self.up_move()
                self.front_move()
                self.up_prime_move()
                self.front_prime_move()
                self.up_prime_move()
                self.left_prime_move()
                self.up_move()
                self.left_move()
            elif self.orange[7] == "o" and self.white[5] == "b":
                self.up_prime_move()
                self.back_prime_move()
                self.up_move()
                self.back_move()
                self.up_move()
                self.left_move()
                self.up_prime_move()
                self.left_prime_move()
            elif self.blue[7] == "b" and self.white[7] == "o":
                self.up_move()
                self.left_move()
                self.up_prime_move()
                self.left_prime_move()
                self.up_prime_move()
                self.back_prime_move()
                self.up_move()
                self.back_move()
            elif self.blue[7] == "b" and self.white[7] == "r":
                self.up_prime_move()
                self.right_prime_move()
                self.up_move()
                self.right_move()
                self.up_move()
                self.back_move()
                self.up_prime_move()
                self.back_prime_move()
            else:
                self.up_move()

    def solve_OLL(self):

        while self.white[0] != "w" or self.white[1] != "w" or self.white[2] != "w" or self.white[3] != "w" or \
                self.white[4] != "w" or self.white[5] != "w" or self.white[6] != "w" or self.white[7] != "w":

            if self.white[1] == "w" and self.white[3] == "w" and self.white[5] == "w" and self.white[7] == "w":

                if self.red[0] == "w" and self.green[0] == "w" and self.white[4] == "w" and self.blue[0] == "w":
                    self.right_move()
                    self.up_move()
                    self.right_prime_move()
                    self.up_move()
                    self.right_move()
                    self.up_move()
                    self.up_move()
                    self.right_prime_move()
                    continue
                elif self.blue[6] == "w" and self.white[2] == "w" and self.green[6] == "w" and self.orange[6] == "w":
                    self.left_prime_move()
                    self.up_prime_move()
                    self.left_move()
                    self.up_prime_move()
                    self.left_prime_move()
                    self.up_move()
                    self.up_move()
                    self.left_move()
                    continue
                elif self.red[0] == "w" and self.red[6] == "w" and self.orange[0] == "w" and self.orange[6] == "w":
                    self.right_move()
                    self.up_move()
                    self.right_prime_move()
                    self.up_move()
                    self.right_move()
                    self.up_prime_move()
                    self.right_prime_move()
                    self.up_move()
                    self.right_move()
                    self.up_move()
                    self.up_move()
                    self.right_prime_move()
                    continue
                elif self.green[0] == "w" and self.blue[6] == "w" and self.orange[0] == "w" and self.orange[6] == "w":
                    self.right_move()
                    self.up_prime_move()
                    self.left_prime_move()
                    self.up_move()
                    self.right_prime_move()
                    self.up_move()
                    self.left_move()
                    self.up_move()
                    self.left_prime_move()
                    self.up_move()
                    self.left_move()
                    continue
                elif self.white[2] == "w" and self.white[4] == "w" and self.blue[0] == "w" and self.blue[6] == "w":
                    self.right_move()
                    self.right_move()
                    self.down_prime_move()
                    self.right_move()
                    self.up_move()
                    self.up_move()
                    self.right_prime_move()
                    self.down_move()
                    self.right_move()
                    self.up_move()
                    self.up_move()
                    self.right_move()
                    continue
                elif self.green[6] == "w" and self.blue[0] == "w" and self.white[0] == "w" and self.white[2] == "w":
                    self.left_move()
                    self.front_move()
                    self.right_prime_move()
                    self.front_prime_move()
                    self.left_prime_move()
                    self.front_move()
                    self.right_move()
                    self.front_prime_move()
                    continue
                elif self.blue[6] == "w" and self.orange[0] == "w" and self.white[2] == "w" and self.white[6] == "w":
                    self.right_prime_move()
                    self.front_prime_move()
                    self.left_prime_move()
                    self.front_move()
                    self.right_move()
                    self.front_prime_move()
                    self.left_move()
                    self.front_move()
                    continue
                else:
                    self.up_move()
                    continue

            elif self.white[1] == "w" and self.white[5] == "w":
                self.front_move()
                self.right_move()
                self.up_move()
                self.right_prime_move()
                self.up_prime_move()
                self.front_prime_move()
                continue
            elif self.white[7] == "w" and self.white[3] == "w":
                self.up_move()
                self.front_move()
                self.right_move()
                self.up_move()
                self.right_prime_move()
                self.up_prime_move()
                self.front_prime_move()
                continue
            elif self.white[7] == "w" and self.white[5] == "w":
                self.front_move()
                self.up_move()
                self.right_move()
                self.up_prime_move()
                self.right_prime_move()
                self.front_prime_move()
                continue
            elif self.white[7] == "w" and self.white[1] == "w":
                self.up_prime_move()
                self.front_move()
                self.up_move()
                self.right_move()
                self.up_prime_move()
                self.right_prime_move()
                self.front_prime_move()
                continue
            elif self.white[1] == "w" and self.white[3] == "w":
                self.up_move()
                self.up_move()
                self.front_move()
                self.up_move()
                self.right_move()
                self.up_prime_move()
                self.right_prime_move()
                self.front_prime_move()
                continue
            elif self.white[3] == "w" and self.white[5] == "w":
                self.up_move()
                self.front_move()
                self.up_move()
                self.right_move()
                self.up_prime_move()
                self.right_prime_move()
                self.front_prime_move()
                continue
            else:
                self.front_move()
                self.right_move()
                self.up_move()
                self.right_prime_move()
                self.up_prime_move()
                self.front_prime_move()
                self.up_move()
                self.up_move()
                self.front_move()
                self.up_move()
                self.right_move()
                self.up_prime_move()
                self.right_prime_move()
                self.front_prime_move()
                continue

    def solve_PLL(self):
        while self.green[0] != "g" or self.green[7] != "g" or self.green[6] != "g" or self.orange[0] != "o" or \
                self.orange[7] != "o" or self.orange[6] != "o" or self.blue[0] != "b" or self.blue[7] != "b" or \
                self.blue[6] != "b" or self.red[0] != "r" or self.red[7] != "r" or self.red[6] != "r":

            if self.green[7] == self.blue[0] and self.blue[0] == self.blue[6] and self.green[0] == self.green[6] and \
                    self.green[6] == self.blue[7]:
                self.left_move()
                self.right_move()
                self.up_move()
                self.up_move()
                self.left_prime_move()
                self.right_prime_move()
                self.front_prime_move()
                self.back_prime_move()
                self.up_move()
                self.up_move()
                self.front_move()
                self.back_move()
                continue
            elif self.green[0] == self.green[7] and self.green[7] == self.green[6] and self.orange[7] == self.red[0] and \
                    self.red[0] == self.red[6]:
                self.right_move()
                self.right_move()
                self.up_prime_move()
                self.right_prime_move()
                self.up_prime_move()
                self.right_move()
                self.up_move()
                self.right_move()
                self.up_move()
                self.right_move()
                self.up_prime_move()
                self.right_move()
                continue
            elif self.green[0] == self.green[7] and self.green[7] == self.green[6] and self.blue[7] == self.red[0] and \
                    self.red[0] == self.red[6]:
                self.right_prime_move()
                self.up_move()
                self.right_prime_move()
                self.up_prime_move()
                self.right_prime_move()
                self.up_prime_move()
                self.right_prime_move()
                self.up_move()
                self.right_move()
                self.up_move()
                self.right_move()
                self.right_move()
                continue
            elif self.green[0] == self.green[6] and self.green[0] == self.red[7] and self.green[7] == self.red[0] and \
                    self.red[0] == self.red[6]:
                self.right_prime_move()
                self.up_prime_move()
                self.right_move()
                self.right_move()
                self.up_move()
                self.right_move()
                self.up_move()
                self.right_prime_move()
                self.up_prime_move()
                self.right_move()
                self.up_move()
                self.right_move()
                self.up_prime_move()
                self.right_move()
                self.up_prime_move()
                self.right_prime_move()
                continue
            elif self.green[7] == self.green[6] and self.green[6] == self.red[0] and self.orange[0] == self.orange[
                7] and self.orange[7] == self.red[6] and self.green[0] == self.orange[6] and self.orange[6] == \
                    self.blue[7]:
                self.right_prime_move()
                self.front_move()
                self.right_prime_move()
                self.back_move()
                self.back_move()
                self.right_move()
                self.front_prime_move()
                self.right_prime_move()
                self.back_move()
                self.back_move()
                self.right_move()
                self.right_move()
                continue
            elif self.blue[7] == self.blue[0] and self.blue[0] == self.red[6] and self.red[0] == self.orange[6] and \
                    self.orange[6] == self.orange[7] and self.blue[6] == self.orange[0] and self.orange[0] == \
                    self.green[7]:
                self.right_move()
                self.back_prime_move()
                self.right_move()
                self.front_move()
                self.front_move()
                self.right_prime_move()
                self.back_move()
                self.right_move()
                self.front_move()
                self.front_move()
                self.right_move()
                self.right_move()
                continue
            elif self.green[7] == self.red[6] and self.green[7] == self.orange[0] and self.orange[6] == self.blue[7] and \
                    self.blue[7] == self.red[0] and self.green[0] == self.orange[7] and self.green[0] == self.blue[6]:
                self.right_prime_move()
                self.up_move()
                self.left_prime_move()
                self.down_move()
                self.down_move()
                self.left_move()
                self.up_prime_move()
                self.right_move()
                self.left_prime_move()
                self.up_move()
                self.right_prime_move()
                self.down_move()
                self.down_move()
                self.right_move()
                self.up_prime_move()
                self.left_move()
                continue
            elif self.green[0] == self.green[7] and self.green[0] == self.green[6] and self.red[0] == self.orange[6] and \
                    self.blue[7] == self.orange[6] and self.orange[0] == self.blue[6] and self.orange[0] == self.red[7]:
                self.right_prime_move()
                self.up_move()
                self.right_move()
                self.up_prime_move()
                self.right_move()
                self.right_move()
                self.front_prime_move()
                self.up_prime_move()
                self.front_move()
                self.up_move()
                self.right_move()
                self.front_move()
                self.right_prime_move()
                self.front_prime_move()
                self.right_move()
                self.right_move()
                continue
            elif self.green[0] == self.green[6] and self.green[0] == self.blue[7] and self.red[0] == self.red[7] and \
                    self.red[0] == self.orange[6] and self.green[7] == self.orange[0] and self.orange[0] == self.blue[
                6]:
                self.up_move()
                self.up_move()
                self.front_move()
                self.front_move()
                self.down_move()
                self.right_prime_move()
                self.up_move()
                self.right_prime_move()
                self.up_prime_move()
                self.right_move()
                self.down_prime_move()
                self.front_move()
                self.front_move()
                self.left_prime_move()
                self.up_move()
                self.left_move()
                continue
            elif self.red[0] == self.red[7] and self.red[7] == self.green[6] and self.blue[7] == self.orange[6] and \
                    self.orange[6] == self.orange[0] and self.green[0] == self.orange[7] and self.green[0] == self.blue[
                6]:
                self.right_prime_move()
                self.up_prime_move()
                self.right_move()
                self.back_move()
                self.back_move()
                self.down_move()
                self.left_prime_move()
                self.up_move()
                self.left_move()
                self.up_prime_move()
                self.left_move()
                self.down_prime_move()
                self.back_move()
                self.back_move()
                continue
            elif self.green[0] == self.green[6] and self.green[0] == self.blue[7] and self.red[0] == self.orange[6] and \
                    self.red[0] == self.orange[7] and self.blue[6] == self.red[7] and self.red[7] == self.orange[0]:
                self.up_move()
                self.up_move()
                self.front_move()
                self.front_move()
                self.down_prime_move()
                self.left_move()
                self.up_prime_move()
                self.left_move()
                self.up_move()
                self.left_prime_move()
                self.down_move()
                self.front_move()
                self.front_move()
                self.right_move()
                self.up_prime_move()
                self.right_prime_move()
                continue
            elif self.red[0] == self.red[6] and self.red[0] == self.blue[7] and self.green[0] == self.orange[6] and \
                    self.green[0] == self.orange[7] and self.green[7] == self.orange[0] and self.orange[0] == self.blue[
                6]:
                self.up_move()
                self.up_move()
                self.right_move()
                self.up_move()
                self.right_prime_move()
                self.front_move()
                self.front_move()
                self.down_prime_move()
                self.left_move()
                self.up_prime_move()
                self.left_prime_move()
                self.up_move()
                self.left_prime_move()
                self.down_move()
                self.front_move()
                self.front_move()
                continue
            elif self.red[0] == self.red[6] and self.red[0] == self.red[7] and self.green[6] == self.green[7] and \
                    self.green[6] == self.blue[0] and self.green[0] == self.orange[6] and self.green[0] == self.orange[
                7]:
                self.back_move()
                self.back_move()
                self.right_prime_move()
                self.up_prime_move()
                self.right_move()
                self.back_move()
                self.back_move()
                self.left_prime_move()
                self.down_move()
                self.left_prime_move()
                self.down_prime_move()
                self.left_move()
                self.left_move()
                continue
            elif self.green[0] == self.green[7] and self.green[0] == self.blue[6] and self.green[6] == self.red[0] and \
                    self.red[0] == self.red[7] and self.orange[0] == self.orange[7] and self.orange[0] == self.orange[
                6]:
                self.right_move()
                self.up_move()
                self.right_prime_move()
                self.front_prime_move()
                self.right_move()
                self.up_move()
                self.right_prime_move()
                self.up_prime_move()
                self.right_prime_move()
                self.front_move()
                self.right_move()
                self.right_move()
                self.up_prime_move()
                self.right_prime_move()
                self.up_prime_move()
                continue
            elif self.green[0] == self.green[7] and self.green[0] == self.blue[6] and self.green[6] == self.blue[0] and \
                    self.blue[0] == self.blue[7] and self.red[6] == self.orange[0] and self.orange[0] == self.orange[7]:
                self.left_move()
                self.up_prime_move()
                self.right_move()
                self.up_move()
                self.up_move()
                self.left_prime_move()
                self.up_move()
                self.right_prime_move()
                self.left_move()
                self.up_prime_move()
                self.right_move()
                self.up_move()
                self.up_move()
                self.left_prime_move()
                self.up_move()
                self.right_prime_move()
                continue
            elif self.green[0] == self.blue[6] and self.green[0] == self.blue[7] and self.blue[0] == self.green[6] and \
                    self.blue[0] == self.green[7] and self.orange[0] == self.red[6] and self.orange[0] == self.red[7]:
                self.right_prime_move()
                self.up_move()
                self.right_move()
                self.up_prime_move()
                self.right_prime_move()
                self.front_prime_move()
                self.up_prime_move()
                self.front_move()
                self.right_move()
                self.up_move()
                self.right_prime_move()
                self.front_move()
                self.right_prime_move()
                self.front_prime_move()
                self.right_move()
                self.up_prime_move()
                self.right_move()
                continue
            elif self.green[0] == self.orange[6] and self.green[0] == self.orange[7] and self.orange[0] == self.green[
                7] and self.orange[0] == self.red[6] and self.blue[0] == self.blue[6] and self.blue[0] == self.red[7]:
                self.right_move()
                self.up_move()
                self.up_move()
                self.right_prime_move()
                self.up_move()
                self.up_move()
                self.right_move()
                self.back_prime_move()
                self.right_prime_move()
                self.up_prime_move()
                self.right_move()
                self.up_move()
                self.right_move()
                self.back_move()
                self.right_move()
                self.right_move()
                self.up_move()
                continue
            elif self.green[0] == self.green[6] and self.green[0] == self.red[7] and self.blue[0] == self.green[7] and \
                    self.blue[0] == self.red[6] and self.orange[0] == self.orange[7] and self.orange[0] == self.blue[6]:
                self.right_prime_move()
                self.up_move()
                self.up_move()
                self.right_move()
                self.up_move()
                self.up_move()
                self.right_prime_move()
                self.front_move()
                self.right_move()
                self.up_move()
                self.right_prime_move()
                self.up_prime_move()
                self.right_prime_move()
                self.front_prime_move()
                self.right_move()
                self.right_move()
                self.up_prime_move()
                continue
            elif self.green[0] == self.blue[6] and self.green[0] == self.orange[7] and self.orange[0] == self.orange[
                6] and self.orange[0] == self.red[7] and self.green[6] == self.green[7] and self.green[6] == self.red[
                0]:
                self.right_move()
                self.up_move()
                self.right_prime_move()
                self.up_prime_move()
                self.right_prime_move()
                self.front_move()
                self.right_move()
                self.right_move()
                self.up_prime_move()
                self.right_prime_move()
                self.up_prime_move()
                self.right_move()
                self.up_move()
                self.right_prime_move()
                self.front_prime_move()
                continue
            elif self.green[6] == self.green[7] and self.green[6] == self.blue[0] and self.green[0] == self.red[7] and \
                    self.green[0] == self.blue[6] and self.orange[0] == self.orange[7] and self.orange[0] == self.red[
                6]:
                self.right_prime_move()
                self.up_move()
                self.right_prime_move()
                self.up_prime_move()
                self.back_prime_move()
                self.right_prime_move()
                self.back_move()
                self.back_move()
                self.up_prime_move()
                self.back_prime_move()
                self.up_move()
                self.back_prime_move()
                self.right_move()
                self.back_move()
                self.right_move()
                continue
            elif self.green[6] == self.green[7] and self.green[6] == self.blue[0] and self.green[0] == self.orange[
                7] and self.green[0] == self.blue[6] and self.red[6] == self.orange[0] and self.orange[0] == self.blue[
                7]:
                self.front_move()
                self.front_move()
                self.down_move()
                self.right_move()
                self.right_move()
                self.up_move()
                self.right_move()
                self.right_move()
                self.down_prime_move()
                self.right_prime_move()
                self.up_prime_move()
                self.right_move()
                self.front_move()
                self.front_move()
                self.right_prime_move()
                self.up_move()
                self.right_move()
                continue
            else:
                self.up_move()
                continue

    def solve_cube(self):
        self.solution.append("\n\n" + "Cross : ")
        self.solve_cross()
        self.solve_cross_official()
        self.solution.append("\n\n" + "Corners : ")
        self.solve_corners()
        self.solution.append("\n\n" + "Edges : ")
        self.solve_edges()
        self.solution.append("\n\n" + "OLL : ")
        self.solve_OLL()
        self.solution.append("\n\n" + "PLL : ")
        self.solve_PLL()


def arrange_solution(solution1):
    solution1.append("T")
    for i in range(len(solution1) - 1):
        if i >= len(solution1) - 1:
            break
        if solution1[i] == solution1[i + 1]:
            counter = 0
            save = solution1[i]
            for j in range(i + 2, len(solution1)):
                if save != solution1[j]:
                    for k in range(j - i):
                        solution1.pop(i)
                        counter += 1
                    break
            if counter % 4 == 1:
                solution1.insert(i, save)
            elif counter % 4 == 2:
                solution1.insert(i, save + "2")
            elif counter % 4 == 3:
                solution1.insert(i, save + "'")
            else:
                solution1.insert(i, "")

            if i >= len(solution1) - 2:
                break


moves = ["U", "D", "F", "B", "R", "L"]
dir = ["", "'", "2"]
slen = 20


def scramble_gen():
    scramble = [0] * slen
    for x in range(len(scramble)):
        scramble[x] = [0] * 2
    return scramble


def scramble_replace(ar):
    for x in range(len(ar)):
        ar[x][0] = random.choice(moves)
        ar[x][1] = random.choice(dir)
    return ar


def valid(ar):
    for x in range(1, len(ar)):
        while ar[x][0] == ar[x - 1][0]:
            ar[x][0] = random.choice(moves)
    for x in range(2, len(ar)):
        while ar[x][0] == ar[x - 2][0] or ar[x][0] == ar[x - 1][0]:
            ar[x][0] = random.choice(moves)
    return ar

# USE THIS CODE TO SOLVE YOUR OWN SCRAMBLES AFTER YOU INSERT THEM IN THE FUNCTION ABOVE(my_scramble())

# newcube = Cube()
# newcube.solution = []
# newcube.my_scramble()
# newcube.solve_cube()
# mysol = newcube.get_solution()
# arrange_solution(mysol)
# newcube.print_solution(mysol)



# USE THIS CODE TO SOLVE 50000 RANDOM CUBES THAT WERE SCRAMBLED BY THE COMPUTER, THEN THE PROGRAM WILL PRINT THE
# SCRAMBLE THAT TOOK THE LEAST NUMBER OF MOVES

cubes = []
min = 1000000000
max = 0

for i in range(50000):
    cubes.append(Cube())
    cubes[i].solution = []
    cubes[i].random_scramble()
    cubes[i].solve_cube()
    mysol = cubes[i].get_solution()
    arrange_solution(mysol)
    movesnum = len(mysol) - 27
    print(i)
    if movesnum < min:
        min = movesnum
        sol1 = mysol
        j = i
    if movesnum > max:
        max = movesnum
        sol2 = mysol
        k = i

cubes[j].print_solution(sol1)
print("\n\n", "the number of moves : ", min)
print("\n\n")
cubes[k].print_solution(sol2)
print("\n\n", "the number of moves : ", max)
