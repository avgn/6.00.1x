def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
    return False


def binarySearch(L, e):
    """Assumes L is list, the elements of which are in
       ascending order.
       Returns True if e is in L and False otherwise"""

    def bSearch(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: # nothing left to search
                return False
            else:
                return bSearch(L, e, low, mid - 1)
        else:
            return bSearch(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)