

brd = [[0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	1, 	0],
[0, 0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	1],
[0, 0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0],
[0, 0, 	0, 	0, 	0, 	1, 	1, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0],
[0, 0, 	0, 	0, 	1, 	0, 	1, 	1, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0],
[0, 0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0],
[0, 0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0],
[0, 0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0],
[0, 0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0],
[0, 0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0],
[0, 0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0],
[0, 0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0],
[0, 0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0],
[0, 0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0],
[0, 0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0],
[0, 0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0],
[0, 0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0],
[0, 0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0],
[0, 0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0],
[0, 0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0],
[0, 0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0, 	0]]

if not brd == None:
    new_brd = brd
    vln_brd = len(new_brd)
    hln_brd = len(new_brd[0])
    # print(vln_brd, hln_brd)

def print_brd(mbrd):
    for line in mbrd:
        for line_cell in line:
            # if line_cell ==1:
            print(line_cell, end = " ")
        print(" ")

def Check_for_Life(x_brd, m_line, m_cell):
    ln_range = range(max(m_line - 1,0), min(vln_brd, m_line + 2))
    cl_range = range(max(m_cell - 1,0), min(hln_brd, m_cell + 2))

    # print("ln_range= ", ln_range)
    # print("cl_range= ", cl_range)
    live_neighbours = 0
    active_cell = bool
    lives = int

    # calculate neighbours of the target cell
    for x in ln_range:
        # print("x=", x)
        for y in cl_range:
            # print("y=",y)
            if x ==m_line and y == m_cell:
                # print("x", end = " ")
                active_cell = x_brd[x][y]
            else:
                live_neighbours = live_neighbours + x_brd[x][y]
                #print(x_brd[x][y], end = " ")
        # print(" ")

    # print("active cell?", active_cell)
    # print("live_neighbours?", live_neighbours)

    if active_cell and live_neighbours in (2,3):
        lives = 1
    elif not active_cell and live_neighbours == 3:
        lives = 1
    else:
        lives = 0

    return lives

print_brd(new_brd)


iteration = 0


while iteration <=5:
    print("------")
    for x in range(vln_brd):
        for y in range(hln_brd):
            # print(x,y)
            a = Check_for_Life(brd,x,y)
            # print("***:", Check_for_Life(brd,x,y))
            new_brd[x][y] = a
    brd = new_brd.copy()
    #print("------")
    iteration = iteration + 1

    # call('clear')
    # os.system('clear')
    print_brd(new_brd)
