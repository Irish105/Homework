import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)
tornado.options.parse_command_line()

class OzHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("Toto,I've a feeling we're not in Kansas anymore.")



application = tornado.web.Application(handlers=[(r"/oz", OzHandler)])
http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(options.port)
tornado.ioloop.IOLoop.instance().start()
