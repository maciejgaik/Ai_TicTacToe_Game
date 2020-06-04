import pygame as pg
import sys

HUMAN = -1
COMP = +1

def check_events(wd, gm, size):
	"""
	Funkcja odpowidzialna za sprawdzanie zachodzacych wydarzen
	:param gm: mechnaika gry
	:param wd: okno gry
	:param width: szerokosc pola gry
	:param size: rozmiar wersji gry
	"""
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_ESCAPE:
				sys.exit()
		elif event.type == pg.MOUSEBUTTONDOWN:
			if event.button == 1:
				mouseX, mouseY = event.pos
				whereX = int(mouseX / int(wd.width))
				whereY = int(mouseY / int(wd.width))
				if gm.game_over(wd.game_area) or gm.empty_cells(wd.game_area) == []:
					wd.clear(gm)
				elif gm.set_move(whereY, whereX, HUMAN):
					wd.update_area(gm)
					gm.ai_turn()
				
