# Raspberry Pi Camera Module Notes

## Hardware

* Camera Module
    * [Camera articles on Raspberry Pi website](http://www.raspberrypi.org/archives/tag/camera-module)
    * [How to set up the camera hardware](http://www.raspberrypi.org/camera) - contains a useful list of example commands
    * [Rpi Camera Module](http://elinux.org/Rpi_Camera_Module) - excellent reference page at elinux.org
* Raspberry Pi Camera cases
    *  [RaspberryPi and camera cases round-up](http://www.recantha.co.uk/blog/?p=5351) - @recantha - 29 July 2013
* Infrared Camera
    * [Announcement of Infrared camera](http://www.raspberrypi.org/archives/5089) 
* Pimoroni Camera Mount
	* [Raspberry Pi Camera Mount](http://shop.pimoroni.com/products/raspberry-pi-camera-mount?utm_source=googlepla&utm_medium=cpc&gclid=COjMldva1bsCFUnjwgodJl0AFg) 
	* [Assembling the Camera Mount](http://shop.pimoroni.com/blogs/help/7987155-assembling-the-camera-mount)
		* Missing instructions
			* Remember to ground yourself, before handling the camera module
			* Peel off the thin plastic sheeting before assembly
			* Do a test run of putting nuts on to screws - and try putting the nut all the way on and off - then pick the best four matches
		* this was *really* fiddly to attach the screws, especially whilst avoiding touching the camera electronics
		* there were 5 screws and 8 nuts - several combinations of which didn't fit together smoothly at all
		* And the supporting plate didn't fit comfortably into the side notches - and when I applied a tiny amount of pressure, one of the "legs" on the base plate snapped off 
			* It turned out that this was not helped by my not knowing to peel off the white plastic sheeting
		* The instructions say to use `-vf` to fix the orientation, but this produces a reflected image
		* The correct option is actually `-rot 180`
* [ModMyPi | RPi Camera Board 360 Gooseneck Mount](https://www.modmypi.com/flexible-camera-mount)
	*  [ModMyPi | Raspberry Pi Camera](https://www.modmypi.com/raspberry-pi-camera)
*  [Camera board extension - Raspberry Pi](https://www.raspberrypi.org/camera-board-extension/)

## Software

* Software for programming
    * [A pure Python interface for the Raspberry Pi camera module.](https://pypi.python.org/pypi/picamera/)
    * [A pure Python interface for the camera module: meet picamera! | Raspberry Pi](http://www.raspberrypi.org/archives/5672)
* BerryCam - iPhone software
    * [BerryCam: use your Raspberry Pi camera board with your iPhone](http://www.raspberrypi.org/archives/4791)
    * [BerryCam support](http://www.fotosyn.com/berrycam-support/)
        * But don't use `sudo` as it'll make root own all the photos - it works fine without sudo for me. 
    * [BerryCam on BitBucket](https://bitbucket.org/fotosyn/fotosynlabs/src/9819edca8927/BerryCam?at=master)
* Picamera
    * [Documentation for picamera — Picamera 1.7 documentation](https://picamera.readthedocs.org/en/release-1.7/)
* [An Efficient And Simple C++ API for the Rasperry Pi Camera Module](http://robotblogging.blogspot.co.uk/2013/10/an-efficient-and-simple-c-api-for.html?m=1)
* Time lapse photography
    * [Raspberry Pi - Timelapse photography and encoding](http://www.youtube.com/watch?v=C2b4aIirE48&feature=c4-overview&list=UURAvo5cQWyfog8nRzlf_jWg)
    * [Simple timelapse camera using Raspberry Pi and a coffee tin](http://www.instructables.com/id/Simple-timelapse-camera-using-Raspberry-Pi-and-a-c/?ALLSTEPS) 
* Stop motion animation
    * [Push Button Stop Motion](http://www.raspberrypi.org/learning/push-button-stop-motion/worksheet.md)

## Other people's projects

* [Winter on Georgian Bay | Inventing Situations.](http://inventingsituations.net/2014/05/16/winter-on-georgian-bay/)
* [Accessing the Raspberry Pi Camera with OpenCV and Python](http://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python)
* [Kite mapping - Raspberry Pi](https://www.raspberrypi.org/kite-mapping/)

## RasPi Camera project ideas

* [Build a wildlife camera with your #RaspberryPi | Raspberry PiPod](http://www.recantha.co.uk/blog/?p=10133)
