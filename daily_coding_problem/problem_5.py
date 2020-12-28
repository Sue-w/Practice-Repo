"""
This problem was asked by Facebook.

Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked, f itself will not be called for N milliseconds.

1. log time t1 when f is invoked first time and start timer.
2. if function is invoked at t2 and t2 - t1 <= N milliseconds, add a delay of N-t2 milliseconds
then execute function
3. else execute function
"""
import time
import copy


def call_limit(N):
    N = N/1000
    return N


# Argument is in milliseconds
N = call_limit(10000)
# time of previous function call. This will lager change.
t0 = 0


def debounced(function):

    def wrapper():
        import time
        global t0, t1
        # time of the current function call
        t1 = time.time()
        # time between current function call and last function call
        difference = t1 - t0
        if difference < N:
            # time.sleep(N-difference)
            print('Oops! Invoked too soon. Have patience human. Use old result')
            t0 = copy.copy(t1)
            return None
        else:
            t0 = copy.copy(t1)
            return function()
    return wrapper


@debounced
def test_func():
    print('The function "f" has run \n ')


test_func()
test_func()
test_func()
test_func()
test_func()
test_func()
time.sleep(N)
test_func()