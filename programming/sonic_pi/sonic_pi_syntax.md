# sonic_pi_syntax

*See [sonic_pi_notes](editorial://open/Computing/Raspberry%20Pi/programming/sonic_pi/sonic_pi_notes.md?root=dropbox)*

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
