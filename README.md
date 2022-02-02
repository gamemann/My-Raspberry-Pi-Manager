# My Raspberry Pi Manager
## Overview
I have two Raspberry Pi 4 Model B devices that I hooked up to my two TVs (one in my bedroom and the other in my new game room). I installed Raspberry OS on both along with Steam Link. Both are configured to boot into an existing desktop under my user and Steam Link automatically starts.

## Description
To make things easier, I decided to make a small Raspberry Pi manager that includes two buttons **so far**. One button stops Steam link while the other starts it. Steam Link sometimes crashes and the only way to launch it is from within the terminal using something like `DISPLAY=:0 steamlink > /dev/null 2>&1 &`. This is easy for me, but my girlfriend isn't tech savy. Therefore, I decided to make this small project so both of us can use a simple web interface through our LAN to start or stop the Steam Link application on the main desktop (that the TVs are hooked up to).

This is also a Django application. The buttons are displayed at the main index.

**WARNING** - This isn't an official project that I want to maintain. I just wanted to share this code for others to use if they need it. Don't expect any updates on this project.

## Credits
* [Christian Deacon](https://github.com/gamemann)