# L-Systems

Hello! This is the code for my (at the time of writing this unreleased)
Computerphile video.

![](screenshot.png)

It runs user-defined L-systems using Python's `turtle` module, and also can
simulate graphical effects such as random angles and segment lengths, and
tropism (where the plant points towards the "sun").

## Quickly getting started

If you just want to see pretty pictures, follow these steps:

 1. [Install Python](https://www.python.org/downloads/) if you haven't already.
 2. Download this repository (either via [cloning it](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) or just [downloading it directly as a ZIP](https://github.com/zac-garby/lsystems/archive/refs/heads/master.zip)).
 3. Install the TkInter graphics library if if you don't have it.
      - Windows: Should be installed with python. If not, run 'pip install tk' in comand prompt.
      - MacOS: Easiest to do by running 'brew install python-tk' if you have [homebrew](https://brew.sh/).
      - Linux: Package name differs between 'tk', 'python3-tkinter', 'python-tk' among others, depending on your distribution.
 4. Run the Python script `lsystem.py`.
    - Through the command line, this is `python3 lsystem.py`.
    - You might be able to just double click the file - I'm not sure.
    - You'll be asked for which system to see, type the name of the given system and press enter.
 5. That's it! I'd recommend full-screening the window, then press ENTER a few
    times to advance the simulation.
    - You can go into "slow mode" by pressing DOWN (and back to fast by pressing
      UP) if you want to show the image as it is being drawn.

## Making your own L-system

If you want to make your own L-system, follow these steps:

 1. Download the Python script as described previously.
 2. Open `lsystem.py` in your editor of choice and scroll down to line 92. There are lots of L-systems defined here, the custom default of which is currently a copy of "cow parsley", between lines 171 and 198.
 3. Edit the rules to your liking!
    - The rules are defined as a Python dictionary in `rules`.
    - The turning angle is defined as a float in `angle`.
    - The initial/seed sequence is defined in `axiom`.
    - Any upper-case letter is interpreted as a stem segment.
    - `[` and `]` are interpreted as described in the video (i.e. branching).
    - `-` and `+` are interpreted as rotation left and right by `angle`.
    - Any other symbols are skipped while drawing the picture, so they can be used for "structural elements" (see the Hilbert curve).

## Using the funky rendering features

I've implemented a few things here which can make your drawings look more realistic and lifelike. Once you've defined an L-system, you can play with these variables:

 - `tropism_angle`: the angle to turn towards as if pointing at the sun. Measured counter-clockwise in degrees from due east.
 - `tropism_amount`: the amount of tropism to apply at each turn. This should usually be very small, like 0.05 or such. Setting this to 0 turns off tropism, and is the default value.
 - `angle_random_variation`, `length_random_variation`: the amount by which the rotation angle and the segment length should vary. Given as the standard deviation of a normal distribution about the means `angle` and `line_length` respectively.
 - `bud_symbols`: a string containing symbols which should be interpreted as flower buds (i.e. which should render with a white circle at the end).
 - `default_pen_size`: the thickness of the stem lines (default 2).
 - `line_length`: the mean segment length (default 10).
 - `start_pos`: the position on the screen to start at, as a tuple. The screen opens as an 800x800 window, and `(0, 0)` is the center (default `(0, -380)`).
 - `sub_chance`: the probability that each rule substitution will take place. Default 1.0. Reducing this can lead to some cool effects.

## Getting help

If you have any trouble at all setting this up, feel free to email me or simply raise an issue on this repository and I'll help you out.
