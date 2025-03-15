import pygame
from sys import exit
from random import randint
def display_score():
    current_score = pygame.time.get_ticks() // 1000 - start_time // 1000 #score
    score_surf = test_font.render(f'Score: {current_score}', False, ('Red')) #score
    score_rectangle = score_surf.get_rect(center = (400, 500)) #score #update screen
    screen.blit(score_surf, score_rectangle) #score #update screen
    
def obstacle_movement(obstacle_list):
    if obstacle_rect_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x += 1
            # obstacle_rect.inflate_ip(-50,-50)
            
            screen.blit(character_surf ,obstacle_rect)
        return obstacle_list
    else : return []


    

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

#text           
test_surf = pygame.Surface((100, 100)) #surface
test_ground = ground.get_rect() #achtergrond
test_ground.topleft = (0, 400) #achtergrond
test_text = test_font.render('My game', True, (255, 140, 0, 255))#text     "firebrick3": (205, 38, 38, 255),
test_text_rectangle = test_text.get_rect(center = (400, 50)) #text

character_surf = pygame.image.load('graphics/3/3_enemies_1_attack_000.png').convert_alpha()#character
character_surf = pygame.transform.scale(character_surf, (150, 150)) #character
character_rectangle = character_surf.get_rect(bottomleft = (0, 400))
character_rectangle_scaled = pygame.transform.scale(character_surf, (90,90))#character movement improvement  scaled ======== hitbox
character_rectangle_scaled = character_rectangle_scaled.get_rect(bottomleft = (0,400))
# def __init__(self):
#         #call the parent class constructor
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load("graphics/3/3_enemies_1_attack_000.png").convert_alpha()
#         self.rect = self.image.get_rect()
#         self.rect.inflate_ip(-110,-54)            #resize hitbox to match actual image size without background
#         pygame.draw.rect(self.image,RED,self.rect)     #draw hitbox for debugging purpose
    
obstacle_rect_list = []
#collision box
player_surf = pygame.image.load('graphics/5/5_enemies_1_attack_000.png').convert_alpha()
player_surf = pygame.transform.scale(player_surf, (150, 150))
player_surf = pygame.transform.flip(player_surf, True, False)
player_surf_rectangle = player_surf.get_rect(bottomright = (800, 400))
player_surf_rectangle_scaled = pygame.transform.scale(player_surf, (90, 90))#character movement improvement
player_surf_rectangle_scaled = player_surf_rectangle_scaled.get_rect(bottomright = (800,400))
player_gravity = 0

player_big = pygame.transform.scale(player_surf, (275, 275))
player_big_rectangle = player_big.get_rect(midbottom = (350, 580))

obstacle_timer = pygame.USEREVENT + 1 #timer   userevent always +1
pygame.time.set_timer(obstacle_timer, 900)


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if game_active:        
            if event.type == pygame.MOUSEBUTTONDOWN and player_surf_rectangle.collidepoint(event.pos):
                if player_surf_rectangle.bottom >= 50:
                    print('click-jump')
                    player_gravity = -30
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_surf_rectangle.bottom >= 50:
                        print('jump')
                        player_gravity = -10
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_rect.collidepoint(event.pos):
                    game_active = True
                    character_rectangle.x = 0
                    player_surf_rectangle.x = 600
                    character_rectangle_scaled.x = 0
                    player_surf_rectangle_scaled.x = 600
                    start_time = pygame.time.get_ticks()
                    
        if event.type == obstacle_timer and game_active:
            obstacle_rect_list.append(character_surf.get_rect(bottomleft = (randint(-800,-200), 400)))
            
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

        
        character_rectangle.x += 2 
        character_rectangle_scaled.x += 2 #movenment
        if character_rectangle.right > 800:
            character_rectangle.left = 0
            character_rectangle_scaled.left = 0 #reset loop 
        screen.blit(character_surf, (character_rectangle))
        
        # player_surf_rectangle.x -= 2
        # player_surf_rectangle_scaled.x -= 2
        # if player_surf_rectangle.left < 0:
        #     player_surf_rectangle.right = 800
        #     player_surf_rectangle_scaled.right = 800
            
        player_gravity += 0.5
        player_surf_rectangle.y += player_gravity
        player_surf_rectangle_scaled.y += player_gravity
        if player_surf_rectangle.bottom >= 400: player_surf_rectangle.bottom = 400
        if player_surf_rectangle_scaled.bottom >= 400: player_surf_rectangle_scaled.bottom = 400
        screen.blit(player_surf, (player_surf_rectangle))
        
        # obstacle movement
        obstacle_rect_list =  obstacle_movement(obstacle_rect_list)
        
        #collision
        if player_surf_rectangle_scaled.colliderect(character_rectangle_scaled):
            game_active = False
            print('collision')  
    else:
        game_over = test_font.render('Game Over', True, ('darkred'))
        game_over_rectangle = game_over.get_rect(center = (400, 50))
        play_again = test_font.render('Play Again ?', True, ('brown3'))
        play_again_rect = play_again.get_rect(center = (400, 300))
       
        screen.fill((0, 0, 0))
        screen.blit(player_big, (player_big_rectangle))
        screen.blit(game_over, (game_over_rectangle))
        screen.blit(play_again, play_again_rect)
        
        
    
    
        
    pygame.display.update() #update screen
    clock.tick(60) #fps 60   
    # keys = pygame.key.get_pressed() #key press    
    # if keys[pygame.K_SPACE]: #space bar
    #     print('jump')
   # player_surf_rectangle.collidepoint(pygame.mouse.get_pos()) #mouse and colliion on point
   # if player_surf_rectangle.collidepoint(pygame.mouse.get_pos()):
   #     player_surf_rectangle.x = 0
   #     print("collision")
   #     print(pygame.mouse.get_pressed())
    # gravity += value     player.y += gravity
    
   
    
    # sprite = 2D img set (stop motion)
    # sprite sheet = collection of sprites
    # sprite strip = row of sprites in sprite sheet
    # sprite strip animation = animate sprite strip (loop)
    # sprite strip frame = single sprite in sprite strip        
    # sprite strip frame animation = animate sprite strip frame (loop)
    # sprite strip frame animation = animate sprite strip frame (once) 