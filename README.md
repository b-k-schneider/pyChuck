# pyChuck
Interface Python to Chuck via OSC.
chuck is its own builtin server, but not very resilient (doesn't detect
duplicates of itself for example, can easily hang with no kind of diagnstic)

Instantiate a pyChuck() object in Python. This will run chuck (if not already
running). pyChuck() talks to chuck with OSC messages

The typical program flow is, a Python statement instantitates a pyChuck()
object which becomes an OSC Server if necessary, and is an OSC client.
pyChuck OSC client passes messages from .py to Chuck VM to shred or
remove other Chuck scripts (.ck files), and return status.

Dependencies: Other than the latest Python 2.7 and Chuck (http://chuck.stanford.edu/), pyOsc is required (https://pypi.python.org/pypi/pyOSC). When in doubt,
google for "Python", "Chuck", "OSC" and "pyOSC".

Note that I have only ever run this on Windows 7. So this is all WYSIWYG.
Make sure that "chuck" is in your system path. pyChuck assumes that. Some
default port numbers are used, which can be ovewrriden.
You can specify the send/receive ports for OSC when you instatiate pyChuck,
but note that these are hardcoded in the Chuck scripts in here and I have
not yet figured out how to make them dynamic for these scripts.

You can run multiple Python scripts/threads. All will use the same Chuck VM.
But you will see some messages due to an attempt to start a second Chuck VM.
You typically ignore these messages, stuff works o.k. anyway, mostly.

# pyChuck
