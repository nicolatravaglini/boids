import math
import random
import pygame


class Bird:
    def __init__(self, win, win_width, win_height, x, y):
        self.win = win
        self.win_width = win_width
        self.win_height = win_height
        self.x = x
        self.y = y
        self.velocity = [random.uniform(-1, 1), random.uniform(-1, 1)]
        # Constants
        self.field_of_view = 50
        self.field_of_avoidance = 20
        self.cohesion_rate = 0.0002
        self.separation_rate = 0.005
        self.alignment_rate = 0.04

    @staticmethod
    def normalize(value):
        if value > 1:
            value = 1
        elif value < -1:
            value = -1
        return value

    @staticmethod
    def distance(bird1, bird2):
        return math.dist((bird1.x, bird1.y), (bird2.x, bird2.y))

    def cohesion(self, birds):
        average_position = [0, 0]
        neighbours = 0
        for bird in birds:
            if self != bird and Bird.distance(self, bird) < self.field_of_view:
                average_position[0] += bird.x
                average_position[1] += bird.y
                neighbours += 1
        if neighbours > 0:
            average_position[0] /= neighbours
            average_position[1] /= neighbours
            self.velocity[0] = Bird.normalize(self.velocity[0] + (average_position[0] - self.x) * self.cohesion_rate)
            self.velocity[1] = Bird.normalize(self.velocity[1] + (average_position[1] - self.y) * self.cohesion_rate)

    def separation(self, birds):
        steering = [0, 0]
        for bird in birds:
            if self != bird and Bird.distance(self, bird) <= self.field_of_avoidance:
                steering[0] += self.x - bird.x
                steering[1] += self.y - bird.y
        self.velocity[0] = Bird.normalize(self.velocity[0] + steering[0] * self.separation_rate)
        self.velocity[1] = Bird.normalize(self.velocity[1] + steering[1] * self.separation_rate)

    def alignment(self, birds):
        average_direction = [0, 0]
        neighbours = 0
        for bird in birds:
            if self != bird and Bird.distance(self, bird) < self.field_of_view:
                average_direction[0] += bird.velocity[0]
                average_direction[1] += bird.velocity[1]
                neighbours += 1
        if neighbours > 0:
            average_direction[0] /= neighbours
            average_direction[1] /= neighbours
            self.velocity[0] = Bird.normalize(self.velocity[0] + (average_direction[0] - self.velocity[0]) * self.alignment_rate)
            self.velocity[1] = Bird.normalize(self.velocity[1] + (average_direction[1] - self.velocity[1]) * self.alignment_rate)

    def noise_velocity(self):
        self.velocity[0] = Bird.normalize(self.velocity[0] + random.uniform(-0.1, 0.1))
        self.velocity[1] = Bird.normalize(self.velocity[1] + random.uniform(-0.1, 0.1))

    def move(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def pacman_effect(self):
        if self.x > self.win_width:
            self.x = 0
        elif self.x < 0:
            self.x = self.win_width
        if self.y > self.win_height:
            self.y = 0
        elif self.y < 0:
            self.y = self.win_height

    def update(self, birds):
        self.cohesion(birds)
        self.alignment(birds)
        self.separation(birds)

        self.noise_velocity()

        self.move()
        self.pacman_effect()

    def draw(self):
        pygame.draw.circle(self.win, (255, 255, 255), (self.x, self.y), 3)
