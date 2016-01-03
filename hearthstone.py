# -*- coding: utf-8 -*-

import time
import re
import json
from pathlib import Path

def load_cards():
	with open('cards.json', encoding='utf-8') as f:
		cards = json.load(f)

		lookup = {}
		for card in cards:
			lookup[card['id']] = card

		return lookup


def tail(f):
	f.seek(0, 2)
	while True:
		line = f.readline()
		if not line:
			time.sleep(0.1)
			continue

		yield line


def p(msg):
	print(str(msg).encode('cp1252'))


LOG_PATH = 'C:\Program Files (x86)\Hearthstone\Logs\Power.log'
log_file = Path(LOG_PATH)
cards_database = load_cards()
#pat = re.compile('^.*id=(?P<id>\d*) .*cardId=(?P<card_id>.*) .*player=(?P<player>\d*)\].*$')
pat = re.compile('^.*id=(?P<id>\d*) .*cardId=(?P<card_id>[a-zA-Z0-9\_]*).*player=(?P<player>\d*)\](?: CardID=(?P<alternate_card_id>[a-zA-Z0-9\_]*))?.*$')
players = {}

def ppad(s):
	len_pad = len(s) + 4
	print('#' * len_pad)
	print('# ' + s + ' #')
	print('#' * len_pad)


def print_player_state():
	print()
	print()
	ppad('Player cards ({})'.format(time.strftime("%c")))

	for player in players:
		print()
		ppad('Player ' + player)

		cards = [cards_database[card_id] for card_id in players[player]]	
		cards.sort(key=lambda card: card['name'])
		for card in cards:
			card_ids = players[player][card['id']]
			card_meta = '{}x {} ({} - {})'.format(
				len(card_ids), card['name'], card['id'], card_ids)

			p(card_meta)


with log_file.open(encoding='utf-8') as file:
	for line in tail(file):
		match = pat.match(line)
		if match:
			id = match.group('id')
			cardId = match.group('card_id')
			player = match.group('player')
			alternate_card_id = match.group('alternate_card_id')

			cardId = cardId or alternate_card_id

			if cardId in cards_database:
				if player not in players:
					players[player] = {}

				if cardId not in players[player]:
					players[player][cardId] = set()

				if id not in players[player][cardId]:
					players[player][cardId].add(id)

					print_player_state()
