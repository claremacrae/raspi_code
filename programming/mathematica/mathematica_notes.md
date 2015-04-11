# Mathematica

## Info and useful links

* [Mathematica and the Wolfram Language on Raspberry Pi](http://www.raspberrypi.org/archives/5623) - 02/01/2014
* Mathlink allows communication with other programs
* [Tutorial Collection](http://www.wolfram.com/learningcenter/tutorialcollection/)
* [Mathematica 10 – now available for your Pi! | Raspberry Pi](http://www.raspberrypi.org/mathematica-10/) - 01/08/2014

## Wolfram Language

* [Stephen Wolfram's Introduction to the Wolfram Language - YouTube](http://m.youtube.com/watch?v=_P9HqHVPeik)

## Running on the command line

* Can run scripts in batch command

	    math

Except that this does exist on the current NOOBS (1.3.3?)

## Reference

### Tips

* `Shift + Enter` to calculate
* Or just `Enter` on numeric keypad
* `Ctrl + L` to recall last input
* Accessing previous results
	* `%` is result of output from last calculation
	* `%%` is next-to-last result
	* `Out[27]` = output of 27th calculation
	* `%n` is result on output line `Out[n]`
* Get instant info about built-in function: Type `?` and function name, then `Shift + Enter`
* To complete a partially typed command name, `Ctrl + K`
* To see a function template for a given function, press `Shift+Ctrl+K`
* To abort a calculation, press Alt+.
* A `;` at end of line suppresses output, but the command is still evaluated.
* Append `//N` to get an approximate numeric result, e.g. instead of a fraction
* `N[ expression, 40 ]` gives result with 40 significant digits
* Presence of explicit decimal point e.g. `Sqrt[2.]` also gives an approximate numeric result
* When you have finished with a symbol, e.g. f, use `Clear[f]` afterwards, to remove it

### Variables

* Naming conventions
	* Objects have names starting with a capital
	* Variable names start with lower case

### Functions 

Defining function:

	f[x_] := x^2

Using the function

	f[4]
	f[3 x + x^2]
	Expand[f[(x + 1 + y)]]

## Mathematica program

* Use `Get["filename.m"]` to load files
* e.g. `Get["raspi_code/mathematica/sin_chart.m"]`
* Type expression, then hit `Shift + Enter` (or Evaluation -> Evaluate Cells)
* Example expressions
    * `42^42`
    * `N[Pi,200]` # Pi to 200 digits (i.e. 2 decimal places)
    * `Integrate[1/(1 + x^2), {x, 0, Infinity}]`
    * `Plot[Sin[x], {x, 0, 10}]`
    * Or create and save a plot:
        * `gr = Plot[Sin[x], {x, 0, 10}]`
        * `Export["test.png", gr]` # Goes in home directory
        * `Export["test.png", gr] // AbsoluteTiming` # That option means timing info is written out
