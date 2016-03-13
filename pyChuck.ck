/*
 * Chuck Master.
 * Handle "System" messages, manage shreds
 *	<msg-op> := 'echo' | 'shred' | 'unshred' | 'stat' | 'kill'
 */

6449 => int rcvPort;
6448 => int sndPort;

OscIn oin;
rcvPort => oin.port;
oin.addAddress("/pyChuck, sss");

OscOut xmit;
xmit.dest("localhost", sndPort);

OscMsg msg;

fun void doXmit(string addr, string s)
{
    xmit.start(addr);
    s => xmit.add;
    xmit.send();
}


fun void stat()
{
	Machine.status() => int stat;
	doXmit("/chuckPy", Std.itoa(stat));
}

stat();

while(true) {
    oin => now;

	// Handle msg
    while(oin.recv(msg)) { 
        msg.getString(0) => string op;
        msg.getString(1) => string ck;
        msg.getString(2) => string arg;
		if (op == "shred") {
			Machine.add(ck) => int id;
        	doXmit("/chuckPy", op + " " + Std.itoa(id) + "," + ck);
		} else if (op == "unshred") {
			Std.atoi(ck) => int id;
			Machine.remove(id);
		} else if (op == "stat") {
			stat();
		}
        <<< "\t---- Chuck: ", op, ck, arg >>>;
    }
}
