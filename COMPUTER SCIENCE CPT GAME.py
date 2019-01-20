import pygame,sys
from pygame.locals import *
import math
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# FONTS
TITLE_FONT = pygame.font.SysFont("", 40)
WRITING_FONT = pygame.font.SysFont("", 20)
# Load Images
shuttle = pygame.image.load("space_shuttle_two.png")
shuttle = pygame.transform.scale(shuttle, (50, 50))  # Change the image size
night = pygame.image.load("starry_night.png")
night = pygame.transform.scale(night, (800, 600))      # Change the image size
moon_pic = pygame.image.load("mon_landing.png")
moon_pic = pygame.transform.scale(moon_pic, (800, 600))     # Change the image size
left_arrow = pygame.image.load("left_arrow.png")
left_arrow = pygame.transform.scale(left_arrow, (30, 30))      # Change the image size
right_arrow = pygame.image.load("right_arrow.png")
position_arrow = pygame.image.load("positionarrow.png")
position_arrow = pygame.transform.scale(position_arrow, (20, 20))   # Change the image size
position_arrowright = pygame.transform.rotate(position_arrow, -90)  # Rotate the image
position_arrowleft = pygame.transform.rotate(position_arrow, 90)    # Rotate the imageg
right_arrow = pygame.transform.scale(right_arrow, (30, 30))     # Change the image size
up_arrow = pygame.image.load("up_arrow.png")
up_arrow = pygame.transform.scale(up_arrow, (30, 30))   # Change the image size
pause_image = pygame.image.load("pause_image.png")
pause_image = pygame.transform.scale(pause_image, (800, 600))   # Change the image size
arrow_image = pygame.image.load("arrow.png")
arrow_image = pygame.transform.scale(arrow_image, (50, 50))     # Change the image size
explosion_image = pygame.image.load("explosion.png")
explosion_image = pygame.transform.scale(explosion_image, (50, 50))     # Change the image size
flames_image = pygame.image.load("flames.png")                      # Rotate the image
flames_image = pygame.transform.scale(flames_image, (50, 50))       # Change the image size
rarrow = pygame.image.load("rarrow.png")
rarrow = pygame.transform.scale(rarrow, (50, 50))               # Change the image size
menu = pygame.image.load("menu.png")
menu = pygame.transform.scale(menu, (50, 50))               # Change the image size

# ---------------- INSTRUCTIONS SCREEN ------------------
def show_instructions():
    global TITLE_FONT
    title = TITLE_FONT.render("INSTRUCTIONS", True, (255, 255, 255))  # Load Font
    word_instruct = TITLE_FONT.render("Use sipy -m pip install -U pygame --userde arrow keys to tilt the ship", True, (255, 255, 255))
    word_instruct_two = TITLE_FONT.render("Use the Up arrow key to apply thrust", True, (255, 255, 255))
    word_instruct_three = TITLE_FONT.render("The shuttle must land on the landing zone/green", True, (255, 255, 255))
    word_instruct_six = TITLE_FONT.render("line.", True, (255, 255, 255))
    word_instruct_five = TITLE_FONT.render("Land the ship softly and upright or it will crash.", True, (255, 255, 255))
    word_instruct_four = TITLE_FONT.render("DO NOT HIT THE MOUNTAIN!!", True, (255, 255, 255))
    arrow_rect = pygame.Rect(50, 500, 50, 50) # A rect for the arrow
    while True:
        clock.tick(60)
        #event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:                 # If the ESC key is pressed,
                if event.key == K_ESCAPE:                       # Return to the previous screen
                    return
            elif event.type == MOUSEBUTTONDOWN:         # If the arrow image is clicked,
                if arrow_rect.collidepoint(event.pos):          # Return to the previous screen
                    return
        #Game state changes
        screen.fill((255, 0, 0))
        screen.blit(night, (0, 0))                       # Load the image
        screen.blit(title, (300, 45))                   # Load the image
        screen.blit(left_arrow, (351, 145))              # Load the image
        screen.blit(right_arrow, (390, 145))             # Load the image
        screen.blit(up_arrow, (375, 220))                # Load the image
        screen.blit(word_instruct, (100, 100))           # Load the image
        screen.blit(word_instruct_two, (100, 170))       # Load the image
        screen.blit(word_instruct_three, (100, 260))     # Load the image
        screen.blit(word_instruct_six, (100, 290))      # Load the image
        screen.blit(word_instruct_five, (100, 360))     # Load the image
        screen.blit(word_instruct_four, (100, 440))     # Load the image
        screen.blit(arrow_image, arrow_rect)            # Load the image on the rect
        pygame.draw.rect(screen, (0, 255, 0), (180, 310, 50, 5))    # Draw the rectangle on the screen
        #Update display
        pygame.display.update()                         # Update the Display
