This project basically just lets you play flappy bird on an esp32 (and potentionally other Micropython-compatible devices) through an HT16K33_8X8 dot matrix display and a tm1650 digit display (that for some reason has a clk pin and a dio pin)

Files included:
1. typings folder: This includes a copy of [micropython stubs](https://pypi.org/project/micropython-esp32-stubs/), basically just letting most modern IDEs (like VSCode) do hints, auto-complete and type checking for Micropython-exclusive libraries without having to add the libraries themselves into the repository.
2. ht16k33.py and ht16k33matrix.py: libraries for the dot-matrix display, which I got from [lesson 38](https://www.dropbox.com/scl/fo/hv1iw3z9094d5rs7qds8q/AIa31qqJDJWj-5ROq9diAdY/Windows/MicroPython/2.%20ESP32_code_MicroPython/lesson%2038.%20HT16K33%20dot%20matrix?rlkey=24sox2xp675n2dcbgfd3t28yd&subfolder_nav_tracking=1&st=jq4y1cfo&dl=0) of [keyestudio's KS5005 kit's files](https://fs.keyestudio.com/KS5005-5006).
3. tm1650.py: a copy of [lesson 37](https://www.dropbox.com/scl/fo/hv1iw3z9094d5rs7qds8q/AJYHHLkDLZ0IcDWsgYAY1QQ/Windows/MicroPython/2.%20ESP32_code_MicroPython/lesson%2037.%20TM1650%20Four%20digital%20tube?rlkey=24sox2xp675n2dcbgfd3t28yd&subfolder_nav_tracking=1&st=gfc8wfhu&dl=0)'s files (from the same place), made into a class, if you're gonna ask me how it actually works, please don't.
4. test.py: A test version of it that prints to the terminal and uses input instead of a button for jumping
5. flappy_bird.py: The main file for the code

