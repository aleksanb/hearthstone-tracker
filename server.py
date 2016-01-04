from logparse import create_log_handler

import tornado.web
import json
from pathlib import Path

LOG_PATH = 'C:\Program Files (x86)\Hearthstone\Logs\Power.log'
PORT = 8888

if __name__ == '__main__':
	# Create Log Handler
	periodic_log_callback, player_state = create_log_handler(Path(LOG_PATH))
	periodic_log_callback.start()

	# Create Web Handler
	class MainHandler(tornado.web.RequestHandler):
		def get(self):
			self.write(json.dumps(player_state.players))

	app = tornado.web.Application([
		(r"/", MainHandler),
	])
	app.listen(PORT)

	print("Server started on port {}".format(PORT))
	tornado.ioloop.IOLoop.current().start()
