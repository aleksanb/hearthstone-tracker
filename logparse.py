from player_state import PlayerState
from utils import p

import re
import tornado.ioloop

card_update_pattern = re.compile('^.*id=(?P<id>\d*) .*cardId=(?P<card_id>[a-zA-Z0-9\_]*).*player=(?P<player>\d*)\](?: CardID=(?P<alternate_card_id>[a-zA-Z0-9\_]*))?.*$')
game_complete_pattern = re.compile('^.*TAG_CHANGE Entity=GameEntity tag=STATE value=COMPLETE.*$')

player_state = PlayerState()


def parse_log_lines(line):
	if game_complete_pattern.match(line):
		player_state.clear_players()

	match = card_update_pattern.match(line)
	if not match:
		return

	id = match.group('id')
	cardId = match.group('card_id')
	alternate_card_id = match.group('alternate_card_id')
	player = match.group('player')

	if player_state.card_drawn(id, cardId or alternate_card_id, player):
		p("Updated player state")


def create_log_handler(file_path):
	f = file_path.open(encoding='utf-8')
	f.seek(0, 2)

	def tail():
		while True:
			line = f.readline()
			if not line:
				break

			tornado.ioloop.IOLoop.current().add_callback(
				parse_log_lines, line)

	return tornado.ioloop.PeriodicCallback(tail, 1000), player_state
