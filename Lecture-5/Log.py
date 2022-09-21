class log:
    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        import datetime 
        log_string = self.func.__name__ + " was called @ " + str(datetime.datetime.now())

        # Open the logfile and append
        with open(log._logfile, 'a') as opened_file:
            # Now we log to the specified logfile
            opened_file.write(log_string + '\n')

        # return base func
        return self.func(*args)

    def setLogFile(file_name):
        log._logfile = file_name

## Test file
#
@log
def function1():
    pass
function1()

log.setLogFile('mylog.log')
function1()

@log
def function2():
    print('Hello class')
function2()
