from attenuator import Attenuator
import os


if __name__ == '__main__':
    print('请输入衰减量(db):')
    x = float(input('> '))
    a=10**(-x/10)
    print('请输入ri(ohm):')
    ri = float(input('> '))
    print('请输入ro(ohm):')
    ro = float(input('> '))
    att=Attenuator()
    [tr1, tr2, tr3, pir1, pir2, pir3]=att.calculate(ri,ro,a)
    print('T型：r1,r2,r3:',tr1,tr2,tr3)
    print('PI型：r1,r2,r3:',pir1, pir2, pir3)
    os.system('pause')