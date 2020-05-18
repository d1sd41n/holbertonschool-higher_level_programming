#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    divs = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            divs.append(div)
        except TypeError:
            print("wrong type")
            divs.append(0)
        except ZeroDivisionError:
            print("division by 0")
            divs.append(0)
        except IndexError:
            print("out of range")
            divs.append(0)
        finally:
            pass
    return divs
