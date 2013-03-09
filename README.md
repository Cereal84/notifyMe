NotifyMe
========

NotifyMe allow you to run a program and show up a desktop notification when it ends. It uses python-notify (a Python binding for libnotify) which allows to display notifications in a small dialog.



Requirements
------------
 ------------

* python
* python-notify

Support
-------
 -------
Due the python-notify library this script supports only Linux O.S. .

Usage
-----
 -----

	Usage:

		$ python notifyMe.py [OPTIONS] -e "COMMAND ARGS"


	Options:

	  --version             show program's version number and exit

	  -h, --help            show this help message and exit

	  -t "TITLE", --title="TITLE"
         	               specify the title in the notification bar, by default
         	               the title will be the empty

	  -m "MESSAGE", --message="MESSAGE"
         	               specify the message to be showed in the notification
         	               bar by default is "Terminated"

  	  -e "COMMAND", --execute="COMMAND"
         	               the command to be executed, remember to type the
         	               options for the command. This option is mandatory


  	Mandatory Options:

	   The option -e is mandatory

	  Note:

	   Every option needs the argument between the "" if the argument is composed
	   by more than 1 word. EXAMPLE if the title is Super Urgent Data you need to
	   type : 

		python notifyMe.py -t "Super Urgent Data" -e "COMMAND ARGS" 
	   This is necessary even for the -e and -m options, if the argument is composed
	   by just one element you can ignore the "".

	EXAMPLE

	  python notifyMe.py -t ls -m "ls terminated" -e "ls -l"

Acknowledgement
---------------
 ---------------
Francesco Pischedda to have removed the os library and put the source code style complaint with Pep8.

Author
------
 ------

Alessandro Pischedda


Contact
-------
 -------
alessandro.pischedda@gmail.com
