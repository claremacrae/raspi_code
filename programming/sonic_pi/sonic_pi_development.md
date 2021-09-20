# Sonic Pi Development

This work was  being done on `sd\_05\_raspi2\_noobs1\_4\_0\_raspian\_log`, which is now archived to `"E:\SD Card Backups\sd_05_raspi2_noobs1_4_0_raspian_backup.img"`

## Building Sonic Pi

* [sonic-pi/INSTALL.md](https://github.com/samaaron/sonic-pi/blob/master/INSTALL.md)

----

## Issue 576

2015-07-17  bug: [log appears to be a CPU hog on low powered machines (RP1) · Issue #576 · samaaron/sonic-pi · GitHub](https://github.com/samaaron/sonic-pi/issues/576)

### Reproduction on PC

* **Can I repro on PC with 2.5?**
	* No - both seem to give similar load

### Reproduction on RasPi

All tests are on 'sd_05_raspi2_noobs1_4_0_raspian'

*  **Can I repro on RasPi 2?**
	*  Background activity (with Sonic Pi server running): 0-2% 
	*  Run 1st code (with logging) - after 80 seconds, CPU was up to 8-12%
	*  Run 2nd code (without logging): ca 3%
*  **Can I repro on RasPi B?**
	*  Background activity: 8 - 25%
	*  Run 1st code (with logging): 50 - 70% CPU
	*  Run 2nd code (without logging): ca 35-40%
*  **Can I repro on RasPi A+?**
	*  Background activity (with Sonic Pi server running): 6% 
	*  Run 1st code (with logging): 70-80% CPU
	*  Run 2nd code (without logging): 40-50%

----

## Building Sonic Pi on Raspberry Pi

* Try building on RasPi 2
* Based on https://github.com/samaaron/sonic-pi/blob/master/INSTALL.md#raspberry-pi, installed - or tried to install:
	* supercollider ruby1.9.3 libqscintilla2-8 libqscintilla2-dev qt4-dev-tools cmake ruby-dev libffi-dev
* Gave lots of errors
* After `sudo apt-get update`, and try again it was fine
* My clone is: [https://github.com/claremacrae/sonic-pi](https://github.com/claremacrae/sonic-pi)
* And it actually built Sonic Pi fine, using:

```
#---------------------------------
# On PC:
# to get changes from me or Sam:
git pull samaaron master
git push origin master
#---------------------------------
# On Raspberry Pi:
cd ~/develop/sonic_pi
git pull remote master
#---------------------------------
cd ~/develop/raspi_code/setup
./setup_sonicpi_dev.sh
./build_sonic_pi_dev.sh
#---------------------------------
cd ~/develop/sonic_pi
git push origin master
```

See also [Git - Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)

* `[x]` Work through Will Stephenson's timing suggestions
* `[x]` Add timer printouts/measurements debug output to the code, so I can do repeated runs, and collect numbers
* `[=]` Try commenting out various bits of the code, to do poor-person's timing
* `[=]` Try moving all the calls to update the log to a method in the log's thread

### QtCreator on Raspberry Pi 

* `[=]` Try getting Qt Creator working on Raspberry Pi 
	* [qt creator Raspberry Pi - Google Search](https://www.google.co.uk/search?q=qt+creator+Raspberry+Pi+&gws_rd=cr,ssl&ei=5bO6VcCrB4GmUJ_nhLgD)
	* Try via installing via [Finding out what is installed on your Pi, and installing more | The Pi Hut](http://thepihut.com/blogs/raspberry-pi-tutorials/16998732-finding-out-what-is-installed-on-your-pi-and-installing-more)
* This worked (actually done via synaptic package manager):
	* `sudo apt-get install qtcreator qtcreator-dbg qtcreator-doc`
* Then ran qtcreator, and loaded `sonic-pi/app/gui/qt/SonicPi.pro`
	* It doesn't understand the toolset
	* But I can still build via my own `build_sonic_pi_dev.sh`


### Profiling Performance on Raspberry Pi 

* [Raspberry Pi • View topic - Profiling on the Pi?](https://www.raspberrypi.org/forums/viewtopic.php?f=33&t=19151)
* [gperftools - Fast, multi-threaded malloc() and nifty performance analysis tools - Google Project Hosting](https://code.google.com/p/gperftools/)
* [How to use the profiler in c++ with raspberry pi 2 - Stack Overflow](http://stackoverflow.com/questions/31368884/how-to-use-the-profiler-in-c-with-raspberry-pi-2)
* [unix - What can I use to profile C++ code in Linux? - Stack Overflow](http://stackoverflow.com/questions/375913/what-can-i-use-to-profile-c-code-in-linux/378024#378024)

----

## Building Sonic Pi on Windows

* See [Sam Aaron's Instructions](https://github.com/samaaron/sonic-pi/blob/master/INSTALL.md#windows)
* QScintilla
	* What does 'Grab a copy of the [QScintilla libs](http://www.riverbankcomputing.co.uk/software/qscintilla/download) and unzip it in your apps directory' mean?
	* See 'Installation' in [QScintilla docs](http://pyqt.sourceforge.net/Docs/QScintilla2/)
	* I've set up build of this in there - and it copied DLLs in to Qt:
		* `D:\Users\Clare\Documents\Programming\Tools`
* Server extensions

```
D:\Users\Clare\Documents\Programming\Tools\setup_ruby.bat
cd /d/Users/Clare/Documents/Programming/github/sonic-pi
ruby app/server/bin/compile-extensions.rb
```
* ~~ERROR: CMake is required to build Rugged.~~
* ERROR: pkg-config is required to build Rugged.
* Problems logged in [ Installation instructions for building Sonic Pi on Windows need to be updated. #563 ](https://github.com/samaaron/sonic-pi/issues/563)

----

## Git stuff

* Get Sam's latest code:
	* `git pull samaaron master`
