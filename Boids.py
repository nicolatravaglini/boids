from Bird import Bird
import random


class Boids:
    def __init__(self, win, win_width, win_height, num):
        self.win = win
        self.win_width = win_width
        self.win_height = win_height
        self.num = num
        self.birds = []

    def generate(self):
        for i in range(self.num):
            self.birds.append(Bird(self.win, self.win_width, self.win_height,
                                   random.randint(0, self.win_width), random.randint(0, self.win_height)))

    def update(self):
        for bird in self.birds:
            bird.update(self.birds)

    def draw(self):
        for bird in self.birds:
            bird.draw()
