#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random

SCREEN_DIM = (800, 600)


class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2d(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vec2d(self.x * other, self.y * other)

    def __len__(self):
        return pow((self.x * self.x + self.y * self.y),0.5)

    def int_pair(self):
        return self.x, self.y


class Point2d:
    def __init__(self, location, velocity):
        self.location = location
        self.velocity = velocity

    def move(self):
        self.location = self.location + self.velocity
        if self.location.x >= SCREEN_DIM[0] or self.location.x <= 0:
            self.velocity.x = - self.velocity.x
        if self.location.y >= SCREEN_DIM[1] or self.location.y <= 0:
            self.velocity.y = - self.velocity.y


class Polyline:
    def __init__(self):
        self.points = []

    def add(self, point):
        self.points.append(point)

    def set_points(self):
        for p in self.points:
            p.move()

    def draw_points(self, game_display, width=3, color=(255, 255, 255)):
        for p in self.points:
            pygame.draw.circle(game_display, color,
                                  (int(p.location.x), int(p.location.y)), width)

    def draw_smooth_line(self, game_display, colour, width, count):
        if len(self.points) >= 3:
            res = []
            for i in range(-2, len(self.points) - 2):
                ptn = [(self.points[i].location + self.points[i + 1].location) * 0.5, self.points[i + 1].location,
                       (self.points[i + 1].location + self.points[i + 2].location) * 0.5]
                res.extend(Polyline.get_points(ptn, count))
            for p_n in range(-1, len(res) - 1):
                pygame.draw.line(game_display, colour,
                                 (int(res[p_n].x), int(res[p_n].y)),
                                 (int(res[p_n + 1].x), int(res[p_n + 1].y)), width)

    @staticmethod
    def get_points(base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(Polyline.get_point(base_points, i * alpha))
        return res

    @staticmethod
    def get_point(points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg] * alpha + Polyline.get_point(points, alpha, deg - 1) * (1 - alpha)


class Application:
    def __init__(self, caption):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode(SCREEN_DIM)
        pygame.display.set_caption(caption)
        self.steps = 35
        self.working = True
        self.line = Polyline()
        self.pause = True
        self.show_help = False
        self.hue = 0
        self.color = pygame.Color(0)

    def run(self):
        while self.working:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.working = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.working = False
                    if event.key == pygame.K_r:
                        self.line.points.clear()
                    if event.key == pygame.K_p:
                        self.pause = not self.pause
                    if event.key == pygame.K_KP_PLUS:
                        self.steps += 1
                    if event.key == pygame.K_F1:
                        self.show_help = not self.show_help
                    if event.key == pygame.K_KP_MINUS:
                        self.steps -= 1 if self.steps > 1 else 0

                if event.type == pygame.MOUSEBUTTONDOWN:
                    location = Vec2d(event.pos[0], event.pos[1])
                    velocity = Vec2d(random.random() * 2, random.random() * 2)
                    new_point = Point2d(location, velocity)
                    self.line.add(new_point)

            self.gameDisplay.fill((0, 0, 0))
            self.hue = (self.hue + 1) % 360
            self.color.hsla = (self.hue, 100, 50, 100)
            self.line.draw_points(self.gameDisplay)
            self.line.draw_smooth_line(self.gameDisplay, self.color, 3, self.steps)
            if not self.pause:
                self.line.set_points()
            if self.show_help:
                self.draw_help()

            pygame.display.flip()

        pygame.display.quit()
        pygame.quit()

    def draw_help(self):
        self.gameDisplay.fill((50, 50, 50))
        font1 = pygame.font.SysFont("courier", 24)
        font2 = pygame.font.SysFont("serif", 24)
        data = []
        data.append(["F1", "Show Help"])
        data.append(["R", "Restart"])
        data.append(["P", "Pause/Play"])
        data.append(["Num+", "More points"])
        data.append(["Num-", "Less points"])
        data.append(["", ""])
        data.append([str(self.steps), "Current points"])

        pygame.draw.lines(self.gameDisplay, (255, 50, 50, 255), True, [
            (0, 0), (800, 0), (800, 600), (0, 600)], 5)
        for i, text in enumerate(data):
            self.gameDisplay.blit(font1.render(
                text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
            self.gameDisplay.blit(font2.render(
                text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    myapp = Application("MyScreenSaver")
    myapp.run()
    exit(0)
