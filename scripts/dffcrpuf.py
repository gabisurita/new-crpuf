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
	outputs			= open(OutputsLocation, "r")
	Response		= open(ResponseLocation, "w")

	line 						 = "#0"
	transitionTime	 = 0.0
	MicroEvent			 = ""
	LastMicroEvent	 = ""
	
	RestartLastMicroEvent = False;
	
	CRPUF1ResponseEvent = ""
	CRPUF2ResponseEvent = ""
	


	while (line):
		line = outputs.readline()
	
		Event = line.split(" ")

		# Detects new PUF entity
		if Event[0].find("#") == 0:
			Response.write("\n\n")
			entity = Event[0].split('#')[1]
			transitionTime = 0.0
			RestartLastMicroEvent = True;
			Response.write("#"+str(entity))


		else:
#			try:
				MicroEventTime = float(Event[2])
				MicroEvent		 = Event[0]

				# Restart response when PUF when changing PUF entity
				if RestartLastMicroEvent == True:
					LastMicroEvent = "0" * len(MicroEvent)
					RestartLastMicroEvent = False;
					
					CRPUF1ResponseEvent = "0" * ((len(MicroEvent) * (len(MicroEvent) - 1)) / 2)
					CRPUF2ResponseEvent = "0" *  (len(MicroEvent) * (len(MicroEvent) - 1))					

				# Detect Challange Change (using time parameters) -- TODO Detect via Simulation Output
				if MicroEventTime > transitionTime + stabilityWeight*timeBase :
					transitionTime = float(Event[2])
					Response.write(CRPUF2ResponseEvent)
					Response.write("\n")

			
				# Detect Bitwise Change
				for i in range(len(MicroEvent)):
					#if LastMicroEvent != "":
					
						# CRPUF2
						for j in range(len(MicroEvent)):
							if MicroEvent[i] == '1':
								EventSegment = CRPUF2ResponseEvent[(i-1)*len(MicroEvent):i*len(MicroEvent)]
								EventSegment = MicroEvent[i-1:] + MicroEvent[:i]
								j1 = j -1
								j2 = j +1 
								CRPUF2ResponseEvent = CRPUF2ResponseEvent[:(i-1)*len(MicroEvent)] + EventSegment + CRPUF2ResponseEvent[(i+1)*len(MicroEvent):]


	
				LastMicroEvent = MicroEvent			

	#		except: #EOF
	#			outputs.close()
#				Response.close()
	#			break;


if __name__ == "__main__":
	OutputsLocation = 'scripts/response_RPUF1_5x5_bits_16_pufs.txt'
	ResponseLocation = 'Response.txt'
	
	parser = OptionParser()
	
	parser.add_option("-i", "--input", metavar="FILE", help="RAW PUF output location",  dest="input")
	parser.add_option("-o", "--output", metavar="FILE", help="Response data output", dest="output")
	parser.add_option("-t", "--timebase", type="float", help="Set time base", dest="time")
	parser.add_option("-s", "--stability", type="float", help="Set stability range", dest="stability")
  
	(options, args) = parser.parse_args()

	if options.input:
		OutputsLocation = options.input;

	if options.output:
		ResponseLocation = options.output;

	if options.time:
		timeBase = options.time;

	if options.stability:
		stabilityWeight = options.stability;


	print "Starting Signature Catch..."
	GetSignature(OutputsLocation, ResponseLocation)
	print "Finished Signature Catch!! \n"

