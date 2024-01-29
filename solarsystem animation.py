#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Animation")

# Function to draw a planet
def draw_planet(surface, color, radius, angle, orbit_radius):
    x = WIDTH // 2 + int(math.cos(math.radians(angle)) * orbit_radius)
    y = HEIGHT // 2 + int(math.sin(math.radians(angle)) * orbit_radius)
    pygame.draw.circle(surface, color, (x, y), radius)

# Function to draw an orbit
def draw_orbit(surface, orbit_radius):
    pygame.draw.circle(surface, WHITE, (WIDTH // 2, HEIGHT // 2), orbit_radius, 1)

# Main game loop
clock = pygame.time.Clock()
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Draw the sun
    pygame.draw.circle(screen, YELLOW, (WIDTH // 2, HEIGHT // 2), 30)

    # Draw orbits
    draw_orbit(screen, 80)
    draw_orbit(screen, 150)
    draw_orbit(screen, 220)

    # Draw planets
    draw_planet(screen, BLUE, 10, angle, 80)
    draw_planet(screen, BLUE, 15, angle * 0.5, 150)
    draw_planet(screen, BLUE, 20, angle * 0.3, 220)

    # Update the angle for the next frame
    angle += 1

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)


# In[ ]:




