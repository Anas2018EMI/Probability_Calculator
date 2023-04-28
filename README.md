# Probability_Calculator

This is a script of a probability problem. Instead to resolve the problem mathematically, the script resolves it empirically, thanks to computing power, by executing random experiments many times.

The problem consists of having a hat which contain some balls with different colors. Then we will draw randomly a certain number of balls from the hat. The assignment is to calculate the probability of having a certain set of balls.
 
For example, if you want to determine the probability of getting at least two red balls and one green ball when you draw five balls from a hat containing six black, four red, and three green. To do this, you will perform N experiments, count how many times M you get at least two red balls and one green ball, and estimate the probability as M/N. Each experiment consists of starting with a hat containing the specified balls, drawing several balls, and checking if you got the balls you were attempting to draw.

Here is how you would call the experiment function based on the example above with 2000 experiments:

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
