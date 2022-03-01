from q1 import safe_call, fun
from q2 import print_sorted
from q3 import find_root

if __name__ == '__main__':

    try:
        print(safe_call(fun, 1, 0.7, 3))
    except Exception as err:
        print(f"expected {err=}, {type(err)=}")

    print_sorted({"a":5, "c":6 , "b":[1,2,3,4]})

    f = lambda x: x ** 2 - 4
    try:
        print(find_root(f, 1, 3))
    except Exception as e:
        print(e)

