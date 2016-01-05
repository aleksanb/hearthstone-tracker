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
			self.players[player][cardId] = self.cards[cardId]
			self.players[player][cardId]['ids'] = []

		if id not in self.players[player][cardId]['ids']:
			self.players[player][cardId]['ids'].append(id)
			return True

	def get_formatted_players(self):
		output = {}

		for player in sorted(self.players.keys()):
			cards = list(self.players[player].values())

			hero = None
			heroes = [card for card in cards if card['type'] == 'HERO']
			if len(heroes) > 0:
				hero = heroes[0]

			type_whitelist = ('MINION', 'SPELL', 'WEAPON')
			filtered_cards = [card for card in cards if card['type'] in type_whitelist]
			sorted_cards = sorted(filtered_cards, key=lambda card: card['cost'])

			output[player] = {
				'hero': hero,
				'cards': sorted_cards
			}

		return output
