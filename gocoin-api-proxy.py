#!/usr/bin/env python
import logging
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import urlfetch

class MainHandler(webapp.RequestHandler):
    def get(self):
    	self.response.headers['Access-Control-Allow-Origin'] = 'http://gocoin.org'
        headers = {}
    	for x in self.request.headers:
        	if (x != "X-Apiurl" and x[0:2] != "Ac" and x[0:2] != "Re"):
        		headers[x] = self.request.headers[x]
       	r = urlfetch.fetch(self.request.headers["X-Apiurl"], None, "GET", headers, True, True, None, None)
        if (r.status_code != 200):
        	self.response.set_status(r.status_code)
        	self.response.out.write(str(r.status_code))
        else:
        	self.response.out.write(r.content)
        
    def post(self):
    	self.response.headers['Access-Control-Allow-Origin'] = 'http://gocoin.org'
        headers = {}
        for x in self.request.headers:
        	if (x != "X-Apiurl" and x[0:2] != "Ac" and x[0:2] != "Re" and x[0:2] != "Or"):
        		headers[x] = self.request.headers[x]
        logging.info(self.request.headers['X-Apiurl'])
        for x in headers:
        	logging.info(x + ": " + headers[x])
        logging.info("\r\n")
        logging.info(self.request.body)
       	r = urlfetch.fetch(self.request.headers['X-Apiurl'], self.request.body, "POST", headers, True, True, None, None)
        if (r.status_code != 200):
        	self.response.set_status(r.status_code)
        	self.response.out.write(str(r.status_code))
        else:
        	if ('location' in r.headers):
        		self.response.out.write(r.headers['location'])
        	else:
				self.response.out.write(r.content)
        	
    def put(self):
    	self.response.headers['Access-Control-Allow-Origin'] = 'http://gocoin.org'
        headers = {}
        for x in self.request.headers:
        	if (x != "X-Apiurl" and x[0:2] != "Ac" and x[0:2] != "Re"  and x[0:2] != "Us"  and x[0:4] != "Conn"):
        		headers[x] = self.request.headers[x]
        for x in headers:
        	logging.info("-H \"" + x + ": " + headers[x] + "\" ")
        logging.info("PUT \"" + self.request.headers['X-Apiurl'] + "\"")
        logging.info(self.request.body + ""); 
       	r = urlfetch.fetch(self.request.headers['X-Apiurl'], self.request.body, "PUT", headers, True, True, None, None)
        logging.info(r.status_code)
       	if (r.status_code != 200):
        	self.response.set_status(r.status_code)
        	self.response.out.write(str(r.status_code))
        else:
        	if ('location' in r.headers):
        		self.response.out.write(r.headers['location'])
        	else:
				self.response.out.write(r.content)

				    	
    def options(self):
    	self.response.headers['Access-Control-Allow-Origin'] = 'http://gocoin.org'
      	self.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    	if ('Access-Control-Request-Headers' in self.request.headers):
    		self.response.headers['Access-Control-Allow-Headers'] = self.request.headers['Access-Control-Request-Headers']
    	
    		
def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
