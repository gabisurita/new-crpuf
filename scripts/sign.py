#!/usr/bin/python

###############################################################################################
# Submodule: Signature detector
# Author: Rodrigo Surita
# Date: 11/06/2014 
#
# Dependencies:
#	* RAW_response_PUF
#	* Time Base used on simulation (time between challanges)
#	* Define Stability Range (% of time base which response is allowed to be unstable)
#
# Usage:
#		sign.py -i <RAW_response_PUF> -o <Signature_Out> -t <Time_Base> -s <Stability_Range>
#
# TODO:
#	* Detect challange change via Simulation Output 
# * Remove time dependency
#
##############################################################################################

# Parser for Command Line Args
from optparse import OptionParser 

# Base Parameters (!IMPORTANT INFORMATION)
timeBase				 = 50.0
stabilityWeight	 = 0.9

def GetSignature(OutputsLocation, SignatureLocation):
	Outputs			= open(OutputsLocation, "r")
	Signature		= open(SignatureLocation, "w")

	line 						 = "#0"
	transitionTime	 = 0.0
	microEvent			 = ""
	LastMicroEvent	 = ""
	
	LastLine = ""
	
	#RestartLastMicroEvent = False;

	for Line in Outputs:
		#if Line == LastLine:
		#	continue
		
		#LastLine = Line
		
		event = Line.split(" ")

		# Detects new PUF entity
		if event[0].find("#") == 0:
			Signature.write("\n\n")
			entity = event[0].split('#')[1]
			transitionTime = 0.0
			#RestartLastMicroEvent = True;
			Signature.write("#"+str(entity))


		else:
			#try:
				microEventTime = float(event[2])
				microEvent		 = event[0]

				# Restart response when PUF when changing PUF entity
				#if RestartLastMicroEvent == True:
					#LastMicroEvent = microEvent
					#RestartLastMicroEvent = False


				# Detect Challange Change (using time parameters) -- TODO Detect via Simulation Output
				if microEventTime > transitionTime + stabilityWeight*timeBase :
					transitionTime = float(event[2])
					Signature.write("\n")
			
				# Detect Bitwise Change
				for i in range(len(microEvent)):
					if LastMicroEvent != "":
						if microEvent[i] != LastMicroEvent[i]:
							Signature.write(str(i+1))
							#if  microEvent[i] >  LastMicroEvent[i]:
								#Signature.write(str(i+1)+"u")
							#else:
								#Signature.write(str(i+1)+"d")
	
				LastMicroEvent = microEvent			

			#except: #EOF
				#pass
				
	Outputs.close()
	Signature.close()


if __name__ == "__main__":
	OutputsLocation = 'scripts/response_RPUF1_3x5_bits_16_pufs.txt'
	SignatureLocation = 'scripts/Signature.txt'
	
	parser = OptionParser()
	
	parser.add_option("-i", "--input", metavar="FILE", help="RAW PUF output location",  dest="input")
	parser.add_option("-o", "--output", metavar="FILE", help="Signature data output", dest="output")
	parser.add_option("-t", "--timebase", type="float", help="Set time base", dest="time")
	parser.add_option("-s", "--stability", type="float", help="Set stability range", dest="stability")
  
	(options, args) = parser.parse_args()

	if options.input:
		OutputsLocation = options.input;

	if options.output:
		SignatureLocation = options.output;

	if options.time:
		timeBase = options.time;

	if options.stability:
		stabilityWeight = options.stability;


	print "Starting Signature Catch..."
	GetSignature(OutputsLocation, SignatureLocation)
	print "Finished Signature Catch!! \n"

