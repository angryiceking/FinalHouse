import os, pygame, sys, time, random
from pygame.locals import *

def sound(sound):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()

def stop_sound():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.stop()

def start():
    os.system('clear')
    raw_input('Press any key to start game. Press CTRL+C to QUIT.')
    os.system('clear')

def loading_files():
    loop = [1,2]
    s = 'Loading ...'
    for count in loop:
        for c in s:
            sys.stdout.write( '%s' % c )
            sys.stdout.flush()
            time.sleep(0.10)
        os.system('clear')

def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.10)

def intro():
    pygame.mixer.music.stop()
    sound('sound.mp3')
    delay_print('\nYou woke up from a dark room.')

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("sound.mp3")
    pygame.mixer.music.play() 

    start()
    loading_files()
    intro()

    while True:
        for event in pygame.event.get():
            if event.key == pygame.K_ESC:
                print("you pressed a key")
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

main()
