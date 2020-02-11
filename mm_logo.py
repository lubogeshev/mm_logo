def draw_mm(n: int):
    dash = '-'
    star = '*'
    d_side_cnt = n
    d_mid_cnt = n
    s_side_cnt = n
    s_mid_cnt = n

    middle = (n + 1) // 2

    for i in range(n + 1):
        if i < middle:
            print((dash * d_side_cnt + star * s_mid_cnt + dash * d_mid_cnt
                   + star * s_mid_cnt + dash * d_side_cnt) * 2)
            d_side_cnt -= 1
            if i < middle - 1:
                d_mid_cnt -= 2
                s_mid_cnt += 2
        else:
            print((dash * d_side_cnt + star * s_side_cnt + dash * d_mid_cnt
                   + star * s_mid_cnt + dash * d_mid_cnt + star * s_side_cnt + dash * d_side_cnt) * 2)
            d_side_cnt -= 1
            d_mid_cnt += 2
            s_mid_cnt -= 2


def main():
    n = int(input())
    draw_mm(n)


if __name__ == '__main__':
    main()
