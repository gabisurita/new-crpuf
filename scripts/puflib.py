#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

class ResponseBuffer:
	def __init__(self):
		self.Responses = []
		self.EntityCount = 0
		self.ChallengeCount = 0
	
	
	
	# Func: BufferSignal(File)
	# Description: Extract responses from file (signature or PUF Response) returning two level list ordered by [Entity][Challange].
	def BufferSignal(self, File):
		BigBuffer = []
		Buffer 		= []

		for Line in File:
			if Line == "":
				pass

	#		elif Line == "\n":
	#			pass
		
			elif Line[0] == "#":
				Buffer = []			
				BigBuffer.append(Buffer)
			
			else:
				Buffer.append((Line.replace("\n","")).replace("U","0"))
			
		self.Responses = BigBuffer
		self.EntityCount = len(BigBuffer)
		self.ChallengeCount = len(BigBuffer[0])
		return self
	
	
	
	# Func: ResponseDist(Challange)
	# Description: Extract responses from file (signature or PUF Response) returning [Response, ocorrences] list.
	def ResponseDist(self, Challenge):
		
		Responses		  = []
		ResponseCount = []
	
		#for Challenge in range(Challenges):
		for Dev in range(self.EntityCount):
			try:
				try:			
					Ocorrence = Responses.index(self.Responses[Dev][Challenge])
				
				except ValueError:
					Ocorrence = -1
		
				if Ocorrence < 0:
					Responses.append(self.Responses[Dev][Challenge])
					ResponseCount.append(1)
				else:
					ResponseCount[Ocorrence] += 1
		
			except IndexError:
				break
			
		ReturnMat = [Responses, ResponseCount]
	
		return ReturnMat
	
	
		
	# Func: HammingDist(Challange, Dev1, Dev2)
	# Description: Calculates Hamming Distance between two challange responses
	def HammingDist(self, Challenge, Dev1, Dev2):
	
		return sum(ch1 != ch2 for ch1, ch2 in zip(self.Responses[Dev1][Challenge], self.Responses[Dev2][Challenge]))
	
	
	
	# Func: HammingWeight(Challange)
	# Description: Calculates Hamming Weight for a Challange Response
	def HammingWeight(self, Challenge, Dev):
		return self.Responses[Dev][Challenge].count("1")

	
		
	# Func: HammingWeightAvgBit(Challange)
	# Description: Calculates average Hamming Weight for a device response bit
	def HammingWeightAvgBit(self, Dev, Bit):
		HWAvg = 0.0
		for Challenge in range(self.ChallengeCount):
			HWAvg += int(self.Responses[Dev][Challenge][Bit])
		
		return HWAvg/self.ChallengeCount



