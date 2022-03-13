
glass_size = int(input())
straw_pos = int(input())



#calculating step number
step = int(glass_size-(straw_pos/2)+2)
#main function
def fun(glass_size,straw_pos,step):
    #base condition
    if step == 0:
        return

    fun(glass_size, straw_pos, step - 1)

    #drawing the straw
    def straw(strawloop1):
        if strawloop1 == 0:
            return

        def straw2(strawloop1):
            if strawloop1 == 1:
                return
            print(' ', end='')
            straw2(strawloop1 - 1)



        straw2(strawloop1)
        print('o')
        straw(strawloop1 - 1)

    straw(straw_pos)

    #drawing the glass then filling it according to the step number
    def glasstime(size):
        if size == 0:
            return

        def spaceloop(size):
            if size == 1:
                return
            print(' ', end='')
            spaceloop(size - 1)

        glasstime(size - 1)
        spaceloop(size)

        print('\\', end='')
        if size+1 > step:
            def fullfil(number):
                print('*', end='')
                if number == 0:
                    return

                fullfil(number-1)
            fullfil((glass_size*2)-(size*2)+1)

        else:
            def emptiness(number):
                if number == 0:
                    return

                print(' ', end='')
                emptiness(number-1)

            emptiness(straw_pos-1)
            print('o', end='')

            emptiness((glass_size*2)-(size*2)-straw_pos+2)



        print('/')


    glasstime(glass_size)


    #drawing the connection between holder and the glass
    def easyholder(size):
        if size == 0:
            return
        print(' ', end='')
        easyholder(size-1)

    easyholder(glass_size)
    print('--')

    #drawing the holder
    def hardholder(glass_size, repeat):
        if repeat == 0:
            return

        def hardholder2(size):
            if size == 0:
                return
            print(' ', end='')

            hardholder2(size - 1)

        hardholder2(glass_size)
        print('||')
        hardholder(glass_size, repeat - 1)

    hardholder(glass_size, glass_size)

fun(glass_size,straw_pos,step)




