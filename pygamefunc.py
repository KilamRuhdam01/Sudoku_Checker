import pygame


def get_cord(pos): 
	global x 
	x = pos[0]//dif 
	global y 
	y = pos[1]//dif 

# Highlight the cell selected 
def draw_box(): 
	for i in range(2): 
		pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7) 
		pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7) 


# Function to draw required lines for making Sudoku grid		 
def draw(): 
	# Draw the lines 
		
	for i in range (9): 
		for j in range (9): 
		    blit(text1, (i * dif + 15, j * dif + 15)) 
			
	# Draw lines horizontally and verticallyto form grid		 
	for i in range(10): 
		if i % 3 == 0 : 
			thick = 7
		else: 
			thick = 1
		pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick) 
		pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)	 

# Fill value entered in cell	 
def draw_val(val): 
	text1 = font1.render(str(val), 1, (0, 0, 0)) 
	screen.blit(text1, (x * dif + 15, y * dif + 15))	 

# Raise error when wrong value entered 
def raise_error1(): 
	text1 = font1.render("WRONG !!!", 1, (0, 0, 0)) 
	screen.blit(text1, (20, 570)) 
def raise_error2(): 
	text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0)) 
	screen.blit(text1, (20, 570)) 

# Check if the value entered in board is valid 
def valid(m, i, j, val): 
	for it in range(9): 
		if m[i][it]== val: 
			return False
		if m[it][j]== val: 
			return False
	it = i//3
	jt = j//3
	for i in range(it * 3, it * 3 + 3): 
		for j in range (jt * 3, jt * 3 + 3): 
			if m[i][j]== val: 
				return False
	return True



# Display instruction for the game 
def instruction(): 
	text1 = font2.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0)) 
	text2 = font2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0)) 
	screen.blit(text1, (20, 520))		 
	screen.blit(text2, (20, 540)) 

# Display options when solved 
def result(): 
	text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0)) 
	screen.blit(text1, (20, 570))	




# # Solves the sudoku board using Backtracking Algorithm 
# def solve(grid, i, j): 
	
# 	while grid[i][j]!= 0: 
# 		if i<8: 
# 			i+= 1
# 		elif i == 8 and j<8: 
# 			i = 0
# 			j+= 1
# 		elif i == 8 and j == 8: 
# 			return True
	 
# 	for it in range(1, 10): 
# 		if valid(grid, i, j, it)== True: 
# 			grid[i][j]= it 
# 			global x, y 
# 			x = i 
# 			y = j 
# 			# white color background\ 
# 			screen.fill((255, 255, 255)) 
# 			draw() 
# 			draw_box() 
# 			pygame.display.update() 
# 			pygame.time.delay(20) 
# 			if solve(grid, i, j)== 1: 
# 				return True
# 			else: 
# 				grid[i][j]= 0
# 			# white color background\ 
# 			screen.fill((255, 255, 255)) 
		
# 			draw() 
# 			draw_box() 
# 			pygame.display.update() 
# 			pygame.time.delay(50)	 
# 	return False