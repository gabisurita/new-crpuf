import numpy as np
import matplotlib.pyplot as plt
	
def GetCoverage(BigBuffer):
	x = [0] * (len(BigBuffer[0]))

	for Dev1 in range(len(BigBuffer)):
		for Dev2 in range(len(BigBuffer)):
			if Dev1 != Dev2:
				Device = BigBuffer[Dev1]
				Device2 = BigBuffer[Dev2]
				
				i = 1

				try:					
					while Device[i] == Device2[i]:
						i += 1
					else:
						x[i+1] += 1
						break
				except:
					continue
					
	Xsum = 0
	for i in range(len(x)):
		Xsum += x[i]
		x[i] = Xsum		
		
	return x


def BufferSignal(File):
	BigBuffer = []
	Buffer 		= []
	
	for Line in File:
		if Line == "":
			pass

		elif Line == "\n":
			pass
			
		elif Line[0] == "#":
			Buffer = []				
			BigBuffer.append(Buffer)
				
		else:
			Buffer.append(Line.replace("\n",""))
	
	return BigBuffer
		
		
if __name__ == "__main__":

	Response0 = open("/root/Dropbox/IC/puf_simulation/trunk/modules/new-crpuf/data/PUF_Response/Signature_PUF_3x3_bits_10000_pufs.txt", "r")
#	Response1 = open("/root/Dropbox/IC/puf_simulation/trunk/modules/crpuf/data/RPUF1_Response/response_RPUF1_5x5_bits_10000_pufs.txt", "r")
#	Response2 = open("/root/Dropbox/IC/puf_simulation/trunk/modules/crpuf/data/RPUF2_Response/response_RPUF2_5x5_bits_10000_pufs.txt", "r")

	Response1 = open("/root/Dropbox/IC/puf_simulation/trunk/modules/new-crpuf/data/PUF_Response/CRPUF1_response_PUF_3x3_bits_10000_pufs.txt", "r")
	Response2 = open("/root/Dropbox/IC/puf_simulation/trunk/modules/new-crpuf/data/PUF_Response/CRPUF2_response_PUF_3x3_bits_10000_pufs.txt", "r")
	
	Buffer = BufferSignal(Response0)
	x = GetCoverage(Buffer)
	
	print x
	plt.plot(range(len(Buffer[0])), x,label="Signature")

	Buffer = BufferSignal(Response1)
	x = GetCoverage(Buffer)

	print x
	plt.plot(range(len(Buffer[0])), x,label="CRPUF1")

	Buffer = BufferSignal(Response2)
	x = GetCoverage(Buffer)

	print x
	plt.plot(range(len(Buffer[0])), x,label="CRPUF2")

#	plt.ylim(10000)	
	plt.xlim(1, 10)
	
	plt.grid(True)
	plt.legend()
	
	plt.show()
