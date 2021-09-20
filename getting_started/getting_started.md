# Raspberry Pi

## Buying Info ##

* [http://www.raspberrypi.org/phpBB3/viewtopic.php?f=45&t=25895RPi Buying Guide](http://elinux.org/RPi_Buying_Guide)
* [Christmas shopping guide | Raspberry Pi](http://www.raspberrypi.org/christmas-shopping-guide/) - December 2014

## Models

* [Raspberry Pi Model B+ Launched Today - RasPi.TV](http://raspi.tv/2014/raspberry-pi-model-b-launched-today)

## Selecting SD Cards

* [Raspberry Pi microSD card performance comparison - 2018](https://www.jeffgeerling.com/blog/2018/raspberry-pi-microsd-card-performance-comparison-2018)
	* Only Samsung and SanDisk cards recommended - all other brands too slow
	* The Samsung Evo+ outshines the rest of the field in 4K random read and random write—two of the most important metrics for common Raspberry Pi use cases
	* The SanDisk Extreme and Samsung Pro+ are also worthy options, but both cost slightly more than the Evo+, and offer slightly less performance overall.
	* In a simpler format, here are my picks for the best microSD cards on the market for use with the Raspberry Pi:
		* [Samsung Evo+](https://www.amazon.com/Samsung-Class-Micro-Adapter-MB-MC32DA/dp/B00WR4IJBE/ref=as_li_ss_tl?s=electronics&ie=UTF8&qid=1523037699&sr=1-4&keywords=samsung+evo+plus&dpID=419o58jbNhL&preST=_SX300_QL70_&dpSrc=srch&linkCode=ll1&tag=mmjjg-20&linkId=8f5797290f6a6ed3dc53159e8b784f73) - $15 on Amazon
		* [SanDisk Extreme](https://www.amazon.com/dp/B06XWMQ81P/ref=as_li_ss_tl?_encoding=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=f7777ae07f3aec259621bdfc999b2303) - $19 on Amazon
		* [Samsung Pro+](https://www.amazon.com/Samsung-Plus-MicroSDHC-Memory-Write/dp/B01273L37G/ref=as_li_ss_tl?s=electronics&ie=UTF8&qid=1523037862&sr=1-3&keywords=samsung+pro+plus+micro+sd&dpID=41OcqEvr1QL&preST=_SY300_QL70_&dpSrc=srch&linkCode=ll1&tag=mmjjg-20&linkId=9c4b4138c2680eb0e1ecef05438f48c9) - $27 on Amazon


## Getting Started

* [The Always-Up-to-Date Guide to Setting Up Your Raspberry Pi](http://lifehacker.com/the-always-up-to-date-guide-to-setting-up-your-raspberr-1781419054)
* [**Raspberry Pi Learning Resources · GitHub**](https://github.com/raspberrypilearning) - excellent set of resources
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
* [How to Create a New SD Card for Raspberry Pi on Windows](http://www.raspberrypi-spy.co.uk/2017/05/how-to-create-a-new-sd-card-image-for-raspberry-pi-on-windows/)

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
