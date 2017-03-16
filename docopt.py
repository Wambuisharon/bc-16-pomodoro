
#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    POMODORO_TIMER start <task_name> 
    POMODORO_TIMER config_time <task_duration>
    POMODORO_TIMER config_cycle <cycle>
    POMODORO_TIMER config_short_break <short_break>
    POMODORO_TIMER config_long_break  <long_break>
    POMODORO_TIMER stop <stop>
    POMODORO_TIMER list <list>
    POMODORO_TIMER (-i | --interactive)
    POMODORO_TIMER(-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from task import Task 

tasks =  Task()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = 'POMODORO_TIMER!' \
        + ' (type help for a list of commands.)' //replace
    prompt = '(POMODORO_TIMER) '
    file = None

    @docopt_cmd
    def do_start(self, arg): 
        """Usage: start <task_name> """

        print(tasks.start(arg["<task_name>"]))
    def do_config_time(self, arg): 
        """Usage: config_time <task_duration> """

        print(tasks.start(arg["<task_name>"]))

    def do_config_short_break(self,arg):
        """Usage: config_short_break<short_break>"""

        print(tasks.short_break(arg["<short_break>"])) 

    def do_config_long_break(self,arg):
        """Usage: config_long_break<"long_break>"""

        print(tasks.long_break(arg["<long_break>"])) 

    '''def do_stop(self,arg):
        """Usage: stop<"stop">"""
        print(tasks.stop(arg["stop"]))'''

    def do_list(self,arg):
        """Usage: list <list>"""

        print(tasks.list(arg["<list>"]))


    def do_sound(self,arg):
        """Usage: sound <sound>"""

        print (tasks.sound(arg["<sound>"]))






    @docopt_cmd
    def do_serial(self, arg):
        """Usage: serial <port> [--baud=<n>] [--timeout=<seconds>]
Options:
    --baud=<n>  Baudrate [default: 9600]
        """

        print(arg)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)