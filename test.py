def decorate(a, b):

    def wrapper(x):
        return a*x + b

    return wrapper


line = decorate(1, 1)
y0 = line(0)
y1 = line(1)
y2 = line(2)      

print("y0, y1, y2 ", y0, y1, y2)
