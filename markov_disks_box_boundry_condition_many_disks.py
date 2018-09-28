# -*- coding: utf-8 -*-
import math,random,pylab,matplotlib.pyplot as plt
import time
start = time.time()

def initial_conditions(N,eta):
    Dx=1./8. #distannce between two atoms on the x axis
    Dy=math.sqrt(3.)*Dx/2. #distannce between two atoms on the y axis
    positions=[[(k1+(k2%2)/2.)*Dx,k2*Dy] for k1 in range(N) for k2 in range(N)]
    Lx=N*Dx #Box size x axis
    Ly=N*Dy #Box size y axis
    sigma = math.sqrt((Lx*Ly*eta)/(N*N*math.pi))# radius of atoms
    return positions,Lx,Ly,sigma,positions

def dist(x,y,Lx,Ly):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, Lx - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, Ly - d_y)
    return  d_x ** 2 + d_y ** 2

def markov_disck(L,sigma,Lx,Ly, delta,nsteps):
    histox=[]
    histoy=[]
    for i in range(nsteps):
        a = random.choice(L)
        L.remove(a)
        b = ((a[0] + random.uniform(-delta, delta)) % Lx , (a[1] + random.uniform(-delta,delta)) % Ly)
        #%Lx e %Ly  give us the periodic boundary conditions
        min_dist = min(dist(b, x,Lx,Ly) for x in L)
        if  min_dist < 4.0 * sigma ** 2:
            L.append(a)
        else:
            L.append(b)
            histox.append(b[0])
            histoy.append(b[1])
    return L, histox,histoy

#------------------------------Initial Conditions -----------------------------#
N=3    #the number of atoms in the box is N*N
eta=0.69 #density
L,Lx,Ly,sigma, positions= initial_conditions(N,eta)# L is the positions of atoms
nsteps = 10**6 #routine
delta = 0.1
#------------------------------------------------------------------------------#

#--------------------------Snapshot Initial Positions -------------------------#
plt.subplot(221)
v=[-Lx,0,Lx]
u=[-Ly,0,Ly]
for [x,y] in positions:
    for delx in v:
            for dely in u:
                cir=pylab.Circle((x +delx  , y +dely ), radius = sigma)
                pylab.gca().add_patch(cir)
pylab.axis([0,Lx,0,Ly])
pylab.xlabel('x-position')
pylab.ylabel('y-position')
pylab.title('Snapshot Initial Positions with N = %d'%(N*N),fontsize = 14)

#------------------------------------------------------------------------------#

L, histox,histoy = markov_disck(L,sigma,Lx,Ly, delta,nsteps)

#---------------------------Snapshot Final Positions --------------------------#
plt.subplot(222)
for [x,y] in L:
    for delx in v:
            for dely in u:
                cir=pylab.Circle((x +delx  , y +dely ), radius = sigma)
                pylab.gca().add_patch(cir)
pylab.axis([0,Lx,0,Ly])
pylab.xlabel('x-position')
pylab.ylabel('y-position')
pylab.title('Snapshot Final Positions with N = %d'%(N*N),fontsize = 14)

#------------------------------------------------------------------------------#

#---------------------------Histogram of x positions --------------------------#
if histox != []:
    plt.subplot(223)
    pylab.hist(histox, normed=True , bins=100, fc='g')
    pylab.xlabel('x-position',fontsize = 12)
    pylab.ylabel('Probability Density')
    pylab.title('Histogram of x-positions with $\eta$ = %.2f' %eta,fontsize = 14)
    
    
else: print 'There was no movement in the x-axis'
#------------------------------------------------------------------------------#

#---------------------------Histogram of y positions --------------------------#
if histoy != []:
    plt.subplot(224)
    pylab.hist(histoy, normed=True , bins=100)
    pylab.xlabel('y-position')
    pylab.ylabel('Probability Density')
    pylab.title('Histogram of y-positions with $\eta$ = %.2f' %eta,fontsize = 14)
    pylab.savefig('markov_disks_box_boundry_condition_many_disks.jpeg')
else: print 'There was no movement in the y-axis'
#------------------------------------------------------------------------------#
#plt.subplots_adjust(left=0.08, right=0.95, wspace=0.50, hspace=0.40)
plt.get_current_fig_manager().resize(878, 760)
plt.tight_layout()
pylab.show()

print time.time() - start, "seconds."