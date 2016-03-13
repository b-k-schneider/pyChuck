import OSC
import os, sys, threading, time, subprocess

class server(threading.Thread):
	def __init__(self, port):
		self.p = None
		self.srv = None
		self.port = port
		threading.Thread.__init__(self)

	def chuckPy(path, tags, args, source, s):
#		print path, tags, args, source, s
		print "chuckPy:", source, type(source)

	def runChuck(self):
		self.p = subprocess.Popen("chuck pyChuck.ck")
		stat = None
		for i in range(10):
			time.sleep(1)
			stat = self.p.poll()
			if stat != None:
				self.p.kill()
				self.p = None
				return False
		return True

	def run(self):
		self.srv = None
		if not self.runChuck():
			print "not runChuck"
			return
		try:
			self.srv = OSC.OSCServer(('127.0.0.1', self.port))
			self.srv.timeout = 0
			self.srv.addMsgHandler("/chuckPy", self.chuckPy)
			self.srv.serve_forever()
		except:
			self.close()
			print "run", sys.exc_info()
			return

	def srv(self):
		return self.srv
		
	def close(self):
		try:
			if self.p != None:
				self.p.kill()
			if self.srv != None:
				self.srv.close()
		except:
			print sys.exc_info()

class client():
	def __init__(self, port):
		self.c = OSC.OSCClient()
		self.c.connect(('127.0.0.1', port))

	def close(self):
		self.c.close()

	def sndMsg(self, q):
		msg = OSC.OSCMessage()
		msg.setAddress("/pyChuck")
		msg.append(q[0])
		f = "foo"
		b = "bar"
		if (len(q) > 1):
			f = q[1]
			if (len(q) > 2):
				b = q[2]
		msg.append(f)
		msg.append(b)
		self.c.send(msg)

class pyChuck():
	def __init__(self, srvPort=6448, clnPort=6449, init=False):
		if init:
			q = subprocess.check_output("chuck --kill",
											stderr=subprocess.STDOUT)
		self.srv = server(srvPort)
		self.srv.start()
		self.cln = client(clnPort)
		self.sndMsg(["stat"])

	def shred(self, ck):
		c = ck.split(",")
		for cc in c:
			self.sndMsg(["shred", cc])

	def sndMsg(self, q):
		self.cln.sndMsg(q)

	def cleanup(self):
		self.cln.close()
		self.srv.close()

if __name__ == "__main__":
	pyc = pyChuck()
	while True:
		try:
			s = raw_input('> ')
			if s == 'q':
				break;
			if s == 'r':
				pyc.shred("s.ck,r.ck")
			else:
				q = s.split(" ")
				pyc.sndMsg(q)
		except:
			print sys.exc_info()
			break

	pyc.cleanup()
