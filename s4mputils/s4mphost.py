import os
import time
from utils.autogui import Autogui
import json
import subprocess

with open(os.path.join(os.path.dirname(__file__), 'cfg.json'), 'r') as cfile:
    cfg = json.load(cfile)

u = Autogui()
u.findAndClick('s4mptext.png')
u.findAndClick('playonlan2.png')
u.findAndClick('leaveroom.png')
if cfg.get('autosync'):
     u.findAndClick('autosyncexpansionpacks2.png')
u.findAndClick('browse1.png')
u.findAndClick('browse2.png')
time.sleep(1)
u.writeAndEnter(cfg.get('save'))
u.findAndClick('hostgame.png')
time.sleep(cfg.get('waittime'))
u.findAndClick('everyonesconnected.png')
time.sleep(1)
u.findAndClick('save.png')
time.sleep(1)
if cfg.get('sims4exe'):
    subprocess.Popen(cfg.get('sims4exe'))
else:
    u.findAndClick('start.png')
