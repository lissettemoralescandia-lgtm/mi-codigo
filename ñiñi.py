import turtle
import math
import random
import time

# ================== Screen Setup ==================
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("❤️ Neon Heart Animation")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)

# ================== Heart Drawing Function ==================
def draw_heart(scale, color, glow=False):
    t.color(color)
    if glow:
        t.width(4)
    else:
        t.width(2)

    t.begin_fill()
    for i in range(361):
        x = scale * 16 * math.sin(math.radians(i))**3
        y = scale * (
            13 * math.cos(math.radians(i))
            - 5 * math.cos(2 * math.radians(i))
            - 2 * math.cos(3 * math.radians(i))
            - math.cos(4 * math.radians(i))
        )
        t.goto(x, y)
    t.end_fill()

# ================== Light Particles ==================
particles = []

def create_particles():
    for _ in range(40):
        angle = random.uniform(0, 360)
        radius = random.uniform(40, 160)
        speed = random.uniform(0.3, 1.2)
        particles.append([angle, radius, speed])

def draw_particles(scale):
    t.color("#fb718b")
    for p in particles:
        p[0] += p[2]
        x = math.cos(math.radians(p[0])) * p[1] * scale / 14
        y = math.sin(math.radians(p[0])) * p[1] * scale / 14
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(3)

# ================== Heart Animation ==================
create_particles()

pulse = 0
while True:
    t.clear()

    # Heart pulse
    scale = 14 + math.sin(pulse) * 1.2
    pulse += 0.08

    # Background glow
    for s in range(18, 14, -1):
        t.penup()
        t.goto(0, -10)
        t.pendown()
        draw_heart(s + math.sin(pulse)*0.5, "#A80606", glow=True)

    # Main heart
    t.penup()
    t.goto(0, -10)
    t.pendown()
    draw_heart(scale, "#ff1a1a")

    # Particles
    draw_particles(scale)

    # Text
    t.penup()
    t.goto(0, -220)
    t.color("#ff6f91")
    t.write(
        "I miss you ❤️",
        align="center",
        font=("Segoe UI", 26, "bold")
    )

    screen.update()
    time.sleep(0.03)