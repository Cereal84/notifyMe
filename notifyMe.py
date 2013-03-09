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


def setup_pynotify():

    if not pynotify.init("NotifyMe"):
        sys.exit(1)

    def notifier(title, message):

        n = pynotify.Notification(opts['title'], msg)
        n.show()

    return notifier


def setup_gntp():
    # More complete example
    growl = gntp.notifier.GrowlNotifier(
        applicationName="NotifyMe",
        notifications=["Completed job",],
    )

    try:
        growl.register()
    except:
        # Be silent.
        pass

    def notifier(_title, message):
        growl.notify(
            noteType="Completed job",
            title=_title,
            description=message,
            sticky=False,
        )

    return notifier


try:
    import pynotify
    notifier = setup_pynotify()
except ImportError:
    print "Library pynotify missing"
    print "trying to import gntp (Growl Notifications)"

    try:
        import gntp.notifier
        notifier = setup_gntp()
    except ImportError:
        print "Unable to import gntp, exiting"
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

    parser.add_option("-T", "--timeit", dest="timeit",
                      metavar="\"TIMEIT\"",
                      help="time the command to be executed")

    group_note = OptionGroup(parser, "Note",
                             "Every options, excepts for -f, need an argument between the \"\" if the argument is composed by more than 1 word."
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

    if 'timeit' in opts:
        import timeit
        cmd = opts['command']

        fun = "call('%s', shell=True)" % cmd
        setup = "from subprocess import call"
        avg = timeit.timeit(stmt=fun, setup=setup, number=1)

        msg = "%s\ntime: %s" % (opts['message'], avg)
    else:
        # execute the command and wait until it is finished
        call(opts['command'], shell=True)
        msg = opts['message']

    notifier(opts['title'], msg)
