#import numpy as np


class Attenuator(object):
    #衰减器电阻值计算
    def calculate(self,ri,ro,a):
        #tr3 = 2*np.sqrt(a*ri*ro)/(1-a)
        tr3 = 2 * (a * ri * ro)**0.5 / (1 - a)
        tr1 = (1+a)/(1-a)*ri-tr3
        tr2 = (1+a)/(1-a)*ro-tr3
        #pir3=1/(2/(1-a)*np.sqrt(a/(ri*ro)))
        pir3 = 1 / (2 / (1 - a) * (a / (ri * ro))**0.5)
        pir1=1/(1/ri*(1+a)/(1-a)-1/pir3)
        pir2=1/(1/ro*(1+a)/(1-a)-1/pir3)
        return [tr1,tr2,tr3,pir1,pir2,pir3]

