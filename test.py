from random import randint

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
        for y in [*range(height), *range(height + 2, 8)]
    ]

def render():
    image = [[0 for _ in range(8)] for _ in range(8)]
    image[bird_height][1] = 1
    for point in pipe_points():
        image[point[1]][point[0]] = 1
    for row in image[::-1]:
        print(row)
    print("")

while True:
    frame_count +=1
    print("Frame number",frame_count)
    if frame_count == 1:
        render()
        continue

    jump_input = input("Want to jump next frame? ").lower()
    while jump_input not in ("y","n","yes","no"):
        print("""\
            Bad input, the only accepted values are:
            y, yes, n, no
        """)
        jump_input = input("Want to jump next frame? ")
    
    if jump_input in ("y","yes"):
        bird_jumped = True
        bird_jumped_at = frame_count
    elif frame_count>bird_jumped_at+1:
        bird_jumped = False

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
    if bird_height<0:
        print("Game over: Fell out of the world")
        break
    elif (1,bird_height) in pipe_points():
        print("Game over: Ran into a pipe")
        break

    # Gaining points
    if pipe_x_values[0] == 1:
        points += 1