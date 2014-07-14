#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from puflib import ResponseBuffer
		
		
if __name__ == "__main__":

	Size = "3x3"

	Response0 = open("/root/Dropbox/IC/puf_simulation/trunk/modules/new-crpuf/data/PUF_Response/Signature_PUF_"+ Size +"_bits_1000_pufs.txt", "r")
	Response1 = open("/root/Dropbox/IC/puf_simulation/trunk/modules/new-crpuf/data/PUF_Response/CRPUF1_response_PUF_"+ Size +"_bits_1000_pufs.txt", "r")
	Response2 = open("/root/Dropbox/IC/puf_simulation/trunk/modules/new-crpuf/data/PUF_Response/CRPUF2_response_PUF_"+ Size +"_bits_1000_pufs.txt", "r")
	
	Buffer = ResponseBuffer().BufferSignal(Response2)
	
	HDist = 0.0
	Hw= 0.0
	for i in range(1, 1000):
		for j in range(i, 1000):
	
			HDist += Buffer.HammingDist(3,1,i)
			#Hw += Buffer.HammingWeight(3,i)

	print("Average Hamming Dist")				
	print(HDist/(1000*999/2))	

#	print(Hw/(999))

	x = []
	print("Hamming Weight avg for bit")
	for j in range(1000):
		xx = []
		for i in range(6):
			xx.append(Buffer.HammingWeightAvgBit(j,i))
			#print(Buffer.HammingWeightAvgBit(j,i))
	
		x.append(xx)
	
	x = zip(*x)
	
	for xx in x:
#		print(np.mean(xx))
#		print(np.std(xx))
		pass

#	print(Buffer.HammingWeightAvgBit(1,0))
	
	#print(Buffer.Responses[0])
	
