def timeChange(t1):
    # 3 conditions
    '''check if its midnight
        check if its AM
        check if its noon
        check if it PM
    '''
    if t1[-2:] == "AM" and t1[:2] == "12":
        return "00" + t1[2:-2]
    elif t1[-2:] == "AM":
        return t1[:-2]
    elif t1[-2:] == "AM" and t1[:2] == "12":
        return t1[:-2]
    else:
        return str(int(t1[:2])+12) + t1[2:-2]


if __name__ == '__main__':
    time = input()
    print(timeChange(time))
