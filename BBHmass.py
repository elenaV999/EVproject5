import numpy as np
import matplotlib.pyplot as plt

#read mergers.out, cob.out --> return: total BBH mass and separation for merged and non merged binaries
def bbh(met)	:
	 
	fname='A1.0/'+str(met)+'/mergers.out' #merged binaries
	ID, sepform, eccform, k1form, m1form, k2form, m2form = np.genfromtxt(fname, dtype="float", comments="#", usecols=(0,4,5,6,7,8,9), unpack=True)
	
	fname_='A1.0/'+str(met)+'/COB.out'  #all CO binaries
	ID_, sepform_, eccform_, k1form_, m1form_, k2form_, m2form_ = np.genfromtxt(fname_, dtype="float", comments="#", usecols=(0,4,5,6,7,8,9), unpack=True) 

	Nmerg=len(ID) 
	Ncob=len(ID_) 
	print('\n\nZ= ', met)
	print('Ncob = ', Ncob, '	Nmerg = ', Nmerg, '	Nnon_merg = ', Ncob-Nmerg)
		
	mtot_merg=m1form + m2form   #total mass of the CO binary
	mtot_cob=	m1form_ + m2form_
		
				
	#find BBHs and count other types of binaries: 
	bhns, ns, bhns_, ns_ = 0, 0, 0, 0 
	mtot_mergBH, mtot_cobBH =[],[] 
	sepBH, sepBH_ =[],[]
	for i in range(Nmerg): 
		if 	k1form[i]==14 and k2form[i]==14 :  
			mtot_mergBH.append(mtot_merg[i])
			sepBH.append(sepform[i])
		elif k1form[i]==13 and k2form[i]==13 : ns+=1
		elif (k1form[i]==14 and k2form[i]==13) or (k1form[i]==13 and k2form[i]==14) :  bhns+=1

	for i in range(Ncob): 
		if 	k1form_[i]==14 and k2form_[i]==14 :  
			mtot_cobBH.append(mtot_cob[i])
			sepBH_.append(sepform_[i])
		elif k1form_[i]==13 and k2form_[i]==13 : ns_ +=1
		elif (k1form_[i]==14 and k2form_[i]==13) or (k1form_[i]==13 and k2form_[i]==14) :  bhns_+=1

	print('all:	bh = ',len(mtot_cobBH), '	ns = ', ns_, '	bhns = ', bhns_ )
	print('merged:		bh = ',len(mtot_mergBH), '	ns = ', ns,  '	bhns = ', bhns  )

	
	print('mergers fracion:  bh: ', len(mtot_mergBH)/len(mtot_cobBH),'	ns = ',ns/ns_,  '	bhns = ', bhns/bhns_ )
	print('BBHs fraction: ' ,len(mtot_cobBH)/2e6, '	CO binaries fraction(%)', len(ID_)/2e6)
	print('maximum mass: all = ', np.max(mtot_cobBH), '	merged = ', np.max(mtot_mergBH))

	return mtot_mergBH, mtot_cobBH, sepBH, sepBH_



mtot1_merg, mtot1_all, sepBH1, sepBH1_= bbh(0.0002)
mtot2_merg, mtot2_all, sepBH2, sepBH2_= bbh(0.004)
mtot3_merg, mtot3_all, sepBH3, sepBH3_= bbh(0.02)

figsize=(7,8)
############## total BBH mass plot #######################################
fig, ax =plt.subplots(2,1, figsize=figsize, sharex=True) 
fig.subplots_adjust(hspace=0)

Nbin=50
h1, b, _ = ax[0].hist ( mtot1_merg, bins=Nbin, density=False, color='blue',  histtype='step', linewidth=1.8, range=(0,150))
h2, b, _ = ax[0].hist ( mtot2_merg, bins=Nbin, density=False, color='green',  histtype='step', linewidth=1.8, range=(0,150))
h3, b, _ = ax[0].hist ( mtot3_merg, bins=Nbin, density=False, color='orangered',  histtype='step', linewidth=1.8, range=(0,150)) 

h1_, b, _ = ax[1].hist ( mtot1_all, bins=Nbin, density=False, color='blue',  histtype='step', linewidth=1.8, ls='--', range=(0,150)) 
h2_, b, _ = ax[1].hist ( mtot2_all, bins=Nbin, density=False, color='green',  histtype='step', linewidth=1.8, ls='--', range=(0,150))
h3_, b, _ = ax[1].hist ( mtot3_all, bins=Nbin, density=False, color='orangered',  histtype='step', linewidth=1.8, ls='--', range=(0,150)) 

