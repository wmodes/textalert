#!/usr/bin/python
"""workflow.py: workflow module of the textalert system
    Get new transaction
    Parse incoming commands
    Actions for incoming commands
        <POST CONTENT>                         # Summit post to channel
        ADD [MOD] [ME | #########] TO <CHANNEL>
        REMOVE [MOD] [ME | #########] FROM [<CHANNEL>]
        SET <CHANNEL>                          # Set channel as context
        STOP                                   # Stop all messages from system
        RESUME                                 # Resume messages from system
        APPROVE [ALL | LAST 2 | 1,2,5-6 ]      # (Mod-only) Approve adds or posts
        REJECT [ALL | LAST 2 | 1,2,3,5-6 ]     # (Mod-only) Reject adds or posts
        TOMODS [<CHANNEL>]                     # Send message to moderators
        LISTMODS [<CHANNEL>]                   # (Mod-only) List mod numbers
        HELP [<CHANNEL>]                       # Get list of commands for channel
        FLAG
    Sending various error messages
    Assigning reps
    Process and score exception messages
Authors: UBEW (ubew000@gmail.com)
Copyright: 2017, MIT"""

# -*- coding: iso-8859-15 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

#
# imports
#

#
# constants
#

# Things in <> are special values
# Things in [] are optional
# Things separated between | are options
# <PHONE> is a phone number (usually 10 digits)
# <INT> is an integer
# <RANGE> is 1-2,5, 7

COMMANDS = [
        {"name": "post",
         "syntax": "*"
         "example": "police at 4th & Mission",
         "whatitdoes": "Summit post to channel",
         "action": cmd_post
         },
        {"name": "add",
         "syntax": "ADD [MOD] [ME | <PHONE>] [TO <CHANNEL>]",
         "action": cmd_add
         },
        {"name": "remove",
         "syntax": "REMOVE [MOD] [ME | <PHONE>] [FROM <CHANNEL>]",
         "action": cmd_remove
         },
        {"name": "set",
         "syntax": "SET <CHANNEL>",
         "whatitdoes": "Set channel as context",
         "action": cmd_set
         },
        {"name": "stop",
         "syntax": "STOP",
         "whatitdoes": "Stop all messages from system",
         "action": cmd_stop
         },
        {"name": "resume",
         "syntax": "RESUME",
         "whatitdoes": "Resume messages from system",
         "action": cmd_resume
         },
        {"name": "approve",
         "syntax": "APPROVE [ALL | LAST <INT> | <RANGE> ]",
         "whatitdoes": "(Mod-only) Approve adds or posts",
         "action": cmd_approve
         },
        {"name": "reject",
         "example": "REJECT [ALL | LAST <INT> | <RANGE> ]",
         "whatitdoes": "(Mod-only) Reject adds or posts",
         "action": cmd_reject
         },
        {"name": "tomods",
         "syntax": "TOMODS [<CHANNEL>]",
         "whatitdoes": "Send message to moderators",
         "action": cmd_tomods
         },
        {"name": "listmods",
         "syntax": "LISTMODS [<CHANNEL>]",
         "whatitdoes": "(Mod-only) List mod numbers",
         "action": cmd_listmods
         },
        {"name": "help",
         "syntax": "HELP [<CHANNEL>]",
         "whatitdoes": "Get list of commands for channel",
         "action": cmd_help
         },
        {"name": "flag",
         "syntax": "FLAG [LAST 2 | 1,2,5-6 ]",
         "whatitdoes": "Flags a user message",
         "action": cmd_flag
         },

]

# import database


# local modules

#
# get new transaction
#

#
# parse incoming commands
#


#
# actions for incoming commands
#

#
# error messages
#

#
# assigning reps
#

#
# process and score exception messages
#


def main():
    pass


if __name__ == "__main__":
    main()
