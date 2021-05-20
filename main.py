# Import the System Library and Python Library
import sys, pygame
# Initialize Pygame
pygame.init()

# Setting Window Size
size = width, height = 650, 350
# Creating a Display Window with Size
screen = pygame.display.set_mode(size)

# Loading a Ball Image
ball = pygame.image.load("intro_ball.gif")
# Measure the Ball Size in Rectangle
ballrect = ball.get_rect()

# Setting Ball Speed
speed = [1, 1]
# Setting Color (BLACK = 0, 0, 0)
black = 0, 0, 0

# Makes the Game Repeating
while(True):
	# When the 'X', Exit Button is Pressed, Game Terminates
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			sys.exit()

	# Changing the Ball DIrection After Bouncing
	ballrect = ballrect.move(speed)

	if(ballrect.left < 0 or ballrect.right > width):
		speed[0] = -speed[0]
	if(ballrect.top < 0 or ballrect.bottom > height):
		speed[1] = -speed[1]

	# Setting Background Color (Solid Black or Random Color)
	screen.fill(black)
	# Updating the Screen and Ball Position
	screen.blit(ball, ballrect)
	pygame.display.flip()