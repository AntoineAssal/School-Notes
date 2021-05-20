def problem(m, i): return 0 < m < i


def no_problem(m, i): return not problem(m, i) and not problem(3-m, 3-i)


def next_states(state):
    m, i, b = state
    if b == 1:
        return{(m-mb, i-ib, 0) for mb in range(m+1)
               for ib in range(i+1)
               if 1 <= mb + ib <= 2 and
               no_problem(m-mb, i-ib)
               }
    else:
        return{(m+mb, i+ib, 1) for mb in range(3-m+1)
               for ib in range(3-i+1)
               if 1 <= mb + ib <= 2 and
               no_problem(m+mb, i+ib)
               }


start = (3, 3, 1)
goal = (0, 0, 0)
