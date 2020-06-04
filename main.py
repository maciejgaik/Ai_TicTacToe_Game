import pygame as pg
import sys
import os
import window
import game
import events

def run_game():
	"""
	Glowna funkcja gry
	"""
	size = int(input("Podaj ilosc pol w zakresie 3 - 10: "))
	while(size < 3 or size > 10):
		size = int(input("Podaj ilosc pol w zakresie 3 - 10: "))
	winCombo = int(input("Podaj ilosc znakow w rzedzie wygrywajacych w zakresie od 3 do ilosci pol: "))
	while(winCombo < 3 or winCombo > size):
		winCombo = int(input("Podaj ilosc znakow w rzedzie wygrywajacych w zakresie od 3 do ilosci pol: "))
	pg.init() #inicjalizacja fukcji biblioteki PyGame
	wd = window.Window(size, winCombo) #inicjalizacja okna gry
	wd.winArr() #stworzenie wygrywajacych ukladow 
	wd.draw_area() #rysowanie planszy
	gm = game.Game(wd, winCombo) #inicjalizacja mechaniki gry
	while True:
		events.check_events(wd, gm, size) #sprawdzanie wydarzen
		wd.update_area(gm) #odswiezanie planszy
		pg.display.update() #wyswietlanie aktualnego stanu



run_game()

