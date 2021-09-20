# Sonic Pi notes

## Info

* [Making Computer Science Audible](http://www.cl.cam.ac.uk/projects/raspberrypi/sonicpi/)
	* [Sonic Pi 1.0 Cheat Sheet](http://www.cl.cam.ac.uk/projects/raspberrypi/sonicpi/media/sonic-pi-cheatsheet.pdf)
* [MIDI Note/Key Number Chart](http://computermusicresource.com/midikeys.html)
* Source code: [samaaron/sonic-pi · GitHub](https://github.com/samaaron/sonic-pi)
* [Sonic Pi v2.0](http://sonic-pi.net/get-v2.0)
* Update to Sonic Pi 2.5 one day

## Learning Sonic Pi

* [Dave Conservatoire](http://www.daveconservatoire.org/course/introduction-to-sonic-pi)

## Examples

* [SonicPiChristmasMedley by rbnman - Hear the worldâs sounds](https://soundcloud.com/rbnman/sonicpichristmasmedley)
	* [Sonic-Pi Christmas Medley 1: The Holly and The Ivy](https://gist.github.com/rbnpi/8275ea63244b0a98aeaa)
	* [Sonic-Pi Christmas Medley 2: Jingle Bells](https://gist.github.com/rbnpi/6032176de271227e6324)
	* [Sonic Pi Christmas Medley 3: SilentNight](https://gist.github.com/rbnpi/eccf3ea23bc55f0f073e)
	* [Sonic Pi Christmas Medley 4: Ding Dong Merrily on High](https://gist.github.com/rbnpi/277d1724fc6f9a4155d1)
	* [Sonic Pi Christmas Medley 5: We Wish You A Merry Christmas](https://gist.github.com/rbnpi/c787e705056bacd0c435)

## Syntax

See [sonic_pi_syntax](editorial://open/Computing/Raspberry%20Pi/programming/sonic_pi/sonic_pi_syntax.md?root=dropbox)

### Basics

Based on Ruby.

	play 60
	sleep 0.5
	play 67

Data structure-based approach - where temp is in beats per minute (BPM):

	with_tempo 150
	play_pattern [60,60,67,67,69,69,67]

With loops - between `do` and `end`:

	with_tempo 150
	2.times do
		play_pattern [60,60,67,67,69,69,67]
		sleep 0.5
	end

Introducing variables

	C=60
	D=62
	play_pattern [C,D,C,D]

Synthesizers: default synch is `pretty_bell`. Others examples are `dull_bell`, `fm`, `beep`, `saw_beep`. You can change by putting something like this before the instructions:

	with_synth "fm"

### Adding comments

Probable: use `#` - or see [How can I comment multiple lines in Ruby?](http://stackoverflow.com/questions/2989762/how-can-i-comment-multiple-lines-in-ruby) for more examples. 

### Randomness

Adding conditionals

	if
	...
	else
	...
	end

Can also scale the value of rand, to play random notes

	play 60 + rand(10)

### Algorithms

Data structures can have algorithms applied:

	[60,72,65,80].sort
	[60,72,65,80].reverse

### Running 2 scripts at once

Use multiple `in_thread do` and `end` blocks

### Odds and ends

Adding a background sound:

	play_pad "woah", 56

Or mouse-controlled - click play and then move mouse around - left/right and up/down:

	control_pad "note", 56

## OSC

### TouchOSC

* [Using TouchOSC with Sonic Pi - Educators - in_thread](https://in-thread.sonic-pi.net/t/using-touchosc-with-sonic-pi/275)
* [h e x l e r . n e t | Documentation | TouchOSC | Introduction](https://hexler.net/docs/touchosc)

Robin Newman's layout - seen at FenJam 1 - using [Cube:Bit](https://shop.4tronix.co.uk/products/cube-bit-magical-rgb-cubes-of-awesome-cubebit):

```
iPad
- Touch OSC
- Sends OSC messages

Pi
- SonicPi
- Receives OSC messages
- Sends OSC messages

PiZero
- Connected to LED cube
- Python Script listening to OSC commands, some of which are primitives
- Sends those primitives to the cube
```


## Internals

* ["Beating Threads - live coding with real time" by Sam Aaron - YouTube](https://m.youtube.com/watch?feature=youtu.be&v=YlRTTzlhquo) - 05' 40"
* *See also [sonic_pi_development](editorial://open/Computing/Raspberry%20Pi/programming/sonic_pi/sonic_pi_development.md?root=dropbox)*.