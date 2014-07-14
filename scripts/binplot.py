import numpy as np
import matplotlib.pyplot as plt


def PrintPuf(Time, WaveVector):

	WaveLine = []
	
	for Wave in WaveVector[1]:
		WaveLine.append([])
	
	j = 0
	for Wave in WaveLine:
		Wave.append(j)

	for Wave in WaveVector:	
		j = 0
		for Char in Wave:
			Char = (0.9 * (float(Char) - 0.5) + j) 
			WaveLine[j].append(Char)
			j += 1



	print len(Time)

	i = 0
	#print Time
	for Wave in WaveLine:	
		plt.step(Time[0:15], Wave[0:15], label="w"+str(i), lw='2')
		i += 1

		
#	plt.axhline(0.5 + i, color='black', lw=3)
	plt.ylim(-0.5, -0.5 + len(WaveLine))	
	#plt.xlim(-1, 60)


	plt.grid(True)
	plt.legend()


#def PrintWaves(Time, WaveVector):

	

if __name__ == "__main__":

	RawDelays = open("/root/Dropbox/IC/puf_simulation/trunk/modules/new-crpuf/data/PUF_Response/RAW_response_PUF_3x3_bits_1000_pufs.txt", "r")

	Line = RawDelays.readline()

	Events	= []
	Moments = []
	

	while Line:
		Line = RawDelays.readline()

		try:
			if Line[0] != "#":

					MicroEvent		 = Line.split(' ')[0].replace("U", "0")
					MicroEventTime = Line.split(' ')[2]
				

					Events.append(MicroEvent)
					Moments.append(MicroEventTime)


			else:
				Entity = Line.split('#')[1]
				#break
				
		except:
			continue
	

	Moments.append(max(Moments))
	PrintPuf( Moments , Events)
	

	plt.show()
	
	
