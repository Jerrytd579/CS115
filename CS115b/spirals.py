import turtle

def square_spiral(walls):
    def square_spiral_helper(walls, distance, initial, count):
        if count == walls:
            turtle.done()
        else:
            turtle.left(90)
            turtle.forward(distance)
            square_spiral_helper(walls, distance + initial * (count % 2), initial, count + 1)
    square_spiral_helper(walls, 20, 20, 0)


def octognoal_spiral(walls):
    def octogonal_spiral_helper(walls, distance, initial, count):
        if count == walls:
            turtle.done()
        else:
            turtle.left(45)
            turtle.forward(distance)
            octogonal_spiral_helper(walls, distance + initial * (count % 2), initial, count + 1)
    octogonal_spiral_helper(walls, 20, 5, 0)


# square_spiral(100)
octognoal_spiral(100)