import random, pylab, math, matplotlib.pyplot as plt
import time
start = time.time()

def direct_disks_box(N, sigma, Lx,Ly):
    z = True
    while z == True:
        L = [(random.uniform(sigma, Lx - sigma), random.uniform(sigma, Ly - sigma))]
        
        for k in range(1, N):
            a = (random.uniform(sigma, Ly - sigma), random.uniform(sigma, Lx- sigma))
            min_dist = min(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) for b in L) 
            if min_dist < 4.0 * (sigma**2) : 
                z = True
                break
            else:
                z = False
                L.append(a)
    
    return L
#------------------------------Initial Conditions -----------------------------#
N = 8   #Number of disks
eta=0.18 #density
sigma = math.sqrt((eta)/(N*math.pi))
positions_i=[]
positions_f=[]
Lx=1.0
Ly=1.0
nruns = 10**5 #routine

#------------------------------------------------------------------------------#

#if u want to see histogram of y delete "#" in lines 27,32,35, 44 to 49

histox = []
histoy = []
for i in range(nruns):
    
    abc = direct_disks_box(N, sigma,Lx,Ly)
    if i==0:positions=abc
    for k in range(N): 
        histox.append(abc[k][0])
        histoy.append(abc[k][1])
positions_f=abc

spendtime = time.time() - start
print spendtime, "seconds."

#---------------------------Snapshot Initial Positions --------------------------#
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
pylab.title('Snapshot Initial Positions',fontsize = 14)

#--------------------------------------------------------------------------------#

#----------------------------Snapshot Final Positions ---------------------------#
plt.subplot(222)
v=[-Lx,0,Lx]
u=[-Ly,0,Ly]
for [x,y] in positions_f:
    for delx in v:
            for dely in u:
                cir=pylab.Circle((x +delx  , y +dely ), radius = sigma)
                pylab.gca().add_patch(cir)
pylab.axis([0,Lx,0,Ly])
pylab.xlabel('x-position')
pylab.ylabel('y-position')
pylab.title('Snapshot Final Positions',fontsize = 14)

#--------------------------------------------------------------------------------#

       
#---------------------------Histogram of x positions --------------------------#
plt.subplot(223)
pylab.hist(histox, normed=True , bins=100 , histtype='step')
pylab.xlabel('x-position')
pylab.ylabel('Probability Density')
pylab.title('Histogram of x-positions with $\eta$ = %.2f' %eta,fontsize = 14)
pylab.savefig('direct_disks_histo.jpeg')
#------------------------------------------------------------------------------#

#---------------------------Histogram of y positions --------------------------#
plt.subplot(224)
pylab.hist(histoy, normed=True , bins=100 ,color='b', histtype='step')
pylab.xlabel('y-position')
pylab.ylabel('Probability Density')
pylab.title('Histogram of y-positions with $\eta$ = %.2f' %eta,fontsize = 14)
pylab.savefig('direct_disks_histo.jpeg')
#------------------------------------------------------------------------------#
plt.get_current_fig_manager().resize(878, 760)
plt.tight_layout()
pylab.show()