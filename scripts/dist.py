#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from puflib import ResponseBuffer
		
if __name__ == "__main__":

	Size = "3x3"

	Response0 = open("/root/Dropbox/IC/puf_simulation/trunk/modules/new-crpuf/data/PUF_Response/Signature_PUF_"+ Size +"_bits_100_pufs.txt", "r")
	Response1 = open("/root/Dropbox/IC/puf_simulation/trunk/modules/new-crpuf/data/PUF_Response/CRPUF1_response_PUF_"+ Size +"_bits_100_pufs.txt", "r")
	Response2 = open("/root/Dropbox/IC/puf_simulation/trunk/modules/new-crpuf/data/PUF_Response/CRPUF2_response_PUF_"+ Size +"_bits_100_pufs.txt", "r")
	
	Buffer = ResponseBuffer().BufferSignal(Response0)

	plt.figure(figsize=(16*1.5,9*1.5))
	
	for i in range(0,8):
		plt.subplot(2, 4, i+1)	
		x = Buffer.ResponseDist(i+1)
		x[1].sort()
		
		#plt.ylim(0,4)
		print len(x[1])
		print sum(x[1])
			
		plt.bar(range(len(x[1])), x[1], label="Desafio " + str(i+1))	
		plt.grid(True)
		plt.legend()

	plt.savefig('Occr_'+ Size +'_Sig.png')
	
	#plt.show()
	
	
	Buffer = ResponseBuffer().BufferSignal(Response1)
	
	
	plt.figure(figsize=(16*1.5,9*1.5))
	
	for i in range(0,8):
		plt.subplot(2, 4, i+1)	
		x = Buffer.ResponseDist(i+1)

		x[1].sort()
		print len(x[1])
		print sum(x[1])
	
		plt.bar(range(len(x[1])), x[1], label="Desafio " + str(i+1))	
		plt.grid(True)
		plt.legend()

	plt.savefig('Occr_'+ Size +'_PUF1.png')
	
	#plt.show()
		
		
	
	Buffer = ResponseBuffer().BufferSignal(Response2)
	
	
	plt.figure(figsize=(16*1.5,9*1.5))
	
	for i in range(0,8):
		plt.subplot(2, 4, i+1)
		x = Buffer.ResponseDist(i+1)

		x[1].sort()
		print len(x[1])
		print sum(x[1])
	
		y=[]
		yacc = 0

	
		plt.bar(range(len(x[1])), x[1], label="Desafio " + str(i+1))	
		plt.grid(True)
		plt.legend()

	plt.savefig('Occr_'+ Size +'_PUF2.png')
	
	#plt.show()
		
		
		
		
