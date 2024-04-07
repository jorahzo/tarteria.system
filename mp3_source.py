import pygame
import os


class MP3Player:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((1820, 900))
        self.music_list = []
        self.music_dir = ''

        # Attributes below might be good to break out into its their own class
        self.number_tracks = 0
        self.song_playing_title = ""
        self.song_playing_number = 0

    def music_initializer(self):
        """Set some of our class attributes"""
        self.music_dir = '/Users/jorahzo/Desktop/code/git/tarteria.system/musicdir/'
        for item in os.listdir(self.music_dir):
            if '.mp3' in item:
                self.music_list.append(item)
        self.number_tracks = len(self.music_list)
        self.song_playing_title = self.music_list[0]

    def music_handler(self, skip_direction: int):
        """This is where we decide which song is playing"""
        if self.song_playing_title == self.music_list[0] and skip_direction == -1:
            self.song_playing_number = self.number_tracks-1
        elif self.song_playing_title == self.music_list[self.number_tracks-1] and skip_direction == 1:
            self.song_playing_number = 0
        else:
             self.song_playing_number += skip_direction
        self.song_playing_title = self.music_list[self.song_playing_number]
        pygame.mixer.music.load(self.music_dir + self.song_playing_title)
        pygame.mixer.music.play()
        
    def gameloop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type== pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        self.music_handler(-1)
                    elif event.key==pygame.K_RIGHT:
                        self.music_handler(1)
                if event.type == pygame.QUIT:
                    running = False