ax[1].set_xlabel('M$_{tot}$ [M$_\odot$]',  fontsize= 13 ) 
ax[0].set_ylabel('number',  fontsize= 13) 
ax[0].set_yscale('log')
ax[1].set_ylabel('number',  fontsize= 13) 
ax[1].set_yscale('log')
ax[0].text(110, 1e2,'merged BBHs', fontsize= 15, color='gray', fontweight='roman', alpha=0.8, stretch='semi-condensed')
ax[1].text(120,2e3, 'all BBHs', fontsize= 15, color='gray', fontweight='roman', alpha=0.8, stretch='semi-condensed')
ax[0].legend(['Z=0.0002','Z=0.004', 'Z=0.02'])

ax[0].xaxis.set_tick_params(direction='inout', length=9)
ax[1].xaxis.set_tick_params(direction='inout', length=6)

ax[0].set_title('Total mass of the binary', fontsize= 14, fontweight='semibold' )
plt.show()





##### PLOT BBHs separation ########
fig, ax =plt.subplots(2,1, figsize=figsize, sharex=True) 
fig.subplots_adjust(hspace=0)

Nbin=50
bins=np.logspace(np.log10(0.8),np.log10(1e8),Nbin)
bins_=np.logspace(np.log10(0.8),np.log10(1e8),Nbin)
h1, b2, _ = ax[0].hist ( sepBH1, bins=bins, density=False, color='blue',  histtype='step', linewidth=2)
h2, b2, _ = ax[0].hist ( sepBH2, bins=bins, density=False, color='green',  histtype='step', linewidth=2)
h3, b2, _ = ax[0].hist ( sepBH3, bins=bins, density=False, color='orangered',  histtype='step', linewidth=2 ) 

h1_, b2_, _ = ax[1].hist ( sepBH1_, bins=bins_, density=False, color='blue',  histtype='step', ls='--', linewidth=2) 
h2_, b2_, _ = ax[1].hist ( sepBH2_, bins=bins_, density=False, color='green',  histtype='step', ls='--', linewidth=2)
h3_, b2_, _ = ax[1].hist ( sepBH3_, bins=bins_, density=False, color='orangered',  histtype='step', ls='--', linewidth=2 ) 

ax[1].set_xlabel('a [ R$_\odot$]',  fontsize= 13 ) 
ax[0].set_ylabel('number',  fontsize= 13) 
ax[0].set_yscale('log')
ax[0].set_xscale('log')
ax[1].set_ylabel('number',  fontsize= 13) 
ax[1].set_yscale('log')
ax[1].set_xscale('log')

ax[0].text(5e5, 1e2,'merged BBHs', fontsize= 15, color='gray', fontweight='roman', alpha=0.8, stretch='semi-condensed')
ax[1].text(2e6,2e3, 'all BBHs', fontsize= 15, color='gray', fontweight='roman', alpha=0.8, stretch='semi-condensed')
ax[0].legend(['Z=0.0002','Z=0.004', 'Z=0.02'], loc='upper right')

ax[0].xaxis.set_tick_params(direction='inout', length=9)
ax[1].xaxis.set_tick_params(direction='inout', length=6)
ax[0].set_title('Initial separation', fontsize= 14, fontweight='semibold' )
plt.show()



#####PLOT merger fraction per mass bin
Nbin=50
h1, b = np.histogram ( mtot1_merg, bins=Nbin, density=False, range=(0,150))
h2, b = np.histogram ( mtot2_merg, bins=Nbin, density=False, range=(0,150))
h3, b = np.histogram ( mtot3_merg, bins=Nbin, density=False, range=(0,150)) 

h1_, b = np.histogram ( mtot1_all, bins=Nbin, density=False, range=(0,150)) 
h2_, b = np.histogram ( mtot2_all, bins=Nbin, density=False, range=(0,150))
h3_, b = np.histogram ( mtot3_all, bins=Nbin, density=False, range=(0,150)) 

deltam=(b[1]-b[0])/2
m_bins = b+deltam #bin center
m_bins = m_bins[:-1] #remove last element

rate1=np.zeros(len(m_bins))
rate2=np.zeros(len(m_bins))
rate3=np.zeros(len(m_bins))
for i in range(len(m_bins)):
	if h1_[i]!=0 : rate1[i]=h1[i]/h1_[i] #avoind divsion by zero
	if h2_[i]!=0 : rate2[i]=h2[i]/h2_[i]
	if h3_[i]!=0 : rate3[i]=h3[i]/h3_[i]
	
plt.plot(m_bins,rate1, color='blue')
plt.plot(m_bins,rate2,  color='green')
plt.plot(m_bins,rate3,  color='orangered')
plt.xlabel('M$_{tot}$ [M$_\odot$]',  fontsize= 13 )
plt.title('fraction of BBHs mergers',  fontsize= 14 , fontweight='semibold')
plt.legend(['Z=0.0002','Z=0.004', 'Z=0.02'])
plt.show()