# ---------------- LEVEL SELECT ------------------
def show_level_select():
    global TITLE_FONT
    title = TITLE_FONT.render("CHOOSE A LEVEL", True, (255, 255, 255))     # Write on the screen
    level_one = TITLE_FONT.render(" Level 1 ", True, (0, 0, 0))            # Write on the screen
    level_two = TITLE_FONT.render(" Level 2 ", True, (0, 0, 0))            # Write on the screen
    level_three = TITLE_FONT.render(" Level 3 ", True, (0, 0, 0))          # Write on the screen
    level_one_rect = pygame.Rect(300, 250, level_one.get_width(), level_one.get_height())   # Create a rect with the height and width of the words
    level_two_rect = pygame.Rect(300, 300, level_two.get_width(), level_two.get_height())   # Create a rect with the height and width of the words
    level_three_rect = pygame.Rect(300, 350, level_three.get_width(), level_three.get_height())  # Create a rect width the height and width of the words
    arrow_rect = pygame.Rect(50, 500, 50, 50)   # Create a rect
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:             # If the ESC key is pressed,
                if event.key == K_ESCAPE:                   # Return to the previous screen
                    return
            elif event.type == MOUSEBUTTONDOWN:                 # If clicked,
                if level_one_rect.collidepoint(event.pos):              # Show the first level
                    show_level_one()
                elif level_two_rect.collidepoint(event.pos):            # Show the second level
                    show_level_two()
                elif level_three_rect.collidepoint(event.pos):          # Show the third level
                    show_level_three()
                elif arrow_rect.collidepoint(event.pos):                # Return to the previous screen
                    return
        screen.fill((0, 0, 0))
        screen.blit(moon_pic, (0, 0))                                   # Load the image
        screen.blit(title, (250, 100))                                  # Load the image
        pygame.draw.rect(screen, (255, 255, 255), level_one_rect)       # Draw a rectangle in the position of the rect
        pygame.draw.rect(screen, (255, 255, 255), level_two_rect)       # Draw a rectangle in the position of the rect
        pygame.draw.rect(screen, (255, 255, 255), level_three_rect)     # Draw a rectangle in the position of the rect
        screen.blit(level_one, level_one_rect)                          # Blit the text to the rect
        screen.blit(level_two, level_two_rect)                          # Blit the text to the rect
        screen.blit(level_three, level_three_rect)                      # Blit the text to the rect
        screen.blit(arrow_image, arrow_rect)                            # Blit the image to the rect
        #Update display
        pygame.display.update()             # Update the image
# ---------------- PAUSE SCREEN ------------------
def show_pause():
    global TITLE_FONT
    title = TITLE_FONT.render("PAUSE", True, (255, 255, 255))               # Write on screen
    level_select = TITLE_FONT.render("Level Select", True, (0, 0, 0))       # Write on screen
    resume = TITLE_FONT.render("Resume", True, (0, 0, 0))                   # Write on screen
    menu = TITLE_FONT.render("Menu", True, (0, 0, 0))                       # Write on screen
    instructions_one = TITLE_FONT.render("Instructions", True, (0, 0, 0))       # Write on screen
    quit = TITLE_FONT.render("Quit", True, (0, 0, 0))                       # Write on screen
    level_rect = pygame.Rect(200, 250, level_select.get_width(), level_select.get_height())     # Write on screen
    instructions_rect = pygame.Rect(450, 150, instructions_one.get_width(), instructions_one.get_height())  # Create a rect with the height and width of the words
    quit_rect = pygame.Rect(450, 250, quit.get_width(), quit.get_height()) # Create a rect with the height and width of the words
    resume_rect = pygame.Rect(200, 150, resume.get_width(), resume.get_height())    # Create a rect with the height and width of the words
    menu_rect = pygame.Rect(200, 350, menu.get_width(), menu.get_height())  # Create a rect with the height and width of the words
    while True:
        clock.tick(60)
        #event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if level_rect.collidepoint(event.pos):          # If clicked,
                    show_level_select()                                 # Go to level one
                if instructions_rect.collidepoint(event.pos):
                    show_instructions()                                 # Go to the instructions page
                if quit_rect.collidepoint(event.pos):
                    pygame.quit()                                       # Quit the game
                    sys.exit()
                if menu_rect.collidepoint(event.pos):
                    show_menu()                                         # Return to the main menu
                if resume_rect.collidepoint(event.pos):
                    return                                              # Go back to previous screen
        #Game state changes
        screen.fill((255, 0, 0))
        screen.blit(pause_image, (0, 0))                                # Load the image to the screen
        pygame.draw.rect(screen, (255, 255, 255), (level_rect))         # Draw a rectangle in the position of the rect
        pygame.draw.rect(screen, (255, 255, 255), (resume_rect))    # Draw a rectangle in the position of the rect
        pygame.draw.rect(screen, (255, 255, 255), (instructions_rect))  # Draw a rectangle in the position of the rect
        pygame.draw.rect(screen, (255, 255, 255), (quit_rect))  # Draw a rectangle in the position of the rect
        pygame.draw.rect(screen, (255, 255, 255), (menu_rect))  # Draw a rectangle in the position of the rect
        screen.blit(title, (350, 50))   # Load the text onto the screen
        screen.blit(level_select, level_rect)       # Blit the text to the rect
        screen.blit(resume, resume_rect)    # Blit the text to the rect
        screen.blit(menu, menu_rect)        # Blit the text to the rect
        screen.blit(instructions_one, instructions_rect)         # Blit the text to the rect
        screen.blit(quit, quit_rect)                # Blit the text to the rect
        #Update display
        pygame.display.update()     # Update the Display
