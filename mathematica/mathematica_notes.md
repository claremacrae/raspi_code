# Mathematica

## Running on the command line

* Can run scripts in batch command

    math

Except that this does exist on the current NOOBS (1.3.3?)

## Mathematica program

* Use Get["filename.m"] to load files
* e.g. Get["raspi_code/mathematica/sin_chart.m"]
* Type expression, then hit  Shift + Enter (or Evaluation -> Evaluate Cells)
* Example expressions
    * 42^42
    * N[Pi,200] # Pi to 200 digits (i.e. 2 decimal places)
    * Integrate[1/(1 + x^2), {x, 0, Infinity}]
    * Plot[Sin[x], {x, 0, 10}]
    * Or create and save a plot:
        * gr = Plot[Sin[x], {x, 0, 10}]
        * Export["test.png", gr] # Goes in home directory
        * Export["test.png", gr] // AbsoluteTiming # That option means timing info is written out
