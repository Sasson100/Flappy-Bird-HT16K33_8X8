This project basically just lets you play flappy bird on an esp32 (and potentionally other Micropython-compatible devices) through an HT16K33_8X8 dot matrix display and a tm1650 digit display (that for some reason has a clk pin and a dio pin)

Files included:
1. typings folder: This includes a copy of [micropython stubs](https://pypi.org/project/micropython-esp32-stubs/), basically just letting most modern IDEs (like VSCode) do hints, auto-complete and type checking for Micropython-exclusive libraries without having to add the libraries themselves into the repository.
2. ht16k33.py and ht16k33matrix.py: libraries for the dot-matrix display, which I got from keyestudio's files.
3. tm1650.py: a copy of keyestudio's files for the tm1650, made into a class, if you're gonna ask me how it actually works, please don't.
4. test.py: A test version of it that prints to the terminal and uses input instead of a button for jumping
5. flappy_bird.py: The main file for the code