# ---------------- VICTORY SCREEN ------------------
def show_victory_screen():
    global TITLE_FONT               # Draw the variable
    global WRITING_FONT             # Draw the variable
    title = TITLE_FONT.render("CONGRATS YOU LANDED SAFELY!", True, (255, 255, 255))     # Add text
    next_level = WRITING_FONT.render("Next Level", True, (255, 255, 255))           # Text
    arrow_rect = pygame.Rect(700, 500, 50, 50)                     # Create a rect
    menu_rect = pygame.Rect(100, 500, 50, 50)                       # Create a rect
    menu_text = WRITING_FONT.render("Menu", True, (255, 255, 255))  # Text
    while True:
        clock.tick(60)

        #event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:           # if clicked,
                if arrow_rect.collidepoint(event.pos):
                    show_level_two()                            # Go to level two
                if menu_rect.collidepoint(event.pos):
                    show_menu()                                 # Go to the main menu

        screen.blit(rarrow, arrow_rect)             # add the image to the rect
        screen.blit(menu, menu_rect)                # add the image to the rect
        screen.blit(menu_text, (103, 480))          # add the text to the screen
        screen.blit(next_level, (695, 490))         # add the text to the screen
        screen.blit(title, (200, 200))              # add the text to the screen
        pygame.display.update()     # Update the Display
# ---------------- DEATH SCREEN ----------------------
def show_end_screen():
    global TITLE_FONT
    title = TITLE_FONT.render("YOU DIED!", True, (255, 255, 255))       # Text
    next_level = WRITING_FONT.render("Choose Level", True, (255, 255, 255))     # Text
    arrow_rect = pygame.Rect(700, 500, 50, 50)              # Create a rect
    menu_rect = pygame.Rect(100, 500, 50, 50)                   # Create a rect
    menu_text = WRITING_FONT.render("Menu", True, (255, 255, 255))          # Text
    while True:
        clock.tick(60)
        #event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:               # if clicked,
                if arrow_rect.collidepoint(event.pos):
                    show_level_select()                             # Show Level Select screen
                if menu_rect.collidepoint(event.pos):
                    show_menu()                                     # Go to the menu screen
        screen.blit(title, (300, 188))          # add the text to the screen
        screen.blit(rarrow, arrow_rect)         # add the image to the rect
        screen.blit(menu, menu_rect)            # add the image to the rect
        screen.blit(menu_text, (103, 480))      # add the text to the screen
        screen.blit(next_level, (695, 490))     # add the text to the screen
        pygame.display.update()     # Update the image

