# textalert
A system for alerting large groups of people about community actions via SMS/text.


Installation
------------
Simple:

```
git clone https://github.com/wmodes/textalert.git
cd textalert
pip -r requirements.txt
```

You'll have to make sure you have a running version of mongodb available, and modify the mondgodb configs to point at it.

```
python textalert.py
```