import window
from math import inf as infinity
from os import system

HUMAN = -1
COMP = +1

class Game():

	def __init__(self, wd, winCombo):
		"""
		Klasa opowida za mechanike i logike gry.
		Zawiera niezbedne funckje dla dzialania SI.
		"""
		self.wd = wd
		self.winCombo = winCombo


	def evaluate(self, state):
		"""
		Funkcja sprawdza teoretyczne zwyciestwo ktoregos z graczy
		:param state: zakladany stan gry
		:return: +1 COMP wygral; -1 jeseli HUMAN wygral; 0 remis
		"""
		if self.wins(state, COMP):
			score = +1
		elif self.wins(state, HUMAN):
			score = -1
		else:
			score = 0
		return score


	def wins(self, board, player):
		"""
		Funkcja sprawdza czy gracz wygral
		:param state: aktualny stan planszy
		:param player: COMP albo HUMAN
		:return: True jeseli gracz wygral
		"""
		tmp = []
		for i in self.wd.win:
			x = []
			for j in i:
				x.append(self.wd.game_area[j[0]][j[1]])
			tmp.append(x)
		win = []
		for i in range(self.wd.winCombo):
			win.append(player)
		if win in tmp:
			return True
		else:
			return False


	def game_over(self, state):
		"""
		Funkcja sprawdza czy COMP albo HUMAN wygral
		:param state: stan planszy
		:return: True jeseli COMP albo HUMAN wygral
		"""
		return self.wins(state, HUMAN) or self.wins(state, COMP)


	def empty_cells(self, state):
		"""
		Sprawdzenie pol czy sa puste
		:param state: stan planszy
		:return: lista wspolrzednych pustych pol
		"""
		cells = []
		for x in range(self.wd.size):
			for y in range(self.wd.size):
				if self.wd.game_area[x][y] == 0:
					cells.append([x,y])
		return cells


	def valid_move(self, x, y):
		"""
		Fukcja sprawdza czy ruch jest możliwy
		:param x: pole
		:return: True jeseli pole jest puste
		"""
		if [x,y] in self.empty_cells(self.wd.game_area):
			return True
		else:
			return False


	def set_move(self, x, y, player):
		"""
		Wykonuje ruch jezeli jest mozliwy
		:param x: wspolrzedna x pola
		:param y: wspolrzedna y pola
		:param player: HUMAN albo COMP
		"""
		if self.valid_move(x, y):
			self.wd.game_area[x][y] = player
			return True
		else:
			return False


	def minimax(self, state, depth, player, alpha, beta):
		"""
		Funkcja SI wybierajaca najlepszy ruch.
		:param state: obecny stan gry
		:param depth: indeks wierzcholka drzewa wywolan,
		:param player: HUMAN albo COMP
		:param alpha: paramter alpha
		:param beta: paramter beta
		:return: najlepszy ruch
		"""
		if player == COMP:
			best = [-1, -1, -infinity]
		else:
			best = [-1, -1, +infinity]

		if depth == 0 or self.game_over(state):
			score = self.evaluate(state)
			return [-1, -1, score]

		score = self.evaluate(state)
		if(player == COMP):
			best[2] = alpha
			for cell in self.empty_cells(state):
				x, y = cell[0], cell[1]
				state[x][y] = player
				score = self.minimax(state, depth - 1, -player, best[2], beta)
				score[0], score[1] = x, y
				if(score[2] > best[2]):

					best = score
				state[x][y] = 0
				if(beta <= best[2]):
					break;
		else:
			best[2] = beta
			for cell in self.empty_cells(state):
				x, y = cell[0], cell[1]
				state[x][y] = player
				score = self.minimax(state, depth - 1, -player, alpha, best[2])
				score[0], score[1] = x, y
				if(score[2] < best[2]):
					best = score
				state[x][y] = 0
				if(best[2] <= alpha):
					break;
		return best


	def ai_turn(self):
		"""
		Wywolywanie funkcji minimax
		"""
		board = self.wd.game_area
		depth = min(8, len(self.empty_cells(board)))
		if depth == 0 or self.game_over(board):
			return
		move = self.minimax(board, depth, COMP, -infinity, +infinity)
		x, y = move[0], move[1]
		self.set_move(x, y, COMP)