# ---------------- LEVEL ONE ------------------
def show_level_one():
    global shuttle  # Draw the image
    vel_x = 0   # X velocity variable
    vel_y = 0   # Y velocity variable
    dx = 0      # Delta x variable
    dy = 0      # Delta y variable
    x_pos = 0    # x position of the shuttle
    y_pos = 50     # y position of the shuttle
    '''
    x2 = x/2
    y2 = y
    x3 = x * 1.25
    y3 = x* 0.65
    '''
    fuel = 1000         # amount of fuel
    delta_fuel = 0      # Delta fuel variable
    angle = 0           # starting angle
    delta_angle = 0     # delta angle variable
    thrust = 0.05       # Thrust variable
    gravity = 0.008     # Gravity variable
    fuel_text = WRITING_FONT.render("Fuel = ", True, (255, 255, 255))       # Text
    velocity = WRITING_FONT.render(('Velocity = '), True, (255, 255, 255))      # Text
    angle_text = WRITING_FONT.render(('Angle = '), True, (255, 255, 255))   # Text
    flames = False      # Flames Variable
    pause = WRITING_FONT.render("Press ESC to pause.", True, (255, 255, 255)) # Text
    landing_rect = pygame.Rect(278, 521, 51, 10)        # Create a rect
    player_rect = pygame.Rect(x_pos, y_pos, 50, 50)     # Create a rect
    mountain_points = [     # Points for the terrain
        (0,450),(35, 485), (70, 459), (95, 433), (110, 417), (139, 427), (194, 401), (217, 367), (232, 410), (251, 453), (270, 499),
        (354, 512), (395, 487), (441, 467), (490, 456), (474, 469), (550, 405), (584, 372),(606, 353),(633, 334), (674, 344), (718, 369), (770, 398)]

    while True:
        clock.tick(60)
        #event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if player_rect.colliderect(landing_rect):   # if the user lands on the landing spot,
                show_victory_screen()                           # Show the victory screen
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:               # If the user hits the ESC key.
                    show_pause()                                # show the pause menu
                if fuel > 0:             # When the fuel is greater than 0,
                    if event.key == K_UP:                       # and the UP key is hit,
                        dx = thrust*math.sin(-angle*(math.pi/180))  # Delta X is equal to thrust * sin of angle (TRIG)
                        dy = thrust*math.cos(-angle*(math.pi/180))  # Delta Y is equal to thrust * sin of angle (TRIG)
                        delta_fuel = 1                          # Change over fuel is 1
                        flames = False                           # Flames are on
                if angle < 90:          # When is angle is greater than 90,
                    if event.key == K_LEFT:     # and the left arrow is hit,
                        delta_angle = 1             # change over the angle is 1
                if angle > -90:         # When the angle is smaller than -90,
                    if event.key == K_RIGHT:    # and the right arrow key is hit,
                        delta_angle = -1            # change in the angle is -1
            if event.type == KEYUP:     # When the player lets go of a key,
                if event.key == K_UP:       # Up key is let go,
                    delta_fuel = 0              # Change in the fuel is 0
                    dy = 0                      # Change in the y is 0
                    dx = 0                      # Change in the x is 0
                    flames = False              # Flames are now turned off
                if event.key == K_LEFT or event.key == K_RIGHT:   # Either the left key or right key is let go,
                    delta_angle = 0                                     # Change in the angle is now 0

        fuel -= delta_fuel      # fuel is = to fuel subtracted from delta
        angle += delta_angle    # angle is = to angle added from delta
        vel_x += dx             # velocity of x is = to velocity  added from delta
        vel_y -= dy             # velocity of y is = to velocity subtracted from delta
        vel_y += gravity        # velocity of y is = to velocity added from gravity
        x_pos += vel_x          # the x position is = to x position added from velocity of x
        y_pos += vel_y          # y position is = to the y position added  from the velocity of y
        player_rect.x = x_pos      # The x coordinate of the rect is equal to the x coordinate of shuttle
        player_rect.y = y_pos      # The y coordinate of the rect is equal to the x coordinate of shuttle

        if fuel <= 0:           # When the fuel is lower or equal to zero,
            fuel = 0                    # fuel is 0
            dy = 0                      # Change over y is 0
        if angle <= -90:        # when the angle is lower or at -90,
            delta_angle = 0         # change over the angle is 0
        if angle >= 90:         # when the angle is greater or at 90,
            delta_angle = 0         # change over the angle is 0


        #Game state changes
        screen.blit(night, (0, 0))
        pygame.draw.polygon(screen, (160, 160, 160), [(0,600), (1, 452), (37, 487), (111, 416), (172, 436), (215, 367), (278, 521)])  # Draw Mountain
        pygame.draw.polygon(screen, (160, 160, 160), [(329, 521), (441, 467), (477, 463), (638, 324), (798, 416)])  # Draw Mountain
        pygame.draw.polygon(screen, (160, 160, 160), [(2, 599), (274, 521), (330, 521), (798, 416), (799, 599)])# Draw Mountain


        if x_pos > 800:     # If the x position of the shuttle is greater than 800,
            screen.blit(position_arrowright, (770, y_pos))      # load the arrow picture
        elif x_pos < -50:   # If the x position of the shuttle is smaller than -50,
            screen.blit(position_arrowleft, (10, y_pos))        # load the arrow picture
        elif y_pos < -50:   # If the y position of the shuttle is smaller than -50,
            screen.blit(position_arrow, (x_pos, 10))            # load the arrow picture
        elif y_pos > 600:   # If the y position of the shuttle is greater than 600,
            show_end_screen()                                   # show the end screen


        for point in mountain_points:           # for any points in the mountain,
            if player_rect.collidepoint(point):     # if the player hits the point
                screen.blit(explosion_image,player_rect) # Load the explosion image over the player
                show_end_screen()                        # show the death screen


        fuel_level = WRITING_FONT.render(str(fuel), True, (255, 255, 255))  # Text
        velocity_level = WRITING_FONT.render(str(vel_y), True, (255, 255, 255)) # Text
        angle_level = WRITING_FONT.render(str(angle), True, (255, 255, 255))        # Text

        shuttle_neutral = pygame.transform.rotate(shuttle, angle)   # Add the rotation to the shuttle
        screen.blit(shuttle_neutral, player_rect)       # Add the rotation to the rect
        screen.blit(pause, (650, 0))                    # add the text to the screen
        screen.blit(fuel_text, (0, 0))                  # add the text to the screen
        screen.blit(fuel_level, (50, 0))                # add the text to the screen
        screen.blit((velocity), (0, 50))                # add the text to the screen
        screen.blit((velocity_level),(70, 50))          # add the text to the screen
        screen.blit((angle_text),(0, 100))              # add the text to the screen
        screen.blit((angle_level),(70, 100))            # add the text to the screen
        pygame.draw.rect(screen, (0, 255, 0), landing_rect)         # Draw a rectangle in the position of the rect

        if flames:      # If flames are true,
            '''
            pygame.draw.polygon(screen, [255, 109, 14],
                     [(x_pos * 1.5, y_pos ),
                      ((x_pos * 1.5)* 1.5 , y_pos),
                      (((x_pos * 1.5)+(x_pos* 1.5))/2, 2*y_pos * 1.5)])
            '''
            screen.blit(flames_image, (x_pos + 8, y_pos + 25))  # Blit the image in the location specified

        if player_rect.colliderect(landing_rect) and ((angle < 8 and angle > -8) and (vel_y < 0.8)):    # if the player hits the rect with the angles between 8 and -8 and the velocity under 0.8,
            show_victory_screen()                                                                           # show the victory screen
        elif player_rect.colliderect(landing_rect): # or else,
            screen.blit(explosion_image, player_rect)         # blit the explosion image to the player,
            show_end_screen()                                   # then show the end screen

        #Update display
        pygame.display.update()     # Update the screen
