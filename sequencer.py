import FEB
import time

#init - set up heater, thermomoter, FEB etc
#look at /data/DAQ
#sweep parameters, in units of uA (?)
qetBiasStart = 100 #garbage placeholder numbers that don't mean anything
qetBiasFinal = 0
qetBiasStep = -10

#FEB rack parameters
subrack=1
slot=3
channel=FEB.CHANNEL.D




#loop - sweep accross range of QET bias currents
for bias in range (qetBiasStart, qetBiasFianl+qetBiasStep, qetBiasStep):
	
	
	print("Bias Step: ",bias," uA")
	FEB.setSensorSquid(subrack,slot,FEB.SETTINGS.SENSORBIAS,bias)
	
	#check bias
	actualBias=FEB.getSensorSquid(subrack,slot,FEB.SETTINGS.SENSORBIAS)
	print("Actualt Bias: ",actual bias," uA")
	
	#get data from daq - need to check connor's implementation

