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

COMMANDS = {
        # "post":
        #     {"name": "post",
        #      "usage": "*"
        #      "example": "police at 4th & Mission",
        #      "help": "Summit post to channel",
        #      "action": cmd_post
        #      },
        "add":
            {"usage": "ADD [MOD] [ME | <PHONE>] [TO <CHANNEL>]",
             "help": "Add member or mod to channel",
             "action": cmd_add
             },
        "remove":
            {"usage": "REMOVE [MOD] [ME | <PHONE>] [FROM <CHANNEL>]",
             "help": "Remove member or mod from channel",
             "action": cmd_remove
             },
        "set":
            {"usage": "SET <CHANNEL>",
             "help": "Set channel as context",
             "action": cmd_set
             },
        "stop":
            {"usage": "STOP [<CHANNEL>]",
             "help": "Stop all messages from system",
             "action": cmd_stop
             },
        "resume":
            {"usage": "RESUME [<CHANNEL>]",
             "help": "Resume messages from system",
             "action": cmd_resume
             },
        "approve":
            {"usage": "APPROVE [ALL | LAST <INT> | <RANGE> ]",
             "help": "(Mod-only) Approve adds or posts",
             "action": cmd_approve
             },
        "reject":
            {"usage": "REJECT [ALL | LAST <INT> | <RANGE> ]",
             "help": "(Mod-only) Reject adds or posts",
             "action": cmd_reject
             },
        "tomods":
            {"usage": "TOMODS [<CHANNEL>]",
             "help": "Send message to moderators",
             "action": cmd_tomods
             },
        "listmods":
            {"usage": "LISTMODS [<CHANNEL>]",
             "help": "(Mod-only) List mod numbers",
             "action": cmd_listmods
             },
        "help":
            {"usage": "HELP [<CHANNEL>]",
             "help": "Get list of commands for channel",
             "action": cmd_help
             },
        "flag":
            {"usage": "FLAG [LAST <INT> | <RANGE> ]",
             "help": "Flags a user message",
             "action": cmd_flag
             }
}

# import database


# local modules

#
# get new transaction
#
def get_new_transaction():
    """Get one new transaction from transaction database"""
    pass

#
# parse incoming commands
#

def parse_new_cmd(xaction):
    cmd = xaction["message"].split(" ")[0]
    # is this a known command
    if cmd in COMMANDS:
        cmd_record = COMMANDS[cmd]
        cmd_record["action"](xaction)
    # otherwise, this may be a post
    else:
        cmd_post(message)


def cmd_post(xaction):
    """Summit post to channel"""
    pass
    # System looks up their number, finds recent context if any
        # if no context and no channel specified return explanatory error
    # Fetches info about cascadia-antifa
    # Checks to see if still a member
    # Checks to see if she’s a mod
        # If so, distros message
        # If not, sends approval to mods
    # System waits for mod approval/denial
    # If approved, distro to list
    # If not, trash
    # Update Shelby’s context & timestamp (and action?)


def cmd_add(xaction):
    """Add member or mod to channel
        ADD [MOD] (ME | <PHONE>) [TO <CHANNEL>]"""
    origin = xaction["origin"]
    cmd_list = xaction["message"].split(" ")
    # discard the first word which should be 'add'
    cmd_list.pop(0)
    # is the next word 'mod'
    if (cmd_list[0].lower() == 'mod'):
        option_add_mod = True
        cmd_list.pop(0)
    # next word should be 'me' or a phone number
    # TODO: should we allow spaces or symbols in a phone number?
    if (cmd_list[0].lower() == 'me'):
        target = origin
        cmd_list.pop(0)
    else:
        target = cmd_list.pop(0)
    # TODO: normalize_phone by removing symbols, adding country code, etc
    # TODO: Check if target is now a valid phone, if not syntax error
    if (len(cmd_list) == 2 and cmd_list[0].lower() == 'to'):
        channel = cmd_list[1]
    else:
        # TODO: Get last context from user record
        pass
    pass
    # Kris sends text to our number, msg “ADD ME TO cascadia-antifa”
    # Kris’ message put in transaction db
    # Doer-module picks up transaction and acts on it
    # System looks up her number, adds her if she’s not there already
    # System looks up the channel
    # Checks for any of the following conditions
        # Kris might already be subscribed (or a mod)
            # If yes, return explanatory error and stop
        # List is open and does not need mod approval
            # Kris is inserted into User Collection (IF she’s not already in)
            # Kris is inserted into users list of channel
            # Send notice to Kris
        # List needs moderator approval
            # Send notice to Kris
            # If yes, send approval to moderators
            # Wait for approval or denial
            # Send notice to Kris
            # If approved, see previous"""



