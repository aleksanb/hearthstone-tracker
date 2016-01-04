# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

import time
import json


def print_player_state(hearthstone):
	players = hearthstone.players
	print()
	print()
	ppad('Player cards ({})'.format(time.strftime("%c")))

	for player in players:
		print()
		ppad('Player ' + player)

		type_blacklist = ('HERO_POWER', 'HERO')
		cards = [cards_database[card_id] for card_id in players[player]]
		cards = [card for card in cards if card['type'] not in type_blacklist]
		cards.sort(key=lambda card: card['cost'])

		for card in cards:
			card_ids = players[player][card['id']]
			card_meta = '{} - {}x {} ({} - {})'.format(
				card['cost'], len(card_ids), card['name'], card['id'], card_ids)

			p(card_meta)
