textalert
=========
A system for creating channels to alert groups of people about community actions via SMS/text. A work in progress at the moment...

**NOTE: STILL UNDER DEVELOPMENT**

Scenarios
---------
A typical configuration:

1. A group of people need a way to send decentralized up-to-the-second alerts to each other. 
1. A contact from the group contacts system admins to set up a channel for the campaign.
1. The contact informs members of the group to text ADD <CHANNELNAME> to the system number
1. Depending on how the channel is configured, moderators may approve adds or they may be added automatically.
1. The contact recruits and sets moderators for the channel.
1. Users may submit posts to the channel.
1. Depending on how the channel is configured, moderators may APPROVE or REJECT posts.

User Levels
-----------
Here are the levels of user authority:

* **Users** - members of the group who receive posts to the channel
* **Moderators** - members of the group who may approve or reject posts
* **Contact** - member of the group who may appoint moderators
* **Admin** - administrators for the system who can set up a channel

Philosophy
----------
Simple guiding principles for creating this software:
* We are transparent about the risks and benefits.
* We are transparent about the system and software, i.e., releasing as open source.
* We protect users and moderators as much as practical, e.g., encrypting databases (but not messages)
* Use a distributed model or software and moderation
* Make it as simple as possible for admins.
* Make it as simple and low tech for users, i.e., relying on SMS available to virtually all mobile phones.
* Server technology independent, i.e., layers of abstraction to use other database tech, SMS gateways, etc.

Installation
------------
Simple:

```
git clone https://github.com/wmodes/textalert.git
cd textalert
```

If you use ``virtualenv`` (or my fave `virtualenvwrapper`) you may want to create a virtualenv before the next step:

```
pip -r requirements.txt
```

You'll have to make sure you have a running version of mongodb available, and modify the mondgodb configs to point at it.

```
python textalert.py
```