def cmd_remove(xaction):
    """Remove member or mod to channel
        REMOVE [MOD] [ME | <PHONE>] [FROM <CHANNEL>]"""
    origin = xaction["origin"]
    cmd_list = xaction["message"].split(" ")
    # discard the first word which should be 'remove'
    cmd_list.pop(0)
    # is the next word 'mod'
    if (cmd_list[0].lower() == 'mod'):
        option_add_mod = True
        cmd_list.pop(0)
    # next word should be 'me' or a phone number
    # TODO: should we allow spaces or symbols in a phone number?
    if (cmd_list[0].lower() == 'me'):
        target = origin
        cmd_list.pop(0)
    else:
        target = cmd_list.pop(0)
    # TODO: normalize_phone by removing symbols, adding country code, etc
    # TODO: Check if target is now a valid phone, if not syntax error
    if (len(cmd_list) == 2 and cmd_list[0].lower() == 'from'):
        channel = cmd_list[1]
    else:
        # TODO: Get last context from user record
        pass
    pass


def cmd_set(xaction):
    """Set channel as context
        SET <CHANNEL>"""
    origin = xaction["origin"]
    cmd_list = xaction["message"].split(" ")
    # discard the first word which should be 'set'
    cmd_list.pop(0)    
    if (len(cmd_list) == 1):
        channel = cmd_list[1]
    else:
        # return syntax error with help
        pass
    pass


def cmd_stop(xaction):
    """Stop all messages from system
        STOP [<CHANNEL>]"""
    pass


def cmd_resume(xaction):
    """Resume all messages from system
        RESUME [<CHANNEL>]"""
    pass


def cmd_approve(xaction):
    """Approve adds or posts (mod only)
        APPROVE [ALL | LAST <INT> | <RANGE> ]"""
    pass


def cmd_reject(xaction):
    """Reject adds or posts (mod only)
        REJECT [ALL | LAST <INT> | <RANGE> ]"""
    pass


def cmd_tomods(xaction):
    """Sends messages to moderators
        TOMODS [<CHANNEL>]"""
    pass


def cmd_listmods(xaction):
    """List mod numbers and handles (mod only)
        LISTMODS [<CHANNEL>]"""
    pass


def cmd_help(xaction):
    """Get list of commands for channel relevant to user
        HELP [<CHANNEL>]"""
    pass


def cmd_flag(xaction):
    """Flags a user message
        FLAG [LAST <INT> | <RANGE> ]"""
    pass



#
# actions for incoming commands
#

#
# error messages
#

def syntax_error(xaction, err=None):
    """Return a contextual syntax error"""
    err_str = "Syntax: "
    if err:
        err_str += err
    else:
        # TODO: Make sure user has permission to use this cmd before sending help
        origin = xaction["origin"]
        cmd_list = xaction["message"].split(" ")
        cmd = cmd_list[0]
        if cmd in COMMANDS:
            cmd_record = COMMANDS[cmd]
            err_str += cmd + ' ' + cmd_record["help"] + '. Usage: ' + cmd_record['usage']
        else:
            err_str += "Not sure what you were trying to say there."
    # TODO: turn on sending
    # message.send_one(origin, err_str)


#
# assigning reps
#

#
# process and score exception messages
#


def main():
    # Test all functions one at a time



if __name__ == "__main__":
    main()
