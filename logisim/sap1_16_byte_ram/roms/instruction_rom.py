# control word signals defintions
HLT = 1 << 23
MI = 1 << 22
RI = 1 << 21
RO = 1 << 20
IO = 1 << 19
II = 1 << 18
AI = 1 << 17
AO = 1 << 16
EO = 1 << 15
SU = 1 << 14
BI = 1 << 13
OI = 1 << 12
CE = 1 << 11
CO = 1 << 10
J = 1 << 9
JC = 1 << 8

file = open("instruction_rom.rom", "w+")
file.write("v2.0 raw\n")
instructions = []

# write fetch microcode to start of all instr
for i in range(0, 16):
	instr = []
	instr.append(CO + MI)
	instr.append(RO + II + CE)
	for j in range(0, 6):
		instr.append(000000)
	instructions.append(instr)
		
# NOP-0x0 ()

# LDA-0x1 (IO|MI, RO|AI)
instructions[1][2] = IO + MI
instructions[1][3] = RO + AI

# ADD-0x2 (IO|MI, RO|BI, EO|AI)
instructions[2][2] = IO + MI
instructions[2][3] = RO + BI
instructions[2][4] = EO + AI

# SUB-0x3 (IO|MI, RO|BI, EO|AI)
instructions[3][2] = IO + MI
instructions[3][3] = RO + BI
instructions[3][4] = EO + AI + SU

# STA-0x4 (IO|MI, AO|RI)
instructions[4][2] = IO + MI
instructions[4][3] = AO + RI

# LDI-0x5 (IO|AI)
instructions[5][2] = IO + AI

# JMP-0x6 (IO|J)
instructions[6][2] = IO + J 

# JC-0x7 (IO|JC)
instructions[7][2] = IO + JC

# OUT-0xE (AO|OI)
instructions[0xe][2] = AO + OI

# HLT-0xF (HLT)
instructions[0xf][2] = HLT

# write instructions to file
for instr in instructions:
	file.write(" ".join(['{:06X}'.format(microcode) for microcode in instr]))
	file.write(" ")
file.close()
	

