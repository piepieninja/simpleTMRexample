# Simple TMR Example
Some Examples of [Triple Modular Redundancey (TMR)](https://en.wikipedia.org/wiki/Triple_modular_redundancy) for a [UGA SSRL](smallsat.uga.edu) workshop at the 4th annual [UGA Hacks](https://ugahacks.com/), the best hackathon on the planet. The slides accompanying this presentation can be found at [smallsat.uga.edu/research](smallsat.uga.edu/research)

_Disclaimer:_ This is not intended for real use. This is only for demonstration and educational purposes.

#### Dependencies
- numpy
- matplotlib
- PIL (Python Image Library)

## TMR

Fundamentally, TMR is exactly what it says it is. There are 3 copies of something and
you can check values at particular locations to make sure all copies are still equal. If
you notice that the copies are not equal, i.e. one copy is `0` and the other two are `1`,
then you can choose to correct the copy that is  the outlier. As a logic circuite this looks like:

<center>

![](https://github.com/piepieninja/simpleTMRexample/blob/master/img/Majority_Logic.png)

</center>

And logically, assuming your bits are `b0`, `b1`, and `b2`:

![](https://github.com/piepieninja/simpleTMRexample/blob/master/img/Majority_Logic2.png)

In python this could be done with:

```Python
if (not((not (b and b1)) and (not (b1 and b2)) and (not (b0 and b2)))):
  # do some TMR here
```


## Worked Examples

In the `TMR.py` file, located in the root of this directory, there is an example setup to test some TMR algorithms. In this example an image of carl has 1 bitflip occuring every millisecond. This is a large exaggeration, only to demonstrate the concept of TMR. These bitflips can be seen below:

![](https://github.com/piepieninja/simpleTMRexample/blob/master/img/animation.gif)

to attempt to slow the degridation of the image, TMR can be performed. In these examples the TMR algorthm occurs at a slower
rate than bitflips occur. This is does to reflect the reality TMR is only capible of slowing the onslaught of radiation.
