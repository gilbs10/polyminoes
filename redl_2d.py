from copy import copy,deepcopy  
from poly_draw import draw_poly_list
from utils import *

if __name__ == "__main__":

    n = 5
    tried = set([])
    untried = set([(0,0)])
    poly = []

    global cnt
    cnts = [0]*n
    polys = [[] for _ in range(n)]

    def redl(poly,untried):
        while untried:
            c = untried.pop()
            tried.add(c)
            poly+=[c]
            polys[len(poly)-1].append(copy(poly))
            # print(poly)
            cnts[len(poly)-1]+=1
            if len(poly) < n:
                ns = get_legal_neighbors(c,tried,untried)
                for neigh   in ns:
                    untried.add(neigh)
                redl(poly,copy(untried))
                for neigh in ns:
                    if neigh in tried:
                        tried.remove(neigh)
                    if neigh in untried:
                        untried.remove(neigh)
            poly.pop()



    redl(poly,untried)
    print(cnts)

    for i in range(n):
        min_p = 3*n
        min_polys = []
        perc = 0
        l = len(polys[i])
        for j,p in enumerate(polys[i]):
            if 100*j/l > perc:
                print('\r',end="")
                print(perc,end="")
                perc+=1
            cur_p = poly_perimeter(p)
            if cur_p < min_p:
                min_p    = cur_p
                min_polys = []
            if cur_p == min_p:
                min_polys.append(p)
        print('\r',i+1,min_p,len(min_polys))
        draw_poly_list(min_polys,"min_poly_"+str(i+1))
        # for p in min_polys:
        #   print(p)

