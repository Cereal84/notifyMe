#!/usr/bin/python
"""
notifyMe: allows the user to execute a program
and when it ends show up a dialog with a title and message
in order to notify that it is ended.

"""

__author__ = "Alessandro Pischedda"
__email__ = "alessandro.pischedda@gmail.com"


import sys
from subprocess import call

<<<<<<< HEAD
=======

def setup_pynotify():

    if not pynotify.init("NotifyMe"):
        sys.exit(1)

    def notifier(title, message):

        n = pynotify.Notification(opts['title'], msg)
        n.show()

    return notifier


def setup_gntp():

    def notifier(_title, message):
        gntp.notifier.mini(
            title=u"{0}".format(_title),
            description=u"{0}".format(message),
            applicationName=u"NotifyMe"
        )

    return notifier


>>>>>>> 351bc32311f9c287834866f5574ab4459219cc80
try:
    import pynotify
except ImportError:
    print "Library pynotify missing"
    sys.exit(-1)

try:
    from optparse import OptionParser, OptionGroup
except ImportError:
    print "Library optparse missing"
    sys.exit(-1)


def options():

    # set the option and help
    usage = "usage: python %prog [OPTIONS] -e \"COMMAND ARGS\""

    parser = OptionParser(usage=usage, version="%prog 0.9")
    parser.add_option("-t", "--title",
                      default="",
                      metavar="\"TITLE\"",
                      dest="title",
                      help="specify the title in the notification bar, "
                      "by default the title will be empty")
    parser.add_option("-m", "--message",
                      metavar="\"MESSAGE\"",
                      dest="message", default="Terminated",
                      help="specify the message to be showed in the notification bar "
                      "by default is \"Terminated\"")
    parser.add_option("-e", "--execute", dest="command",
                      metavar="\"COMMAND\"",
                      help="the command to be executed, "
                      "remember to type the options for the command."
                      " This option is mandatory.")

    group_note = OptionGroup(parser, "Note",
                             "Every options need an argument between the \"\" if the argument is composed by more than 1 word."
                             "EXAMPLE if the title is Super Urgent Data you need to type :"
                             " -t \"Super Urgent Data\" . "
                             "This is necessary even for the -e and -m options, if the argument is composed by just one element"
                             " you can ignore the \"\".")

    group_mandatory = OptionGroup(parser, "Mandatory Options", "The option -e is mandatory")

    parser.add_option_group(group_mandatory)
    parser.add_option_group(group_note)

    (options, args) = parser.parse_args()

    # make options as a dictionary
    opts = options.__dict__

    if opts['command'] is None:
        parser.error("Missing the option -e, it is mandatory.")

    return opts

if __name__ == "__main__":

    opts = options()

<<<<<<< HEAD
    if not pynotify.init("NotifyMe"):
        sys.exit(1)
=======
    if opts['timeit'] is not None:
        import timeit
        cmd = opts['command']
>>>>>>> 351bc32311f9c287834866f5574ab4459219cc80

    # execute the command and wait until it is finished
    call(opts['command'], shell=True)

    n = pynotify.Notification(opts['title'], opts['message'])
    n.show()

