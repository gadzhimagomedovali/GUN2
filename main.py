import math
from random import choice
import random
from time import time
import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

class Airship():
    def __init__(self, _screen: pygame.Surface, x=0, y=0, a=0, b=0, color=GREY):
        self.live = 1
        self.screen = _screen
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.color = color
        self.points = 0
        self.vx = 0.8 - 0.7
        self.t = time()



    def hit(self, points=1):
        self.points += points

    def draw(self):
        pygame.draw.ellipse(self.screen,self.color,(self.x, self.y, self.a, self.b))
        y1 = self.y + self.b + 5
        x1 = self.x + self.a//2
        y2 = self.y + self.b + 5
        x2 = self.x - 20 + self.a//2
        y3 = self.y + self.b//2
        x3 = self.x - 20 + self.a//2
        y4 = self.y + self.b//2
        x4 = self.x + 20 + self.a//2
        y5 = self.y + self.b + 5
        x5 = self.x + 20 + self.a//2
        pygame.draw.polygon(self.screen, self.color, [[x1, y1], [x2, y2], [x3, y3], [x4, y4], [x5, y5]])


    def move(self, t):
        self.x += self.vx * t
        if self.x + self.a >= WIDTH:
            self.x = WIDTH - self.a
            self.vx = -self.vx
        elif self.x <= 0:
            self.x = 0
            self.vx = -self.vx
        if time()-self.t > 4:
            self.t = time()
            bombs.append(Bomb(screen, self.x + self.a//2, self.y + self.b//2))

class Bomb:
    def __init__(self, _screen: pygame.Surface, x , y):
        self.screen = _screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30


    def move(self, t):
        g = 0.001
        self.vy -= g * t
        self.y -= self.vy*t

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest1(self, obj):
        if (self.x-obj.x)**2+(self.y-obj.y)**2 <= (obj.r+self.r)**2:
            return True
        else:
            return False



class Target1:
    # self.points = 0
    # self.live = 1
    #
    # self.new_target()
    def __init__(self, _screen: pygame.Surface, x=0, y=0, r=0, color=RED):
        self.live = 1
        self.screen = _screen
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.points = 0
        self.vx = 0.5-0.7*random.random()
        self.vy = 0.5-0.7*random.random()


    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def movetar1(self, t):
        self.x += self.vx * t
        self.y += self.vy * t
        if self.x - self.r <= 0:
            self.x = self.r
            self.vx = -self.vx
        elif self.x + self.r >= 800:
            self.x = 800 - self.r
            self.vx = -self.vx
        elif self.y - self.r <= 0:
            self.y = self.r
            self.vy = -self.vy
        elif self.y + self.r >= 450:
            self.y = 450 - self.r
            self.vy = -self.vy


    def movetar2(self, t):
        self.x += self.vx * t
        self.y += self.vy * t
        if self.x - self.r <= 0:
            self.x = self.r
            self.vx = -self.vx
        elif self.x + self.r >= 800:
            self.x = 800 - self.r
            self.vx = -self.vx
        elif self.y - self.r <= 0:
            self.y = self.r
            self.vy = -self.vy
        elif self.y + self.r >= 450:
            self.y = 450 - self.r
            self.vy = -self.vy

class Target2(Target1):
    # self.points = 0
    # self.live = 1
    #
    # self.new_target()
    def __init__(self, _screen: pygame.Surface, x=0, y=0, r=0, color=RED):
        self.live = 1
        self.screen = _screen
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.points = 0
        self.vx = 0.4-0.6*random.random()
        self.vy = 0.4-0.6*random.random()

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def movetar2(self, t):
        self.x += self.vx * t
        self.y += self.vy * t
        if self.x - self.r <= 0:
            self.x = self.r
            self.vx = -self.vx
        elif self.x + self.r >= 800:
            self.x = 800 - self.r
            self.vx = -self.vx
        elif self.y - self.r <= 0:
            self.y = self.r
            self.vy = -self.vy
        elif self.y + self.r >= 450:
            self.y = 450 - self.r
            self.vy = -self.vy


    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

class Gun:
    def __init__(self, _screen: pygame.Surface):
        self.screen = _screen
        self.f2_power = 1
        self.f2_on = 0
        self.an = 0
        self.color = GREY
        self.y = 580
        self.x = 400
        self.r = 15


    def fire2_start(self, event):
        self.f2_on = 0.5

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        if is_ball:
            new_ball = Ball(self.screen, x=self.x, y=self.y)
        else:
            new_ball = Arrow(self.screen, x=self.x, y=self.y)
        new_ball.r += 5
        self.scale = 0.3
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)*self.scale
        new_ball.vy = - self.f2_power * math.sin(self.an)*self.scale
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 1

    def move(self):
        speed = 0
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[97] and (not (pressed_keys[100])) and self.x > 20:
            speed = -7
        elif (not (pressed_keys[97])) and pressed_keys[100] and self.x < WIDTH - 20:
            speed = 7
        self.x += speed

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event and (event.pos[1] < self.y):
            self.an = math.atan((event.pos[0] - self.x) / (event.pos[1] - self.y))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        '''rect1 = pygame.Surface((50 * self.f2_power, 10))
        rotrect = pygame.transform.rotate(rect1, self.an)
        rect = rotrect.get_rect(center = (20, 450))
        self.screen.blit(rotrect, rect)'''
        y11 = self.y + 5 * math.sin(self.an)
        x11 = self.x - 5 * math.cos(self.an)
        y12 = self.y - 5 * math.sin(self.an)
        x12 = self.x + 5 * math.cos(self.an)

        y21 = self.y - (self.f2_power + 40) * math.cos(self.an) - 5 * math.sin(self.an)
        x21 = self.x - (self.f2_power + 40) * math.sin(self.an) + 5 * math.cos(self.an)
        y22 = self.y - (self.f2_power + 40) * math.cos(self.an) + 5 * math.sin(self.an)
        x22 = self.x - (self.f2_power + 40) * math.sin(self.an) - 5 * math.cos(self.an)
        pygame.draw.polygon(self.screen, self.color, [[x11, y11], [x12, y12], [x21, y21], [x22, y22]])
        pygame.draw.circle(self.screen, [29, 150, 20], [self.x, self.y], 20)
        x1 = self.x - 40
        y1 = self.y
        x2 = self.x - 40
        y2 = self.y + 10
        x3 = self.x - 20
        y3 = self.y + 20
        x4 = self.x + 40
        y4 = self.y
        x5 = self.x + 40
        y5 = self.y + 10
        x6 = self.x + 20
        y6 = self.y + 20
        pygame.draw.polygon(self.screen, [100, 200, 20], [[x1, y1], [x2, y2], [x3, y3], [x6, y6], [x5, y5], [x4, y4]])


    def power_up(self):
        if self.f2_on:
            if self.f2_power < 10:
                self.f2_power += 0.5
            self.color = RED
        else:
            self.color = GREY

class Ball():

    def __init__(self, _screen: pygame.Surface, x = 410, y = 520):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = _screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30


    def move(self, t):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        g = 0.01
        self.vy -= g * t
        self.x += self.vx*t
        self.y -= self.vy*t

        if self.x - self.r <= 0:
            self.x = self.r
            self.vx = -self.vx
        elif self.x + self.r >= WIDTH:
            self.x = WIDTH - self.r
            self.vx = -self.vx
        elif self.y - self.r <= 0:
            self.y = self.r
            self.vy = -self.vy



    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest1(self, obj: Target1):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x-obj.x)**2+(self.y-obj.y)**2 <= (obj.r+self.r)**2:
            return True
        else:
            return False

    def hittest2(self, obj: Airship):
        if (self.x  - (obj.x + obj.a//2)) ** 2 + (self.y - (obj.y + obj.b//2)) ** 2 <= (obj.b//2 + self.r) ** 2:
            return True
        else:
            return False

    def hittest1(self, obj: Target2):
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (obj.r + 3 + self.r) ** 2:
            return True
        else:
            return False

class Arrow():

    def __init__(self, _screen: pygame.Surface, x = 410, y = 520):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = _screen
        self.x = x
        self.y = y
        self.r = 40
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30


    def move(self, t):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        g = 0.01
        self.vy -= g * t
        self.x += self.vx*t
        self.y -= self.vy*t

        if self.x - self.r <= 0:
            self.x = self.r
            self.vx = -self.vx
        elif self.x + self.r >= WIDTH:
            self.x = WIDTH - self.r
            self.vx = -self.vx
        elif self.y - self.r <= 0:
            self.y = self.r
            self.vy = -self.vy



    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest1(self, obj: Target1):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x-obj.x)**2+(self.y-obj.y)**2 <= (obj.r+self.r)**2:
            return True
        else:
            return False

    def hittest2(self, obj: Airship):
        if (self.x  - (obj.x + obj.a//2)) ** 2 + (self.y - (obj.y + obj.b//2)) ** 2 <= (obj.b//2 + self.r) ** 2:
            return True
        else:
            return False

    def hittest1(self, obj: Target2):
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (obj.r + 3 + self.r) ** 2:
            return True
        else:
            return False



def rnd(a,b):
    return a + (b-a)*random.random()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
is_ball = True
bullet = 0
balls = []
bombs = []

clock = pygame.time.Clock()
gun = Gun(screen)
target1 = Target1(screen, rnd(200, 600),
        rnd(100, 380),
        rnd(2, 50))
target2 = Target2(screen, rnd(200, 600),
        rnd(100, 380),
        rnd(2, 50))
airship1 = Airship(screen, 0, rnd(300, 350), rnd(80, 140), rnd(50, 60))
airship2 = Airship(screen, 0, rnd(200, 300), rnd(80, 140), rnd(50, 60))
airship3 = Airship(screen, 0, rnd(100, 250), rnd(80, 140), rnd(50, 60))

finished = False
t0 = pygame.time.get_ticks()
while not finished:
    t1 = pygame.time.get_ticks()
    dt = t1 - t0
    t0 = t1

    screen.fill(WHITE)
    gun.move()

    gun.draw()
    airship1.move(dt)
    airship2.move(dt)
    airship3.move(dt)
    target1.draw()
    target2.draw()
    airship1.draw()
    airship2.draw()
    airship3.draw()
    for b in balls:
        b.draw()
    for g in bombs:
        g.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                is_ball = True
            elif event.key == pygame.K_2:
                is_ball = False

    target1.movetar1(dt)
    target2.movetar2(dt)
    for b in balls:
        b.move(dt)
        if b.hittest1(target1) and target1.live:
            target1.live = 0
            target1.hit()
            target1 = Target1(screen, rnd(600, 780),
        rnd(300, 550),
        rnd(2, 50))
        elif b.hittest1(target2) and target2.live:
            target2.live = 0
            target2.hit()
            target2 = Target1(screen, rnd(600, 780),
        rnd(300, 550),
        rnd(2, 50))
        elif b.hittest2(airship1) and airship1.live:
            airship1.live = 0
            airship1.hit()
            airship1 = Airship(screen, 0, rnd(300, 350), rnd(80, 140), rnd(50, 60))
        elif b.hittest2(airship2) and airship2.live:
            airship2.live = 0
            airship2.hit()
            airship2 = Airship(screen, 0, rnd(200, 300), rnd(80, 140), rnd(50, 60))
        elif b.hittest2(airship3) and airship3.live:
            airship3.live = 0
            airship3.hit()
            airship3 = Airship(screen, 0, rnd(100, 250), rnd(80, 140), rnd(50, 60))

    for g in bombs:
        g.move(dt)
        if g.hittest1(gun):
            finished = True



    gun.power_up()

pygame.quit()
