class Exception1(Exception):
    pass


class Exception2(Exception):
    pass


def raise_exception1():
    raise Exception1


def raise_exception2():
    raise Exception2


if __name__ == '__main__':
    try:
        raise_exception1()
        raise_exception2()
    except Exception1:
        print("Exception1")
    except Exception2:
        print("Exception2")
    else:
        print("else")
    finally:
        print("finally")
