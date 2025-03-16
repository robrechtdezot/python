import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('pygames/graphics/char/Jump.png').convert_alpha()
        self.player_walk_1 = pygame.transform.scale(player_walk_1, (70, 70))
        player_walk_2 = pygame.image.load('pygames/graphics/char/Fall.png').convert_alpha()
        self.player_walk_2 = pygame.transform.scale(player_walk_2, (70, 70))
        self.player_walk = [self.player_walk_1, self.player_walk_2]
        self.player_index = 0
        player_jump = pygame.image.load('pygames/graphics/char/Jump.png').convert_alpha()
        self.player_jump = pygame.transform.scale(player_jump, (70, 70))
        player_fall = pygame.image.load('pygames/graphics/char/Fall.png').convert_alpha()
        self.player_fall = pygame.transform.scale(player_fall, (70, 70))
        self.player_jumping = [self.player_jump, self.player_fall]
        self.player_jumping_index = 0
        
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 400))
        self.gravity = 0
        
        self.walk_sound = pygame.mixer.Sound('pygames/audio/step1.ogg')
        self.walk_sound.set_volume(2)
        self.jump_sound = pygame.mixer.Sound('pygames/audio/jumpland2.mp3')
        self.jump_sound.set_volume(0.1)
    def player_input(self):
        keys = pygame.key.get_pressed()     
        if keys[pygame.K_SPACE] and self.rect.bottom >= 100:
            self.gravity = -8
            self.jump_sound.play()
    def apply_gravity(self):
        self.gravity += 0.5
        self.rect.y += self.gravity
        if self.rect.bottom >= 400:
            self.rect.bottom = 400
       
    def animation_state(self):
        if self.rect.bottom < 400:
            self.player_jumping_index += 0.1
            if self.player_jumping_index > len(self.player_jumping): self.player_jumping_index = 0
            self.image = self.player_jumping[int(self.player_jumping_index)]
            
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
            if self.player_index == 0: self.walk_sound.play()
        if game_active == False:    
            self.walk_sound.stop()
            
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state() 
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'character':
            character_surf1 = pygame.image.load('pygames/graphics/char/Jump2.png').convert_alpha()
            character_surf1 = pygame.transform.scale(character_surf1, (70, 70))
            character_surf2 = pygame.image.load('pygames/graphics/char/Fall2.png').convert_alpha()
            character_surf2 = pygame.transform.scale(character_surf2, (70, 70))
            self.frames = [character_surf1, character_surf2]
            y_pos = 400
            self.walk_sound2 = pygame.mixer.Sound('pygames/audio/stomp.flac')
            self.walk_sound2.set_volume(20)
            self.walk_sound2.play()
        elif type == 'character2':
            character2_surf1 = pygame.image.load('pygames/graphics/char/Jump3.png').convert_alpha()
            character2_surf1 = pygame.transform.scale(character2_surf1, (70, 70))
            character2_surf2 = pygame.image.load('pygames/graphics/char/Fall3.png').convert_alpha()
            character2_surf2 = pygame.transform.scale(character2_surf2, (70, 70))
            self.frames = [character2_surf1, character2_surf2]
            y_pos = 150
            self.walk_sound3 = pygame.mixer.Sound('pygames/audio/fly.wav')
            self.walk_sound3.set_volume(4)
            self.walk_sound3.play()
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos)) 
    
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0  
        self.image = self.frames[int(self.animation_index)] 
        
        
    def update(self):
        self.animation_state()
        self.rect.x -= 3
        self.destroy()
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()     
                             
def display_score():
    current_score = pygame.time.get_ticks() // 1000 - start_time // 1000 #score
    score_surf = test_font.render(f'Score: {current_score}', False, ('Red')) #score
    score_rectangle = score_surf.get_rect(center = (400, 500)) #score #update screen
    screen.blit(score_surf, score_rectangle) #score #update screen   
    
    
