
def is_legal_and_untried(c,tried,untried):
    if c in tried or c in untried:
        return False
    else:
        return c[1] > 0 or (c[1] == 0 and c[0] >=0)

def get_legal_neighbors(c,tried = {},untried = {}):
    x = c[0]
    y = c[1]
    ns = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    ns = [x for x in ns if is_legal_and_untried(x,tried,untried)]
    return ns

def get_all_neighbors(c):
    x = c[0]
    y = c[1]
    return [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]


def poly_perimeter(p):
    poly = set(p)
    perimeter = set()
    for c in p:
        for n in get_all_neighbors(c):
            if not n in poly:
                perimeter.add(n)
    return len(perimeter)
