import pygame
from sys import exit
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/char/Jump.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect(midbottom = (80, 400))
        self.gravity = 0
    def player_input(self):
        keys = pygame.key.get_pressed()     
        if keys[pygame.K_SPACE]:
            self.gravity = -8
        
    def apply_gravity(self):
        self.gravity += 0.5
        self.rect.y += self.gravity
        if self.rect.bottom >= 400:
            self.rect.bottom = 400
    def update(self):
        self.player_input()
        self.apply_gravity()

def display_score():
    current_score = pygame.time.get_ticks() // 1000 - start_time // 1000 #score
    score_surf = test_font.render(f'Score: {current_score}', False, ('Red')) #score
    score_rectangle = score_surf.get_rect(center = (400, 500)) #score #update screen
    screen.blit(score_surf, score_rectangle) #score #update screen
    
def obstacle_movement(obstacle_list):
    
    if obstacle_rect_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 1
            
            if obstacle_rect.bottom == 400:screen.blit(character_surf ,obstacle_rect)
            else: screen.blit(character2_surf ,obstacle_rect)
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > 0]
        return obstacle_list
    else : return []
    
def collision(player, obstacles):
    for obstacle_rect in obstacles:
        if player.colliderect(obstacle_rect):
            return False
    return True
 
def player_animation():
    global player_surf, player_index, player_jumping, player_jumping_index
    if player_rect.bottom < 400:
        player_jumping_index += 0.1
        if player_jumping_index > len(player_jumping): player_jumping_index = 0
        player_surf = player_jumping[int(player_jumping_index)]
    else:
        player_index += 0.1
        if player_index > len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]
 
def character_animation():
    global character_surf, character_index, character_jumping, character_jumping_index
    if character_rect.bottom < 400:
        character_jumping_index += 0.1
        if character_jumping_index > len(character_jumping): character_jumping_index = 0
        character_surf = character_jumping[int(character_jumping_index)]
    else:
        character_index += 0.1
        if character_index > len(character_walk): character_index = 0
        character_surf = character_walk[int(character_index)] 
 
def character2_animation():
    global character2_surf, character2_index, character2_jumping, character2_jumping_index
    if character2_rect.bottom < 400:
        character2_jumping_index += 0.1
        if character2_jumping_index > len(character2_jumping): character2_jumping_index = 0
        character2_surf = character2_jumping[int(character2_jumping_index)] 
    else:
        character2_index += 0.1
        if character2_index > len(character2_walk): character2_index = 0
        character2_surf = character2_walk[int(character2_index)]
    
pygame.init() #basis
screen = pygame.display.set_mode((800, 600)) #screen size
pygame.display.set_caption('First Game') #title
sky = pygame.image.load('graphics/sky.png').convert() #icon      convert png for faster load
sky = pygame.transform.scale(sky, (800, 600)) #icon
ground = pygame.image.load('graphics/Battleground1.png').convert()#achtergrond
ground = pygame.transform.scale(ground, (1000, 600)) #achtergrond
test_font = pygame.font.Font("font\BreatheFireIii-PKLOB.ttf", 50) #achtergrond
clock = pygame.time.Clock() #fps
game_active = True #game loop
start_time = 0 #start time

player = pygame.sprite.GroupSingle()
player.add(Player())
#text           
test_surf = pygame.Surface((100, 100)) #surface
test_ground = ground.get_rect() #achtergrond
test_ground.topleft = (0, 400) #achtergrond
test_text = test_font.render('My game', True, (255, 140, 0, 255))#text     "firebrick3": (205, 38, 38, 255),
test_text_rectangle = test_text.get_rect(center = (400, 50)) #text

character_walk_1 = pygame.image.load('graphics/char/Jump2.png').convert_alpha()
character_walk_2 = pygame.image.load('graphics/char/Fall2.png').convert_alpha()
character_walk = [character_walk_1, character_walk_2]
character_index = 0
character_jump = pygame.image.load('graphics/char/Jump2.png').convert_alpha()
character_fall = pygame.image.load('graphics/char/Fall2.png').convert_alpha()
character_jumping = [character_jump, character_fall]#character
character_jumping_index = 0
character_surf = character_walk[character_index]
character_surf = pygame.transform.scale(character_surf, (90, 90)) #character
character_surf = pygame.transform.flip(character_surf, True, False)
character_rect = character_surf.get_rect(bottomright = (600, 400))

