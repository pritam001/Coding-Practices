import sys
heavy_ball = 0
finished = False

while not finished:
    print "1"
    sys.stdout.flush()
    print "2 1 2"
    sys.stdout.flush()
    print "2 3 4"
    sys.stdout.flush()
    line = int(raw_input())
    if line == 0:
        finished = True
        heavy_ball = 5
        break
    if line > 0:
        print "1"
        sys.stdout.flush()
        print "1 1"
        sys.stdout.flush()
        print "1 2"
        sys.stdout.flush()
        line1 = int(raw_input())
        if line1 > 0:
            finished = True
            heavy_ball = 1
            break
        else:
            finished = True
            heavy_ball = 2
            break
    if line < 0:
        print "1"
        sys.stdout.flush()
        print "1 3"
        sys.stdout.flush()
        print "1 4"
        sys.stdout.flush()
        line1 = int(raw_input())
        if line1 > 0:
            finished = True
            heavy_ball = 3
            break
        else:
            finished = True
            heavy_ball = 4
            break

print "2"
print heavy_ball
