def fish(shoal):
    size = 1
    ate = 0
    ate_t = 0
    shoal_list = []
    to_grow = 4
    for fish in shoal:
        shoal_list.append(int(fish))
    to_eat = [1]
    for item in to_eat:
        while item in shoal_list:
            for fish in shoal_list:
                if fish in to_eat:
                    ate += fish
                    ate_t += fish
                    shoal_list.remove(fish)
            while ate >= to_grow:
                size += 1
                ate -= to_grow
                to_eat.append(size)
                to_grow = size * 4
    print(size)
    return size

#27
#fish("318521851111991905670234046287541032388917496474105161342189721856646773677438956815504990664637450190679843349076909465248571932762645988595806041728447572280705235247070635912475255298281305884069857305524216079493551215795763638309398919006392294294550085913506503428739255140028213362666991378918516697888")
#1
#fish("6")
#5
fish("111111111111111111112222222222")
#5
#fish("151128241212192113722321331")