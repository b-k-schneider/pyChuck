import sys
import pyChuck

cmd = ["stat", "shred", "unshred", "r", "q"]

pyc = pyChuck.pyChuck()
while True:
	try:
		s = raw_input('> ')
		if s == 'q':
			break;
		if s == 'r':
			pyc.shred("s.ck,r.ck")
		else:
			q = s.split(" ")
			if q[0] in cmd:
				pyc.sndMsg(q)
			else:
				print "Supported Commands:", cmd
	except:
		print sys.exc_info()
		break

pyc.cleanup()