# ---------------- Level 2 ---------------
def show_level_two():
    global shuttle
    vel_x = 0   # X velocity variable
    vel_y = 0   # Y velocity variable
    dx = 0      # Delta x variable
    dy = 0      # Delta y variable
    x_pos = 10    # x position of the shuttle
    y_pos = 400     # y position of the shuttle
    fuel = 1000         # amount of fuel
    delta_fuel = 0      # Delta fuel variable
    angle = 0           # starting angle
    delta_angle = 0     # delta angle variable
    thrust = 0.05       # Thrust variable
    gravity = 0.008     # Gravity variable
    fuel_text = WRITING_FONT.render("Fuel = ", True, (255, 255, 255))       # Text

    velocity = WRITING_FONT.render(('Velocity = '), True, (255, 255, 255))      # Text
    angle_text = WRITING_FONT.render(('Angle = '), True, (255, 255, 255))   # Text
    flames = False      # Flames Variable
    pause = WRITING_FONT.render("Press ESC to pause.", True, (255, 255, 255)) # Text
    mountain_points = [ # Points for the terrain
        (425, 600), (0, 531), (54, 531), (85, 497), (119, 461), (143, 425), (173, 377), (202, 336), (237, 318), (282, 293), (303, 332), (331, 398),
        (368, 460), (394, 484), (425, 512), (456, 534), (486, 530), (512, 533), (531, 531), (545, 494), (556, 452), (571, 411),(575, 392),
        (609, 409), (656, 432), (673, 474), (697, 516)
    ]
    player_rect = pygame.Rect(x_pos, y_pos, 50, 50)
    landing_rect = pygame.Rect(705, 532, 50, 10)
    while True:
        clock.tick(60)
        #event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if player_rect.colliderect(landing_rect):   # if the user lands on the landing spot,
                show_victory_screen()                           # Show the victory screen
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:               # If the user hits the ESC key.
                    show_pause()                                # show the pause menu
                if fuel > 0:             # When the fuel is greater than 0,
                    if event.key == K_UP:                       # and the UP key is hit,
                        dx = thrust*math.sin(-angle*(math.pi/180))  # Delta X is equal to thrust * sin of angle (TRIG)
                        dy = thrust*math.cos(-angle*(math.pi/180))  # Delta Y is equal to thrust * sin of angle (TRIG)
                        delta_fuel = 1                          # Change over fuel is 1
                        flames = False                           # Flames are on
                if angle < 90:          # When is angle is greater than 90,
                    if event.key == K_LEFT:     # and the left arrow is hit,
                        delta_angle = 1             # change over the angle is 1
                if angle > -90:         # When the angle is smaller than -90,
                    if event.key == K_RIGHT:    # and the right arrow key is hit,
                        delta_angle = -1            # change in the angle is -1
            if event.type == KEYUP:     # When the player lets go of a key,
                if event.key == K_UP:       # Up key is let go,
                    delta_fuel = 0              # Change in the fuel is 0
                    dy = 0                      # Change in the y is 0
                    dx = 0                      # Change in the x is 0
                    flames = False              # Flames are now turned off
                if event.key == K_LEFT or event.key == K_RIGHT:   # Either the left key or right key is let go,
                    delta_angle = 0                                     # Change in the angle is now 0

        fuel -= delta_fuel      # fuel is = to fuel subtracted from delta
        angle += delta_angle    # angle is = to angle added from delta
        vel_x += dx             # velocity of x is = to velocity  added from delta
        vel_y -= dy             # velocity of y is = to velocity subtracted from delta
        vel_y += gravity        # velocity of y is = to velocity added from gravity
        x_pos += vel_x          # the x position is = to x position added from velocity of x
        y_pos += vel_y          # y position is = to the y position added  from the velocity of y
        player_rect.x = x_pos      # The x coordinate of the rect is equal to the x coordinate of shuttle
        player_rect.y = y_pos      # The y coordinate of the rect is equal to the x coordinate of shuttle

        if fuel <= 0:           # When the fuel is lower or equal to zero,
            fuel = 0                    # fuel is 0
            dy = 0                      # Change over y is 0
        if angle <= -90:        # when the angle is lower or at -90,
            delta_angle = 0         # change over the angle is 0
        if angle >= 90:         # when the angle is greater or at 90,
            delta_angle = 0         # change over the angle is 0

        screen.fill((0, 0, 0))
        screen.blit(night, (0, 0))
        pygame.draw.polygon(screen, (160, 160, 160), [(0, 530), (55, 529), (129, 445),(200, 334),(281, 291), (309, 347), (345, 438), (401, 488), (457, 544)]) # Draw terrain
        pygame.draw.polygon(screen, (160, 160, 160), [(457, 544),(531, 532), (574, 390), (656, 432),(703, 532)])  # Draw Terrain
        pygame.draw.rect(screen, (160, 160, 160), (0 , 532 , 800, 200))  # Draw terrain

        if x_pos > 800:     # If the x position of the shuttle is greater than 800,
            screen.blit(position_arrowright, (770, y_pos))      # load the arrow picture
        elif x_pos < -50:   # If the x position of the shuttle is smaller than -50,
            screen.blit(position_arrowleft, (10, y_pos))        # load the arrow picture
        elif y_pos < -50:   # If the y position of the shuttle is smaller than -50,
            screen.blit(position_arrow, (x_pos, 10))            # load the arrow picture
        elif y_pos > 600:   # If the y position of the shuttle is greater than 600,
            show_end_screen()                                   # show the end screen

        for point in mountain_points:           # for any points in the mountain,
            if player_rect.collidepoint(point):     # if the player hits the point
                screen.blit(explosion_image,player_rect) # Load the explosion image over the player
                show_end_screen()                        # show the death screen

        fuel_level = WRITING_FONT.render(str(fuel), True, (255, 255, 255))  # Text
        velocity_level = WRITING_FONT.render(str(vel_y), True, (255, 255, 255)) # Text
        angle_level = WRITING_FONT.render(str(angle), True, (255, 255, 255))        # Text

        shuttle_neutral = pygame.transform.rotate(shuttle, angle)   # Add the rotation to the shuttle
        screen.blit(shuttle_neutral, player_rect)       # Add the rotation to the rect
        screen.blit(pause, (650, 0))                    # add the text to the screen
        screen.blit(fuel_text, (0, 0))                  # add the text to the screen
        screen.blit(fuel_level, (50, 0))                # add the text to the screen
        screen.blit(velocity, (0, 50))                # add the text to the screen
        screen.blit(velocity_level, (70, 50))          # add the text to the screen
        screen.blit(angle_text, (0, 100))              # add the text to the screen
        screen.blit(angle_level, (70, 100))            # add the text to the screen
        pygame.draw.rect(screen, (0, 255, 0), landing_rect)         # Draw a rectangle in the position of the rect

        pygame.draw.rect(screen, (0, 255, 0), (705 , 532 , 100, 0))
        if flames:      # If flames are true,
            '''
            pygame.draw.polygon(screen, [255, 109, 14],
                     [(x_pos * 1.5, y_pos ),
                      ((x_pos * 1.5)* 1.5 , y_pos),
                      (((x_pos * 1.5)+(x_pos* 1.5))/2, 2*y_pos * 1.5)])
            '''
            screen.blit(flames_image, (x_pos + 8, y_pos + 25))  # Blit the image in the location specified

        if player_rect.colliderect(landing_rect) and ((angle < 8 and angle > -8) and (vel_y < 0.8)):    # if the player hits the rect with the angles between 8 and -8 and the velocity under 0.8,
            show_victory_screen()                                                                           # show the victory screen
        elif player_rect.colliderect(landing_rect): # or else,
            screen.blit(explosion_image, player_rect)         # blit the explosion image to the player,
            show_end_screen()                                   # then show the end screen

        # Update display
        pygame.display.update()     # Update the screen
