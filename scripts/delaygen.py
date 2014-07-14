#!/usr/bin/python

###############################################################################################
# Submodule: Delay & Challenge Generator
# Author: Rodrigo Surita
# Date: 12/06/2014 
#
# Dependencies:
#	* Mean and Variance
#	* PUF size
#	* Number of devices and challanges
# * Python
#
# Usage:
#		sign.py -d <Delay_File> -c <Challenge_file> -i <XORi> -j <XORj> -n <Dev_Num> -v <Challenge_Num>
#
# TODO:
#	* Compare with old simulator
# * Avoid repeated results in a row
# 
#
##############################################################################################

import random

import math

from os import urandom, getpid

# Parser for Command Line Args
from optparse import OptionParser 

# Base Parameters (!IMPORTANT INFORMATION)
Mean			= 1.5
StdDev		= 1.0
#Variance	= 1.0


XORi			 = 7	
XORj			 = 9
Devices		 = 16
Challanges = 8


def RandomNormal(DelayFileName, Mean, Variance):
	random.seed(urandom(int(getpid())))
	DelayFile	= open(DelayFileName, "w")
#	StdDev = math.sqrt(Variance)
	
	for x in range(2*Devices):
		line = ""
		
		for y in range(2 * XORi * (XORj+1)):
			element = str(abs(int(random.normalvariate(Mean, StdDev)*1000000)))

			while len(element) < 7:
				element = "0" + element
					
			line += element + " "		
		
		DelayFile.write(line + "\n")	
		
	DelayFile.close



def RandomChallange(ChallangeFileName):
	random.seed(urandom(int(getpid())))
	ChallangeFile	= open(ChallangeFileName, "w")
	
	for x in range(Challanges):
		line = str(bin(random.getrandbits(2*XORi))).split("b")[1]
		while len(line) < 2*XORi:
			line = "0" + line

		ChallangeFile.write(line + "\n")
	ChallangeFile.close

if __name__ == "__main__":

	DelayFileName 		= "atrasos_RPUF_"+str(XORi)+"x"+str(XORj)+"_"+str(Devices)+"_pufs_.txt"
	ChallangeFileName = "desafios_"+str(Challanges)+"_C_"+str(2*XORi)+"_bits.txt"
	
	parser = OptionParser()
	
	parser.add_option("-d", "--delay_file", metavar="FILE", help="Delay File Output Name",  dest="delay")
	parser.add_option("-c", "--challange_file", metavar="FILE", help="Challange File Output Name", dest="challange")
	parser.add_option("-i", "--width", type="int", help="XOR grid width", dest="matxori")
	parser.add_option("-j", "--lengh", type="int", help="XOR grid lengh", dest="matxorj")
	parser.add_option("-n", "--devices", type="int", help="Number of PUFs", dest="devnum")
	parser.add_option("-v", "--challanges", type="int", help="XOR grid lengh", dest="chalnum")

	(options, args) = parser.parse_args()

	if options.delay:
		DelayFileName = options.delay;
	if options.challange:
		ChallangeFileName = options.challange;
	if options.matxori:
		XORi = options.matxori; 
	if options.matxorj:
		XORj = options.matxorj;
	if options.devnum:
		Devices = options.devnum;		
	if options.chalnum:
		Challanges = options.chalnum;

	print "Creating Delay File..."
	RandomNormal(DelayFileName, Mean, StdDev);
	print "Done!"
	print "Creating Challanges..."
	RandomChallange(ChallangeFileName);
	print "Done!"

	


