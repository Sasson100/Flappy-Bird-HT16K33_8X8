from machine import I2C, Pin
from ht16k33matrix import HT16K33Matrix
from tm1650 import TM1650
import time
from random import randint

display = HT16K33Matrix(I2C(scl=Pin(5), sda=Pin(18)))
tm = TM1650(19,21)
button = Pin(23, Pin.IN, Pin.PULL_UP)

display.set_brightness(2)
tm.displayDot(2,1)
tm.displayDot(3,1)

bird_height = 3
bird_jumped = False
bird_jumped_at = 0

pipe_heights = [randint(1,5)] # Refers specifically to the lower pipe
pipe_x_values = [7]

frame_count = 0
points = 0

def pipe_points():
    return [
        (x, y)
        for x, height in zip(pipe_x_values, pipe_heights)
        for y in list(range(height)) + list(range(height + 2, 8))
    ]

def render():
    image = [[0 for _ in range(8)] for _ in range(8)]
    image[bird_height][1] = 1
    for point in pipe_points():
        image[point[1]][point[0]] = 1
    image = [row[::-1] for row in image[::-1]]
    image = bytes([
        int("".join(map(str, bits)), 2)
        for bits in image
    ])
    display.set_icon(image).draw()

def restart():
    global bird_height, bird_jumped, bird_jumped_at, pipe_heights, pipe_x_values, frame_count, points
    bird_height = 3
    bird_jumped = False
    bird_jumped_at = 0
    pipe_heights = [randint(1,5)] # Refers specifically to the lower pipe
    pipe_x_values = [7]
    frame_count = 0
    points = 0

while True:
    frame_count +=1
    
    if frame_count != 1:
        # Bird logic
        if bird_jumped:
            bird_height += 1
            bird_height = min(bird_height,7)
        else:
            bird_height -= 1
        
        # Pipe logic
        pipe_x_values = [pos - 1 for pos in pipe_x_values]
        if pipe_x_values[0]<0:
            del pipe_x_values[0]
            del pipe_heights[0]
        if frame_count%3 == 1:
            pipe_x_values.append(7)
            pipe_heights.append(randint(1,5))
    
    render()

    # Game over logic
    if bird_height<0 or (1,bird_height) in pipe_points():
        tm.display(2,[0,0,1,1,1,0,0,0])
        tm.clearBit(1)
        time.sleep(1)
        while button.value() == 1:
            pass
        restart()
        continue

    # Gaining points
    if pipe_x_values[0] == 1:
        points += 1
        if points == 100:
            tm.display(4,[0,1,1,1,0,0,1,1])
            tm.display(3,[0,1,1,1,0,1,1,1])
            tm.display(2,[0,1,1,0,1,1,0,1])
            tm.display(1,[0,1,1,0,1,1,0,1])
            time.sleep(1)
            while button.value() == 1:
                pass
            restart()
            continue
        tm.ShowNum(points,3)
    
    # Jumping logic
    end_time = time.time_ns()+2*(10**9)
    while time.time_ns()<end_time:
        t = (end_time-time.time_ns())/(10**9)
        tm.ShowNum(num = int(t%1*10), bit = 1, clear_rest = False)
        tm.ShowNum(num = int(t), bit = 2, clear_rest = False)
        tm.ShowNum(points,3)
        if button.value() == 0 and 2-t>.25:
            bird_jumped = True
            bird_jumped_at = frame_count
            break

    if button.value() == 1 and frame_count>bird_jumped_at+1:
        bird_jumped = False