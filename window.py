import pygame as pg
import sys
import os

white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
HUMAN = -1
COMP = +1

class Window():

	def __init__(self, size, winCombo):
		"""
		Klasa odpowidzialna za oprawe graficzna gry.
		Zawiera funckje zwiazane z rysowaniem planczy 
		oraz wstawianiem X lub O
		"""
		self.game_area = []
		self.win = []
		self.width = 200
		self.size = int(size)
		self.winCombo = winCombo
		self.screen_size = (self.width*self.size,self.width*self.size)
		self.screen = pg.display.set_mode(self.screen_size, 0, 32)
		pg.display.set_caption("Kolko i Krzyzyk")
		for i in range(self.size):
			tmp = []
			for j in range(self.size):
				tmp.append(0)
			self.game_area.append(tmp)
		self.screen.fill(black)

	def draw_area(self):
		"""
		Funkcja rysuje poczatkowa plansze gry
		"""
		for i in range(self.size):
			for j in range(self.size):
				pg.draw.rect(self.screen, white, pg.Rect((j * self.width, i * self.width), (self.width, self.width)), 1)


	def update_area(self, gm):
		"""
		Funkcja odpowiedzialna za odswiezanie planszy 
		:param gm: mechanika gry dla wczytania aktualnego stanu
		"""
		for i in range(self.size):
			for j in range(self.size):
				x = int(j * self.width + self.width / 2)
				y = int(i * self.width + self.width / 2)
				if self.game_area[i][j] == HUMAN:
					self.drawX((x,y))
				elif self.game_area[i][j] == COMP:
					self.drawCircle((x,y))
		if gm.game_over(self.game_area) or gm.empty_cells(self.game_area) == []:
			self.displayWhoWin(gm.evaluate(self.game_area))


	def drawCircle(self, where):
		"""
		Funkcja rysujaca znak O w odpowidznim miejscu na planszy
		:param where: wybrane miejsce na planszy
		"""
		pg.draw.circle(self.screen, blue, where, int(self.width/3))


	def drawX(self, where):
		"""
		Funkcja rysujaca znak X w odpowidznim miejscu na planszy
		:param where: wybrane miejsce na planszy
		"""
		x = int(0.6*self.width/2)
		y = int(0.8*self.width/2)
		point1 = (x+where[0], y+where[1])
		point2 = (-x+where[0], -y+where[1])
		point3 = (-x+where[0], y+where[1])
		point4 = (x+where[0], -y+where[1])
		pg.draw.line(self.screen, red, point1, point2, 20)
		pg.draw.line(self.screen, red, point3, point4, 20)



	def winArr(self):
		"""
		Funkcja odpowiedzialna za wybranie ukladow wygrywajacych
		"""
		#poziome
		for i in range(0,self.size):
			for j in range(0,self.size):
				q = []
				w = []
				e = []
				r = []
				for k in range(0,self.winCombo):
					if j + self.winCombo - 1 < self.size:
						q.append([i,j+k])
					if j + self.winCombo - 1 < self.size:
						w.append([j+k,i])
					if j + self.winCombo - 1 < self.size and i + self.winCombo - 1 < self.size:
						e.append([i+k,j+k])
					if j - self.winCombo + 1 >= 0 and i + self.winCombo - 1 < self.size:
						r.append([i+k,j-k])
				if q != []:
					self.win.append(q)
				if w != []:
					self.win.append(w)
				if e != []:
					self.win.append(e)
				if r != []:
					self.win.append(r)
		for i in self.win:
			print(i)


	def displayWhoWin(self, who):
		"""
		Funckja odpowiedzialna za wyswietelnie napisu
		ktory z graczy wygral.
		:param who: ktory z graczy wygral
		"""
		pg.font.init()
		font = pg.font.SysFont("impact", 96)
		if int(who) == HUMAN:
			text = font.render("You Win!", True, green)
		elif int(who) == COMP:
			text = font.render("Comp Win!", True, green)
		else:
			text = font.render("Draw!", True, green) 
		text_rect = text.get_rect()
		text_rect.centerx = self.screen.get_rect().centerx
		text_rect.centery = self.screen.get_rect().centery
		self.screen.blit(text,text_rect)


	def clear(self,gm):
		"""
		Funkcja odpowiedzialna za wyczyszczenie 
		plnaszy w przypadku ponownej rozgrywki
		"""
		self.screen.fill(black)
		self.game_area = []
		self.draw_area()
		for i in range(self.size):
			tmp = []
			for j in range(self.size):
				tmp.append(0)
			self.game_area.append(tmp)
	













