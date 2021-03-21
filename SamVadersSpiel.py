import pygame as pg

pg.init()

array = [ [0, 0, 0],  [0, 0, 0], [0, 0, 0]]

screen = pg.display.set_mode((640, 480))
pg.display.set_caption("Sam Vaders Spiel")
#screen.fill((255,140,0))
schwarz = (0, 0, 0)
screen.fill(schwarz)
weiß=(255, 255, 255)
green = (0, 255, 0) 
blue = (0, 0, 128)

pg.draw.line(screen, weiß, [213, 10], [213, 470], 4)
pg.draw.line(screen, weiß, [427, 10], [427, 470], 4)

pg.draw.line(screen, weiß, [10, 160], [630, 160], 4)
pg.draw.line(screen, weiß, [10, 320], [630, 320], 4)

SamVader = pg.image.load("Sam2.jpg")
Coucho = pg.image.load("Coucho2.jpg")


Coucho_klein = pg.transform.scale(Coucho, (175,136))
Sam_klein = pg.transform.scale(SamVader, (175,136))







pg.display.flip()

clock = pg.time.Clock()
clock.tick(60)
i = 0
spieloffen = True
while spieloffen:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			spieloffen = False
		elif event.type == pg.MOUSEBUTTONDOWN:
			
			pos = pg.mouse.get_pos()
			posX = pos[0]
			posY = pos[1]
			
			#oben links
			if posX >= 0 and posX <= 213 and posY >= 0  and posY <= 160:
				if array[0][0] == 0:
					if i % 2 == 0:
						screen.blit(Sam_klein, (19, 17))
						pg.display.flip()
						array[0][0] = 1
					else:
						screen.blit(Coucho_klein, (19, 17))
						pg.display.flip()
						array[0][0] = 2
			#mitte oben
			if posX >= 213 and posX <= 427 and posY >= 0  and posY <= 160:
				if array[0][1] == 0:
					if i % 2 == 0:
						screen.blit(Sam_klein, (232, 17))
						pg.display.flip()
						array[0][1] = 1
					else:
						screen.blit(Coucho_klein, (232, 17))
						pg.display.flip()
						array[0][1] = 2
			#oben rehcts
			elif posX >= 427 and posX <= 640 and posY >= 0  and posY <= 160:
				if array[0][2] == 0:
					if i % 2 == 0:
						screen.blit(Sam_klein, (446, 17))
						pg.display.flip()
						array[0][2] = 1
					else:
						screen.blit(Coucho_klein, (446, 17))
						pg.display.flip()
						array[0][2] = 2
						
			#mitte links
			elif posX >= 0 and posX <= 213 and posY >= 160  and posY <= 320:
				if array[1][0] == 0:
					if i % 2 == 0:
						screen.blit(Sam_klein, (19, 177))
						pg.display.flip()
						array[1][0] = 1
					else:
						screen.blit(Coucho_klein, (19, 177))
						pg.display.flip()
						array[1][0] = 2
			#mitte mitte
			elif posX >= 213 and posX <= 427 and posY >= 160  and posY <= 320:
				if array[1][1] == 0:
					if i % 2 == 0:
						screen.blit(Sam_klein, (232, 177))
						pg.display.flip()
						array[1][1] = 1
					else:
						screen.blit(Coucho_klein, (232, 177))
						pg.display.flip()
						array[1][1] = 2
			#mitte rechts
			elif posX >= 427 and posX <= 640 and posY >= 160  and posY <= 320:
				if array[1][2] == 0:
					if i % 2 == 0:
						screen.blit(Sam_klein, (446, 177))
						pg.display.flip()
						array[1][2] = 1
					else:
						screen.blit(Coucho_klein, (446, 177))
						pg.display.flip()
						array[1][2] = 2
			#unten links
			elif posX >= 0 and posX <= 213 and posY >= 320  and posY <= 480:
				if array[2][0] == 0:
					if i % 2 == 0:
						screen.blit(Sam_klein, (19, 337))
						pg.display.flip()
						array[2][0] = 1
					else:
						screen.blit(Coucho_klein, (19, 337))
						pg.display.flip()
						array[2][0] = 2
			#unten mitte
			elif posX >= 213 and posX <= 427 and posY >= 320  and posY <= 480:
				if array[2][1] == 0:
					if i % 2 == 0:
						screen.blit(Sam_klein, (232, 337))
						pg.display.flip()
						array[2][1] = 1
					else:
						screen.blit(Coucho_klein, (232, 337))
						pg.display.flip()
						array[2][1] = 2
			#unten rechts
			elif posX >= 427 and posX <= 640 and posY >= 320  and posY <= 480:
				if array[2][2] == 0:
					if i % 2 == 0:
						screen.blit(Sam_klein, (446, 337))
						pg.display.flip()
						array[2][2] = 1
					else:
						screen.blit(Coucho_klein, (446, 337))
						pg.display.flip()
						array[2][2] = 2
				
				
			if (array[0][0] == 1 and array[0][1] == 1 and array[0][2] == 1) or (array[1][0] == 1 and array[1][1] == 1 and array[1][2] == 1) or (array[2][0] == 1 and array[2][1] == 1 and array[2][2] == 1) or (array[0][0] == 1 and array[1][0] == 1 and array[2][0] == 1) or (array[0][1] == 1 and array[1][1] == 1 and array[2][1] == 1) or (array[0][2] == 1 and array[1][2] == 1 and array[2][2] == 1) or(array[0][0] == 1 and array[1][1] == 1 and array[2][2] == 1) or (array[0][2] == 1 and array[1][1] == 1 and array[2][0] == 1):
				font = pg.font.Font('freesansbold.ttf', 32) 
				text = font.render('Sam gewinnt!', True, green, blue) 
				textRect = text.get_rect()
				
				textRect.center = (320, 240) 
				screen.blit(text, textRect) 
				"""
				text2 = font.render('Beenden', True, green, blue) 
				textRect2 = text2.get_rect()  
				print(textRect2)  
				textRect2.center = (200, 300) 
				screen.blit(text2, textRect2) 
				pg.display.flip()
				if posX >= 128.5 and posX <= 271.5 and posY >= 283.5  and posY <= 316.5:
					pg.quit
				
				
				text3 = font.render('Nochmal', True, green, blue) 
				textRect3 = text3.get_rect()  
				textRect3.center = (420, 300) 
				screen.blit(text3, textRect3) 
				"""
				pg.display.flip()
				
				
				
			elif (array[0][0] == 2 and array[0][1] == 2 and array[0][2] == 2) or (array[1][0] == 2 and array[1][1] == 2 and array[1][2] == 2) or (array[2][0] == 2 and array[2][1] == 2 and array[2][2] == 2) or (array[0][0] == 2 and array[1][0] == 2 and array[2][0] == 2) or (array[0][1] == 2 and array[1][1] == 2 and array[2][1] == 2) or (array[0][2] == 2 and array[1][2] == 2 and array[2][2] == 2) or(array[0][0] == 2 and array[1][1] == 2 and array[2][2] == 2) or (array[0][2] == 2 and array[1][1] == 2 and array[2][0] == 2):
				font = pg.font.Font('freesansbold.ttf', 32) 
				text = font.render('Coucho gewinnt!', True, green, blue) 
				textRect = text.get_rect()  
				textRect.center = (320, 240) 
				screen.blit(text, textRect) 
				pg.display.flip()
			i = i+ 1


pg.quit