# ---------------- LEVEL THREE --------------------
def show_level_three():
    global shuttle
    vel_x = 0   # X velocity variable
    vel_y = 0   # Y velocity variable
    dx = 0      # Delta x variable
    dy = 0      # Delta y variable
    x_pos = 485    # x position of the shuttle
    y_pos = 82     # y position of the shuttle
    fuel = 1000         # Amount of fuel
    delta_fuel = 0      # Delta fuel variable
    angle = 0           # starting angle
    delta_angle = 0     # delta angle variable
    thrust = 0.05       # Thrust variable
    gravity = 0.008     # Gravity variable
    fuel_text = WRITING_FONT.render("Fuel = ", True, (255, 255, 255))       # Text
    velocity = WRITING_FONT.render('Velocity = ', True, (255, 255, 255))      # Text
    angle_text = WRITING_FONT.render('Angle = ', True, (255, 255, 255))   # Text
    flames = False      # Flames Variable
    pause = WRITING_FONT.render("Press ESC to pause.", True, (255, 255, 255))  # Text
    mountain_points = [  # Points for the terrain
        (627, 6), (610, 33), (584, 69),(570, 85), (552, 120),(526, 149), (487, 152), (437, 154), (406, 152),(375, 152),
        (362, 185), (351, 223), (341, 253), (333, 282),(317, 328),(353, 334), (381, 339),(420, 343), (467, 351), (512, 356),
        (549, 362), (589, 367), (626, 372), (660, 376), (688, 381),(728, 388), (754, 393), (797, 396), (0, 286), (20, 307),
        (44, 331),(76, 365), (99, 391), (119, 413), (143, 432), (182, 447), (218, 462), (260, 479), (290, 490), (340, 504),
        (379, 512), (414, 514), (457, 526), (492, 530), (525, 534), (577, 531), (607, 533), (652, 532), (678, 531)
                    ]
    player_rect = pygame.Rect(485, 82, 50, 50)
    landing_rect = pygame.Rect(705, 532, 100, 50)
    while True:
        clock.tick(60)
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if player_rect.colliderect(landing_rect):   # if the user lands on the landing spot,
                show_victory_screen()                           # Show the victory screen
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:               # If the user hits the ESC key.
                    show_pause()                                # show the pause menu
                if fuel > 0:             # When the fuel is greater than 0,
                    if event.key == K_UP:                       # and the UP key is hit,
                        dx = thrust*math.sin(-angle*(math.pi/180))  # Delta X is equal to thrust * sin of angle (TRIG)
                        dy = thrust*math.cos(-angle*(math.pi/180))  # Delta Y is equal to thrust * sin of angle (TRIG)
                        delta_fuel = 1                          # Change over fuel is 1
                        flames = False                           # Flames are on
                if angle < 90:          # When is angle is greater than 90,
                    if event.key == K_LEFT:     # and the left arrow is hit,
                        delta_angle = 1             # change over the angle is 1
                if angle > -90:         # When the angle is smaller than -90,
                    if event.key == K_RIGHT:    # and the right arrow key is hit,
                        delta_angle = -1            # change in the angle is -1
            if event.type == KEYUP:     # When the player lets go of a key,
                if event.key == K_UP:       # Up key is let go,
                    delta_fuel = 0              # Change in the fuel is 0
                    dy = 0                      # Change in the y is 0
                    dx = 0                      # Change in the x is 0
                    flames = False              # Flames are now turned off
                if event.key == K_LEFT or event.key == K_RIGHT:   # Either the left key or right key is let go,
                    delta_angle = 0                                     # Change in the angle is now 0

        fuel -= delta_fuel      # fuel is = to fuel subtracted from delta
        angle += delta_angle    # angle is = to angle added from delta
        vel_x += dx             # velocity of x is = to velocity  added from delta
        vel_y -= dy             # velocity of y is = to velocity subtracted from delta
        vel_y += gravity        # velocity of y is = to velocity added from gravity
        x_pos += vel_x          # the x position is = to x position added from velocity of x
        y_pos += vel_y          # y position is = to the y position added  from the velocity of y
        player_rect.x = x_pos      # The x coordinate of the rect is equal to the x coordinate of shuttle
        player_rect.y = y_pos      # The y coordinate of the rect is equal to the x coordinate of shuttle

        if fuel <= 0:           # When the fuel is lower or equal to zero,
            fuel = 0                    # fuel is 0
            dy = 0                      # Change over y is 0
        if angle <= -90:        # when the angle is lower or at -90,
            delta_angle = 0         # change over the angle is 0
        if angle >= 90:         # when the angle is greater or at 90,
            delta_angle = 0         # change over the angle is 0

        screen.fill((0, 0, 0))
        screen.blit(night, (0, 0))

        pygame.draw.polygon(screen, (160, 160, 160), [(0, 596),(0, 286), (138, 430), (315, 500),(534, 536),(687, 530), (800, 534)])
        pygame.draw.rect(screen, (160, 160, 160), (0 , 532 , 800, 200))
        pygame.draw.polygon(screen, (160, 160, 160), [(316, 327),(375, 150), (527, 148), (627, 4), (798, 2),(800, 396)])
        pygame.draw.rect(screen, (0, 255, 0), (705 , 532 , 50, 10))
        if x_pos > 800:     # If the x position of the shuttle is greater than 800,
            screen.blit(position_arrowright, (770, y_pos))      # load the arrow picture
        elif x_pos < -50:   # If the x position of the shuttle is smaller than -50,
            screen.blit(position_arrowleft, (10, y_pos))        # load the arrow picture
        elif y_pos < -50:   # If the y position of the shuttle is smaller than -50,
            screen.blit(position_arrow, (x_pos, 10))            # load the arrow picture
        elif y_pos > 600:   # If the y position of the shuttle is greater than 600,
            show_end_screen()                                   # show the end screen


        for point in mountain_points:           # for any points in the mountain,
            if player_rect.collidepoint(point):     # if the player hits the point
                screen.blit(explosion_image, player_rect)  # Load the explosion image over the player
                show_end_screen()                        # show the death screen

        fuel_level = WRITING_FONT.render(str(fuel), True, (255, 255, 255))  # Text
        velocity_level = WRITING_FONT.render(str(vel_y), True, (255, 255, 255)) # Text
        angle_level = WRITING_FONT.render(str(angle), True, (255, 255, 255))        # Text

        shuttle_neutral = pygame.transform.rotate(shuttle, angle)   # Add the rotation to the shuttle
        screen.blit(shuttle_neutral, player_rect)       # Add the rotation to the rect
        screen.blit(pause, (650, 0))                    # add the text to the screen
        screen.blit(fuel_text, (0, 0))                  # add the text to the screen
        screen.blit(fuel_level, (50, 0))                # add the text to the screen
        screen.blit((velocity), (0, 50))                # add the text to the screen
        screen.blit((velocity_level),(70, 50))          # add the text to the screen
        screen.blit((angle_text),(0, 100))              # add the text to the screen
        screen.blit((angle_level),(70, 100))            # add the text to the screen
        pygame.draw.rect(screen, (0, 255, 0), landing_rect)         # Draw a rectangle in the position of the rect

        if flames:      # If flames are true,
            '''
            pygame.draw.polygon(screen, [255, 109, 14],
                     [(x_pos * 1.5, y_pos ),
                      ((x_pos * 1.5)* 1.5 , y_pos),
                      (((x_pos * 1.5)+(x_pos* 1.5))/2, 2*y_pos * 1.5)])
            '''
            screen.blit(flames_image, (x_pos + 8, y_pos + 25))  # Blit the image in the location specified

        if player_rect.colliderect(landing_rect) and ((angle < 8 and angle > -8) and (vel_y < 0.8)):    # if the player hits the rect with the angles between 8 and -8 and the velocity under 0.8,
            show_victory_screen()                                                                           # show the victory screen
        elif player_rect.colliderect(landing_rect): # or else,
            screen.blit(explosion_image, player_rect)         # blit the explosion image to the player,
            show_end_screen()                                   # then show the end screen

        #Update display
        pygame.display.update()     # Update the screen

