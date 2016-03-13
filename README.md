# pyChuck
Interface Python to Chuck via OSC.
chuck is its own builtin server, but not very resilient (doesn't detect
duplicates of itself)

.py instantiates a pyChuck() causing a chuck to run (if not already running)
pyChuck() talks to chuck with OSC messages

Flow:
	.py instantitates pyChuck() which becomes an OSC Server if necessary, and
	is an OSC client.
	pyChuck OSC client passes messages from .py to Chuck VM to shred or
	remove other Chuck scripts, and return status.

Make sure that "chuck" is in your system path. pyChuck assumes that. Some
default port numbers are used, which can be ovewrriden.

You can run multiple Python scripts/threads. All will use the same Chuck VM.
But you will see some messages due to an attempt to start a second Chuck VM.
You typically ignore these messages, stuff works o.k. anyway.
# pyChuck
