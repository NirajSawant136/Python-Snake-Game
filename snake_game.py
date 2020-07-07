# snake game
import pygame
import time
import random

WIDTH , HEIGHT = 500, 500

WHITE = (255, 255, 255)
RED = (255, 38, 38)
GREEN = (38, 255, 38)
BLACK = (0, 0, 0)

pygame.init()
WORLD = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

font = pygame.font.Font('Sriracha-Regular.ttf', 32)

global cells , snake, dirX, dirY, food_present, food, foodPos, score

dirX, dirY = 1, 0
grid = 25
cell_size = 20

score = -1
food_present = 0

cells = []
snake = [(4,4)]
for i in range(grid):
        for j in range(grid):
                cells.append((i, j))

food = list(set(cells) - set(snake))
foodPos = random.choice(food)

def collision(X, Y):

	collided = False
	
	if (X, Y) in snake:
		collided = True

	elif X > 24 or X < 0:
		collided = True

	elif Y > 24 or Y < 0:
		collided = True

	return collided  

def draw_snake():

		global food_present, snake

		head = snake[0]

		for i in range(len(snake)-1,0,-1):
			snake[i] = snake[i-1]

		if snake[0] == foodPos:
			food_present = 0

		tail = snake[len(snake)-1]	
		
		if collision(snake[0][0] + dirX, snake[0][1] + dirY):
			pygame.quit()

		else:
			snake[0] = (snake[0][0] + dirX, snake[0][1] + dirY)

			for parts in snake:
				if parts == snake[0]:
					pygame.draw.rect(WORLD, GREEN, (parts[0]*cell_size, parts[1]*cell_size, cell_size, cell_size), 0)
					pygame.display.update()
				else:
					pygame.draw.rect(WORLD, WHITE, (parts[0]*cell_size, parts[1]*cell_size, cell_size, cell_size), 0)
					pygame.display.update()

			pygame.draw.rect(WORLD, (0, 0, 0), (tail[0]*cell_size, tail[1]*cell_size, cell_size, cell_size), 0)
			pygame.display.update()
			Score = font.render('Score: '+ str(score), True, WHITE, None)
			score_area = Score.get_rect()
			score_area.center = (400, 20)
			WORLD.blit(Score, score_area)

def food():
	global food_present, foodPos, snake, score

	if(food_present == 0):
		score += 1
		food = list(set(cells) - set(snake))
		foodPos = random.choice(food)
		food_present = 1
		add_tail = snake[len(snake)-1]
		snake.append(add_tail)
		#print(score)
		WORLD.fill((0, 0, 0))

	pygame.draw.rect(WORLD, RED, (foodPos[0]*cell_size, foodPos[1]*cell_size, cell_size, cell_size), 0)
	pygame.display.update()

def snake_up():
	global dirX, dirY
	
	dirX = 0
	if dirY == 0:
		dirY = -1

def snake_down():
	global dirX, dirY

	dirX = 0
	if dirY == 0:
		dirY = 1

def snake_left():
	global dirX, dirY

	dirY = 0
	if dirX == 0:
		dirX = -1

def snake_right():
	global dirX, dirY

	dirY = 0
	if dirX == 0:
		dirX = 1

running = True
while running:
		#pygame.fill((0,0,0))
		time.sleep(0.15)
		#WORLD.fill((0,0,0))
		food()
		draw_snake()
		pygame.draw.rect(WORLD, WHITE, (0,0,500,500), 3)
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				running = False

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					snake_left()

				elif event.key == pygame.K_UP:
					snake_up()

				elif event.key == pygame.K_RIGHT:
					snake_right()

				elif event.key == pygame.K_DOWN:
					snake_down()

				elif event.key == pygame.K_q:
					pygame.quit()
					running = False