# ----------------- MENU ------------------------
def show_menu():
    title = TITLE_FONT.render("Interstellar Landing", True, (255, 255, 255))  # Text
    start = TITLE_FONT.render("Start", True, (0, 0, 0))                     # Text
    instructions = TITLE_FONT.render("Instructions", True, (0, 0, 0))               # Text
    start_rect = pygame.Rect(336, 321, start.get_width(), start.get_height())   # Draw a rect with the width and the height of the text
    instructions_rect = pygame.Rect(289, 372, instructions.get_width(), instructions.get_height())  # Draw a rect with the width and the height of the text
    while True:
        clock.tick(60)

        #event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:  # If clicked,
                if start_rect.collidepoint(event.pos):    # on the start box,
                    show_level_select()                         # show the level select
                if instructions_rect.collidepoint(event.pos):   # on the instructions box,
                    show_instructions()                               # Show the instructions
        #Game state changes
        screen.fill((0, 0, 0))
        screen.blit(moon_pic, (0, 0))               # Load the image
        screen.blit(title, (250, 250))              # Load the text to  the screen
        pygame.draw.rect(screen, (255, 255, 255), start_rect)   # draw a rectangle in the position of the rect
        pygame.draw.rect(screen, (255, 255, 255), instructions_rect)    # draw a rectangle in the position of the rect
        screen.blit(start, start_rect)      # Load the text to the rect
        screen.blit(instructions, instructions_rect)    # Load the text to the rect
        #Update display
        pygame.display.update()     # Update the screen

