
def prime(n: int):
    '''

    :param n: un numar dat
    :return: True daca un numar este prim sau False daca nu este prim

    '''
    nr = 0
    for x in range(2, n//2):
        if n % x == 0:
            nr = nr + 1
    if nr > 0:
        return False
    else:
        return True
def get_goldbach(n: int):
    '''

    :param n: un numar dat
    :return: numerele p1 si p2 astfel incat adunate sa dea numarul n, p1 fiind minim, iar p2 maxim

    '''

    if(n >4):
        for p1 in range(2, n-1):
            for p2 in range(p1+1, n):
                if p1 + p2 == n:
                   if prime(p1) is True and prime(p2) is True:
                    return (p1, p2)
    else:
        return None


def test_get_goldbach():

    assert get_goldbach(5) == (2, 3)
    assert get_goldbach(500) == (13, 487)
    assert get_goldbach(4) == (0, 3)
    assert get_goldbach(4) == None

test_get_goldbach()



def get_newton_sqrt(n: int, steps: int) -> float:
    '''

    :param n: un numar dat
    :param steps: numarul dat de pasi
    :return: aproximarea radicalului unui numar folosind metoda lui Newton

    '''
    x=2
    for i in range(0, steps):
        x = 0.5 * (x + n / x)
    return x


def test_get_newton_sqrt():
    assert get_newton_sqrt(2, 1) == 1.5
    assert get_newton_sqrt(2, 2) == 1.4166
    assert get_newton_sqrt(5, 1) == 2.25
    assert get_newton_sqrt(9, 1) == 3.25

test_get_newton_sqrt()