character2_walk_1 = pygame.image.load('graphics/char/Jump3.png').convert_alpha()
character2_walk_1 = pygame.transform.scale(character2_walk_1, (90, 90))
character2_walk_2 = pygame.image.load('graphics/char/Fall3.png').convert_alpha()
character2_walk_2 = pygame.transform.scale(character2_walk_2, (90, 90))
character2_walk = [character2_walk_1, character2_walk_2]
character2_index = 0
character2_jump = pygame.image.load('graphics/char/Jump3.png').convert_alpha()
character2_fall = pygame.image.load('graphics/char/Fall3.png').convert_alpha()
character2_jumping = [character2_jump, character2_fall]
character2_jumping_index = 0
character2_surf = character2_walk[character2_index]
character2_surf = pygame.transform.scale(character2_surf, (90, 90)) #character    
character2_surf = pygame.transform.flip(character2_surf, True, False)
character2_rect = character2_surf.get_rect(bottomright = (800, 400))

obstacle_rect_list = []

player_walk_1 = pygame.image.load('graphics/char/Jump.png').convert_alpha()
player_walk_1 = pygame.transform.scale(player_walk_1, (70, 70))
player_walk_2 = pygame.image.load('graphics/char/Fall.png').convert_alpha()
player_walk_2 = pygame.transform.scale(player_walk_2, (70, 70))
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('graphics/char/Jump.png').convert_alpha()
player_jump = pygame.transform.scale(player_jump, (70, 70))
player_fall = pygame.image.load('graphics/char/Fall.png').convert_alpha()
player_fall = pygame.transform.scale(player_fall, (70, 70))
player_jumping = [player_jump, player_fall]
player_jumping_index = 0
player_surf = player_walk[player_index]
player_surf = pygame.transform.scale(player_surf, (90, 90))
player_rect = player_surf.get_rect(midbottom = (100, 400))
player_gravity = 0

player_big = pygame.transform.smoothscale(player_surf, (250, 250))
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
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.collidepoint(event.pos):
                if player_rect.bottom >= 50:
                    print('click-jump')
                    player_gravity = -30
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom >= 50:
                        print('jump')
                        player_gravity = -8
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
        else:
            if event.type == pygame.MOUSEBUTTONDOWN and play_again_rect.collidepoint(event.pos): 
                    game_active = True
                    start_time = pygame.time.get_ticks()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True       
                    start_time = pygame.time.get_ticks()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()           
                    
        if game_active:            
            if event.type == obstacle_timer:
                if randint(0, 2) == 0:
                    obstacle_rect_list.append(character2_surf.get_rect(bottomleft = (randint(900, 1100), 400)))
                else:
                    obstacle_rect_list.append(character_surf.get_rect(bottomleft = (randint(900, 1100), 150)))
            if event.type == character_timer:
                if character_index == 0:
                    character_index = 1
                else:   
                    character_index = 0
                character_surf = character_walk[character_index]
                character_surf = pygame.transform.scale(character_surf, (90, 90)) #character
                character_surf = pygame.transform.flip(character_surf, True, False)
            if event.type == character2_timer:
                if character2_index == 0:
                    character2_index = 1
                else:   
                    character2_index = 0
                character2_surf = character2_walk[character2_index]
                character2_surf = pygame.transform.scale(character2_surf, (90, 90)) #character
                character2_surf = pygame.transform.flip(character2_surf, True, False)    
        
            
            # obstacle_rect_list.append(pygame.transform.scale())
            print(obstacle_timer)
            
            
        # if event.type == pygame.KEYUP:
        #     print('key up')
    if game_active:    
        screen.blit(sky, (0, 0)) 
        screen.blit(ground, (0, 50)) #position    
        screen.blit(test_text, (test_text_rectangle)) #position
        display_score()
    # pygame.draw.ellipse(screen, 'Black', pygame.Rect(350,300,100,100)) #collision box

        
        # character_rect.x -= 2 
        # if character_rect.x <= 0:
        #     character_rect.x = 600 
        # screen.blit(character_surf, (character_rect))
        
        # player_surf_rectangle.x -= 2
        # player_surf_rectangle_scaled.x -= 2
        # if player_surf_rectangle.left < 0:
        #     player_surf_rectangle.right = 800
        #     player_surf_rectangle_scaled.right = 800
            
        player_gravity += 0.5
        player_rect.y += player_gravity
        if player_rect.bottom >= 400: player_rect.bottom = 400
        screen.blit(player_surf, (player_rect))
        player_animation()
        player.draw(screen)
        player.update()
        # obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        #collision
        game_active = collision(player_rect, obstacle_rect_list)
    else:
        game_over = test_font.render('Game Over', True, ('darkred'))
        game_over_rectangle = game_over.get_rect(center = (400, 50))
        play_again = test_font.render('Play Again ?', True, ('brown3'))
        play_again_rect = play_again.get_rect(center = (400, 300))
        obstacle_rect_list.clear()
        player_rect.midbottom = (100, 400)
        player_gravity = 0  
        
        screen.fill((0, 0, 0))
        screen.blit(player_big, (player_big_rectangle))
        screen.blit(game_over, (game_over_rectangle))
        screen.blit(play_again, play_again_rect)
        
        
    
    
        
    pygame.display.update() #update screen
    clock.tick(60) #fps 60 