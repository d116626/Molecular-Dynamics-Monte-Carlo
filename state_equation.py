import random, math, pylab,matplotlib.pyplot as plt

def initial_conditions(N):
    Dx=1./8. #distannce between two atoms on the x axis
    Dy=math.sqrt(3.)*Dx/2. #distannce between two atoms on the y axis
    positions=[[(k1+(k2%2)/2.)*Dx,k2*Dy] for k1 in range(N) for k2 in range(N)]
    Lx=N*Dx#Box size x axis
    Ly=N*Dy #Box size y axis
    return positions,Lx,Ly

def gama_cut(N,xcut):
    x1=1-N*1.0/(xcut*1.0)
    if(x1<0):
       return 
    else:
        z=True
        while z == True:
            delta_x = - math.log(random.uniform(0,1))/x1
            x = xcut + delta_x
            gama1 = ((x/xcut)**N) * math.exp(-(1-x1)*delta_x)
            if(random.uniform(0,1)>gama1): z = True
            else:
                z = False
        return xcut+delta_x

def sigma_cut(x,betaP):
    dists=[]
    for j in range (N*N):
        a=x[j]
        s_c=min(math.sqrt((x[j][0]-b[0])**2+(x[j][1]-b[1])**2) for b in x if b!=a)
        dists.append(s_c) 
    sc=min(dists)   
    return betaP*Vi*(sigma/(sc/2))**2

N=10 # number of disks is N*N
x,Lx,Ly = initial_conditions(N)
sigma = 0.5
Vi = Lx*Ly
betaP=4.0
nruns=10**3

grafx_betaP=[]
grafy_Vn=[]

while betaP<20:
    sumvn=0
    for h in range(nruns):
        xc=sigma_cut(x,betaP)     # xcut
        Vn = gama_cut(N*N,xc)/betaP
        sumvn=sumvn+Vn
    grafx_betaP.append(betaP)
    grafy_Vn.append(sumvn/(nruns*N*N))
        
    print betaP
    
    betaP+=1

pylab.plot(grafx_betaP,grafy_Vn, '-')
pylab.xlabel(r'$ \beta $ P')
pylab.ylabel('Volume')
pylab.title('Equation of state for %d disks ' %(N*N) ,fontsize = 14)
pylab.savefig('equation_state.jpeg')
pylab.grid(True)
pylab.show()














