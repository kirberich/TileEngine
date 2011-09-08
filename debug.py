import traceback

INFO = 0
WARNING = 3
CRITICAL = 5

DEBUG = True
DEBUG_LEVEL = INFO
SHOW_TRACEBACKS = True

def debugPrint(message, level=None):
	if level == 0: print "INFO:",
	if level == 3: print "WARNING:",
	if level == 5: 
		print "CRITICAL:",
	print str(message)

	if SHOW_TRACEBACKS:
		traceback.print_exc()
	
# How to output debug messages. Expects a function that can handle a string or an exception as first argument and the debug level as an optional second
DEBUG_MODE = debugPrint

def debugMsg(message, level=INFO):
	if level >= DEBUG_LEVEL: DEBUG_MODE(message, level)
	if level >= 5: exit(1)