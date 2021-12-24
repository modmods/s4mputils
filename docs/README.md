# s4mputils
Various utilities for use with s4mp

---
## Not affiliated with s4mp team, please DO NOT bug them with issues with these scripts.  Create an issue on this repo instead.
---

## s4mphost
Clicks through launcher based on options in cfg.json using [pyautogui](https://pypi.org/project/PyAutoGUI/).
Works best if used in conjuction witha way to skip the menu and world map, such as [these mods by thepancake1 and MizoreYukii](https://www.patreon.com/posts/skip-world-map-1-57554501).
Currently only tested with free version 0.15.0 so only works for lan/direct connection. Probably only works on windows at the moment.

Instructions:
1. Either clone the repo or download as zip and extract.
2. Install python (written using python 3.9) and required libraries listed in requirements.txt
    ```pip requirements.txt```
3. Fill out cfg.json
    ```
    {
    	"sims4exe": "C:\\Games\\Sims4\\Game\\Bin\\TS4_x64.exe -args", #null for default s4mp launcher behavior.
    	"save": "Slot_00000004.save",
    	"autosync": true, #"auto-sync expansion packs" toggle in launcher
    	"waittime": 300 #time (in seconds) to keep lobby open before locking and launching 
    }
    ```
4. Launch s4mp normally.  Make sure it is on your main monitor (requirement for pyautogui) and try not to have too many windows blocking it.  The script will try to switch focus to it by clicking on the top left corner.
5. Run s4mphost by double-clicking on it in file explorer or runnning via command line 
```python <pathto>/s4mphost```