def obstacle_movement(obstacle_list):
    
    if obstacle_rect_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 1
            
            # if obstacle_rect.bottom == 400:screen.blit(character_surf ,obstacle_rect)
            # else: screen.blit(character2_surf ,obstacle_rect)
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else : return []
def collision(player, obstacles):
    for obstacle_rect in obstacles:
        if player.colliderect(obstacle_rect):
            return False
    return True
def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        lose_music.play()
        return False
    else: return True   
    
pygame.init() #basis
screen = pygame.display.set_mode((800, 600)) #screen size
pygame.display.set_caption('First Game') #title
sky = pygame.image.load('pygames/graphics/sky.png').convert() #icon      convert png for faster load
sky = pygame.transform.scale(sky, (800, 600)) #icon
ground = pygame.image.load('pygames/graphics/Battleground1.png').convert()#achtergrond
ground = pygame.transform.scale(ground, (1000, 600)) #achtergrond
test_font = pygame.font.Font("pygames/font/BreatheFireIii-PKLOB.ttf", 50) #achtergrond
clock = pygame.time.Clock() #fps
game_active = True #game loop
start_time = 0 #start time
bg_music = pygame.mixer.Sound('pygames/audio/music.ogg')
bg_music.set_volume(0.1)
bg_music.play(loops = -1)
lose_music = pygame.mixer.Sound('pygames/audio/you_lose.ogg')
lose_music.set_volume(2)
player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()  
obstacle_rect_list = []
#text           
test_surf = pygame.Surface((100, 100)) #surface
test_ground = ground.get_rect() #achtergrond
test_ground.topleft = (0, 400) #achtergrond
test_text = test_font.render('My game', True, (255, 140, 0, 255))#text     "firebrick3": (205, 38, 38, 255),
test_text_rectangle = test_text.get_rect(center = (400, 50)) #text

player_gravity = 0
player_surface = pygame.image.load('pygames/graphics/char/Jump.png').convert_alpha()
player_big = pygame.transform.smoothscale(player_surface, (250, 250))
player_big_rectangle = player_big.get_rect(midbottom = (375, 580))
#timers
obstacle_timer = pygame.USEREVENT + 1 #timer   userevent always +1
pygame.time.set_timer(obstacle_timer, 4000)
character_timer = pygame.USEREVENT + 4
pygame.time.set_timer(character_timer, 400)
character2_timer = pygame.USEREVENT + 2
pygame.time.set_timer(character2_timer, 150)
#highscore
high_score = 0

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()           
        if game_active:        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
        else:
            if event.type == pygame.MOUSEBUTTONDOWN and play_again_rect.collidepoint(event.pos): 
                    game_active = True
                    start_time = pygame.time.get_ticks()
                    lose_music.stop()
                    bg_music.play(loops = -1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    game_active = True       
                    start_time = pygame.time.get_ticks()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()                               
        if game_active:            
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['character', 'character2', 'character'])))              
    if game_active:    
        screen.blit(sky, (0, 0)) 
        screen.blit(ground, (0, 50)) #position    
        screen.blit(test_text, (test_text_rectangle)) #position
        display_score()
        player.draw(screen)
        player.update() 
        obstacle_group.draw(screen)
        obstacle_group.update()     
        game_active = collision_sprite ()
               
    else:
        game_over = test_font.render('Game Over', True, ('darkred'))
        game_over_rectangle = game_over.get_rect(center = (400, 50))
        play_again = test_font.render('Play Again ?', True, ('brown3'))
        play_again_rect = play_again.get_rect(center = (400, 300))
         # play once
        obstacle_rect_list.clear()
        player.update()
        player_gravity = 0 
        bg_music.stop()
        
        
        
        
        
        screen.fill((0, 0, 0))
        screen.blit(player_big, (player_big_rectangle))
        screen.blit(game_over, (game_over_rectangle))
        screen.blit(play_again, play_again_rect)
                
    pygame.display.update() #update screen
    clock.tick(60) #fps 60 