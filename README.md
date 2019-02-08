# Simple TMR Example
Some Examples of [Triple Modular Redundancey (TMR)](https://en.wikipedia.org/wiki/Triple_modular_redundancy) for a [UGA SSRL](smallsat.uga.edu) workshop at the 4th annual [UGA Hacks](https://ugahacks.com/), the best hackathon on the planet. The slides accompanying this presentation can be found at [smallsat.uga.edu/research](smallsat.uga.edu/research)

_Disclaimer:_ This is not intended for real use. This is only for demonstration and educational purposes.

#### Dependencies
- numpy
- matplotlib

## TMR

![](https://github.com/piepieninja/simpleTMRexample/blob/master/img/Majority_Logic.png)

## Worked Examples

In the `TMR.py` file, located in the root of this directory, there is an example setup to test some TMR algorithms. In this example an image of carl has 1 bitflip occuring every millisecond. This is a large exaggeration, only to demonstrate the concept of TMR. These bitflips can be seen below:

![](https://github.com/piepieninja/simpleTMRexample/blob/master/img/animation.gif)

to attempt to top degridation of the image, TMR must be performed
