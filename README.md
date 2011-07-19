# Login Background Updater *(LBU)*

This is a simple python script which sets your login window's background to your current Desktop background.

## System Requirements:
Tested with Python 2.7 and 3.2
Tested on Mac OS X 10.6 (Snow Leopard)

## How does it work?
(1.1.1 and earlier)
This is not one of those hack scripts that replaces DefaultDesktop.jpg in the CoreServices folder.  This script edits the plist file that points to this file using the command line tools built into OS X to do so, namely the "defaults" command

Since your home directory, where most of us store out background pictures, it usually unreadable unless you changed permissions, this script copies your background out and stores it as /.LoginBackground and points the plist to this location.

(1.2.0 and later)
I had to use a "hack" method to duplicate functionality in Lion since Lion removed the plist option I had before.  So 1.2.0 in Lion moves the original background, then softlinks /.LoginBackground to where the original background used to be.

## Feedback
it's welcome, I may have overlooked something and there may be a better way to do this.  Get at me on twitter [@nuckin42](http://twitter.com/nuckin42)

## Changes
### Version 1.2.0
Changes:
- This version drops Snow Leopard support
- Adds Lion support
- install/uninstall scripts hold all the sudo-needed commands

### Version 1.1.1
Changes:
- Fixed a typo in the cmd string

### Version 1.1.0
Changes:
- Backgrounds no longer need to be in a public folder
- Python 2.7 support added
- The current background is stored at /.LoginBackground

### Version 1.0.0
Changes:
- it sets your login window background
- Python 3.2 support