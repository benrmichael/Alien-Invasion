import pygame

# Initialize pygame
pygame.init()

# Set the window size
width = 600
height = 400

# Create the window
screen = pygame.display.set_mode((width, height))

# Create the paddles and the ball
paddle1 = pygame.Rect(10, 150, 20, 100)
paddle2 = pygame.Rect(width - 30, 150, 20, 100)
ball = pygame.Rect(width/2 - 15, height/2 - 15, 30, 30)

# Set the initial velocity of the ball
ball_velocity = [5, 5]

# Create the main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles based on user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.y -= 5
    if keys[pygame.K_s]:
        paddle1.y += 5
    if keys[pygame.K_UP]:
        paddle2.y -= 5
    if keys[pygame.K_DOWN]:
        paddle2.y += 5

    # Move the ball
    ball.x += ball_velocity[0]
    ball.y += ball_velocity[1]

    # Handle collisions with the paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_velocity[0] = -ball_velocity[0]
    # Handle collisions with the walls
    if ball.top <= 0 or ball.bottom >= height:
        ball_velocity[1] = -ball_velocity[1]
    if ball.left <= 0 or ball.right >= width:
        running = False

    # Draw the paddles and the ball
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle1)
    pygame.draw.rect(screen, (255, 255, 255), paddle2)
    pygame.draw.circle(screen, (255, 255, 255), ball.x)