#!/usr/bin/python
import sys
import pygame
import random

def main():
    pygame.init()
    pygame.display.set_caption("Disaster-Relief")
    screen = pygame.display.set_mode((800,600))
    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

if __name__=="__main__":
    main()
