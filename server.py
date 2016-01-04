from logparse import create_log_handler

import tornado.web
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
			self.set_header("Access-Control-Allow-Origin", "*")
			self.write(player_state.get_formatted_players())

	app = tornado.web.Application([
		(r"/", MainHandler),
	])
	app.listen(PORT)

	print("Server started on port {}".format(PORT))
	tornado.ioloop.IOLoop.current().start()
