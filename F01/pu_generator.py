import sys
import subprocess
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
    
    for idx, compo in enumerate(my_LHS):
        generate_file(compo, idx) 



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
    print(_LHS)
    return _LHS


def generate_file(compo, n):
    names =[ "_PU_238",
            "_PU_239",
            "_PU_240",
            "_PU_241",
            "_PU_242",
            "_AM_241", ]
    subprocess.call(["cp shared/pu_template.xml shared/pu.xml"],
            shell=True)

    for idx, name in enumerate(names):
        val = compo[idx]
        subprocess.call(["sed -i -e 's/" + name + "/" + str(val) + "/g' "
            "shared/pu.xml"], shell=True)
    subprocess.call(["/Users/mouginot/.local/bin/cyclus main_pueq.xml -o " +
        str(n) + "_pueq.h5 -v2"], shell=True)
    subprocess.call(["/Users/mouginot/.local/bin/cyclus main_fix.xml -o " +
        str(n) + "_fix.h5 -v2"], shell=True)









if __name__ == '__main__':
    build()
