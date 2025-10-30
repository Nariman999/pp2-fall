import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 400, 200
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Music Player")
timer = pygame.time.Clock()

songs = ["music1.mp3", "music2.mp3", "music3.mp3"]
pos = 0
mode = "stop"

def start_track():
    global mode
    pygame.mixer.music.load(songs[pos])
    pygame.mixer.music.play()
    mode = "play"
    print("Now playing:", songs[pos])

def halt():
    global mode
    pygame.mixer.music.stop()
    mode = "stop"
    print("Music stopped")

def toggle():
    global mode
    if mode == "play":
        pygame.mixer.music.pause()
        mode = "pause"
        print("Paused")
    elif mode == "pause":
        pygame.mixer.music.unpause()
        mode = "play"
        print("Continue")
    elif mode == "stop":
        start_track()

def forward():
    global pos
    pos = (pos + 1) % len(songs)
    start_track()

def back():
    global pos
    pos = (pos - 1) % len(songs)
    start_track()

start_track()

go = True
while go:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            go = False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                go = False
            elif ev.key == pygame.K_SPACE:
                toggle()
            elif ev.key == pygame.K_s:
                halt()
            elif ev.key == pygame.K_RIGHT:
                forward()
            elif ev.key == pygame.K_LEFT:
                back()

    if mode == "play" and not pygame.mixer.music.get_busy():
        forward()

    win.fill((40, 30, 25))
    pygame.display.update()
    timer.tick(30)

pygame.quit()
sys.exit()