# ---------------- MENU SCREEN ------------------
title = TITLE_FONT.render("Interstellar Landing", True, (255, 255, 255)) # Text
start = TITLE_FONT.render("Start", True, (0, 0, 0))     # Text
instructions = TITLE_FONT.render("Instructions", True, (0, 0, 0))           # Text
start_rect = pygame.Rect(336, 321, start.get_width(), start.get_height())   # Draw a rect with the width and the height of the text
instructions_rect = pygame.Rect(289, 372, instructions.get_width(), instructions.get_height())      # Draw a rect with the width and the height of the text
while True:
    clock.tick(60)
    #event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:   # If clicked,
            if start_rect.collidepoint(event.pos):  # on the start box,
                show_level_select()                                 # show the level select
            if instructions_rect.collidepoint(event.pos):    # on the instructions box,
                show_instructions()                                 # Show the instructions
    #Game state changes
    screen.fill((0, 0, 0))
    screen.blit(moon_pic, (0, 0))                   # Load the image on the screen
    screen.blit(title, (250, 250))                  # Load the text to  the screen
    pygame.draw.rect(screen, (255, 255, 255), start_rect)       # draw a rectangle in the position of the rect
    pygame.draw.rect(screen, (255, 255, 255), instructions_rect)    # draw a rectangle in the position of the rect
    screen.blit(start, start_rect)                          # Load the text to the rect
    screen.blit(instructions, instructions_rect)            # Load the text to the rect
    #Update display
    pygame.display.update()     # Update the display