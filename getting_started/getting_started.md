# Raspberry Pi

## Buying Info ##

* [http://www.raspberrypi.org/phpBB3/viewtopic.php?f=45&t=25895RPi Buying Guide](http://elinux.org/RPi_Buying_Guide)
* [Christmas shopping guide | Raspberry Pi](http://www.raspberrypi.org/christmas-shopping-guide/) - December 2014

## Models

* [Raspberry Pi Model B+ Launched Today » RasPi.TV](http://raspi.tv/2014/raspberry-pi-model-b-launched-today)

## Getting Started

* [Raspberry Pi: Up and Running](http://blog.makezine.com/video/raspberry-pi-up-and-running/) - very good introductory video, from Make
* [Makezine Raspberry Pi section](http://blog.makezine.com/category/electronics/raspberry-pi/)
* [Raspberry Pi Wiki Hub](http://elinux.org/RPi_Hub)
	* [RPi Basic Setup](http://elinux.org/RPi_Hardware_Basic_Setup)
	* [Keyboard Maven*: Raspberry Pi 'Gotchas' and new buyer tips](http://www.keyboardmaven.com/2013/04/raspberry-pi-gotchas-and-newbiebuyer.html)
	* [RPi Hardware Basic Setup - eLinux.org](http://elinux.org/RPi_Hardware_Basic_Setup)
	* [RPi Easy SD Card Setup](http://elinux.org/RPi_Easy_SD_Card_Setup)
* [Fitting the case - video](http://www.youtube.com/watch?v=yRbfQCxEWYs)
* [RaspbianFAQ - Raspbian](http://www.raspbian.org/RaspbianFAQ)
* [How To Format Pi SD Cards Using SD Formatter | Raspberry Pi Spy](http://www.raspberrypi-spy.co.uk/2015/03/how-to-format-pi-sd-cards-using-sd-formatter/)
* **[NOOBS](http://www.raspberrypi.org/archives/4100) - much easier getting started**
* [Ultimate Raspberry Pi Configuration Guide](http://www.instructables.com/id/Ultimate-Raspberry-Pi-Configuration-Guide/?ALLSTEPS)

## Connecting up

From [Connecting Together](http://elinux.org/RPi_Hardware_Basic_Setup#Connecting_Together):

You can use the diagram to connect everything together, or use the following instructions:

1. Plug the preloaded SD Card into the Pi.
1. Plug the USB keyboard and mouse into the Pi, perhaps via a USB Hub. Connect the Hub to power, if necessary.
1. Plug the video cable into the screen (TV) and into the Pi.
1. Plug your extras into the Pi (USB WiFi, Ethernet cable, hard drive etc.). This is where you may really need a USB Hub.
1. Ensure that your USB Hub (if any) and screen are working.
1. Plug the power source into the main socket.
1. With your screen on, plug the other end of the power source into the Pi.
1. The Pi should boot up and display messages on the screen. 

It is always recommended to connect the MicroUSB Power to the unit last (while most connections can be made live, it is best practice to connect items such as displays and other connections with the power turned off).

If you use both a R-PI power supply and a powered hub, **it's recommended you connect them to the same switched power bar, and use the switch on the power bar to switch off both the R-PI and hub at the exact same time**.

Also, always shutdown using the software shutdown function, not by pulling the plug. When not using a GUI, (with a GUI use the GUI command) you can use the command "**shutdown -h now**", and power off when all the LED's on the board (except the power LED) go off. This is especially important the first time you boot, as in the process the R-PI modifies the content of the SD-card, without a clean shutdown the contents of the card may be damaged.

The RPi may take a long time to boot when powered-on for the first time, so be patient, and cleanly shutdown afterwards, as described above! 
