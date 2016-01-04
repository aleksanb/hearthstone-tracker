import json

def load_cards():
	with open('cards.json', encoding='utf-8') as f:
		cards = json.load(f)

		lookup = {}
		for card in cards:
			lookup[card['id']] = card

		return lookup


class PlayerState:
	players = {}
	cards = load_cards()

	def clear_players(self):
		self.players = {}

	def card_drawn(self, id, cardId, player):
		if not cardId:
			return

		if player not in self.players:
			self.players[player] = {}

		if cardId not in self.players[player]:
			self.players[player][cardId] = {
				'meta': self.cards[cardId],
				'ids': []
			}

		if id not in self.players[player][cardId]['ids']:
			self.players[player][cardId]['ids'].append(id)
			return True
