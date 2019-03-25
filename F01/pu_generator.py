import sys
sys.path.append('/Users/mouginot/work/LHS_build')
import build_lhs



def build():
    
    dim = 5
    sample = 1000
    method = 'maximin'
    outdat = "outdat"
    my_LHS = build_lhs.build_LHS(dim, sample, method, 1, outdat, plot=False,
            verbose=False)

    Pu = [  [ 0., 7.5],
            [10., 30],
            [ 0., 20.],
            [ 0., 20.],
            [ 0., 7.]]
    
    my_LHS = build_lhs.normalyse_LHS(my_LHS, Pu)
   
    my_LHS = add_pu9(my_LHS)
    build_lhs.build_plot(my_LHS, outdat +".png")




def add_pu9(LHS):

    _LHS = []
    for compo in LHS:
       pu38 = compo[0]
       pu40 = compo[1]
       pu41 = compo[2]
       pu42 = compo[3]
       am41 = compo[4]
       pu39 = 100 - pu38 - pu40 - pu41 - pu42 - am41
        
       _compo = [pu38, pu39, pu40, pu41, pu42, am41]
       _LHS.append(_compo)

    return _LHS



if __name__ == '__main__':
    build()
