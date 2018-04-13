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
TR = 1 << 8
FI = 1 << 7
INV = 1 << 6
JLZ = 1 << 5
JZ = 1 << 4
JC = 1 << 3
L2 = 1 << 2
L1 = 1 << 1
L0 = 1

file = open("instruction_rom.rom", "w")
file.write("v2.0 raw\n")
instructions = []

# write fetch microcode to start of all instr
for i in range(0, 256):
	instr = []
	instr.append(CO + MI)
	instr.append(RO + II + CE)
	for j in range(0, 6):
		instr.append(000000)
	instructions.append(instr)
		
		
# memory operations
#################################################
		
# NOP-0x00 ()

# LDA-0x01 (IO|MI, RO|AI)
instructions[1][2] = MI + CO
instructions[1][3] = MI + RO
instructions[1][4] = RO + AI + CE
instructions[1][5] = TR

# LDI-0x10->1f
for i in range(0, 16):
	instructions[0x10+i][2] = IO + AI
	instructions[0x10+i][3] = TR

# LDN-0x02
instructions[0x2][2] = MI + CO
instructions[0x2][3] = RO + AI + CE
instructions[0x2][4] = TR

# STA-0x03
instructions[0x3][2] = MI + CO
instructions[0x3][3] = MI + RO
instructions[0x3][5] = RO + AI + CE
instructions[0x3][6] = TR

# arithmetic operators
#################################################

# ADD-0x20 (IO|MI, RO|BI, EO|AI)
instructions[0x20][2] = MI + CO
instructions[0x20][3] = MI + RO
instructions[0x20][4] = RO + BI
instructions[0x20][5] = EO + AI + CE + FI
instructions[0x20][6] = TR

# INC- 0x21->0x2e
for i in range(0, 0xe):
	instructions[0x21+i][2] = IO + BI
	instructions[0x21+i][3] = EO + AI + FI
	instructions[0x21+i][4] = TR

# ADDN-0x29
instructions[0x2f][2] = MI + CO
instructions[0x2f][3] = RO + BI
instructions[0x2f][4] = EO + AI + CE + FI
instructions[0x2f][5] = TR

# SUB-0x30
instructions[0x30][2] = MI + CO
instructions[0x30][3] = MI + RO
instructions[0x30][4] = RO + BI
instructions[0x30][5] = EO + AI + SU + CE + FI
instructions[0x30][6] = TR

# DEC- 0x31->0x3e
for i in range(0, 0xe):
	instructions[0x31+i][2] = IO + BI
	instructions[0x31+i][3] = EO + AI + SU + CE + FI
	instructions[0x31+i][4] = TR
	
# SUBN-0x3f
instructions[0x3f][2] = MI + CO
instructions[0x3f][4] = RO + BI
instructions[0x3f][5] = EO + AI + SU + CE + FI
instructions[0x3f][6] = TR

# SAR-0x49
instructions[0x49][2] = AI + L2 + L1 + L0 + FI
instructions[0x49][3] = TR

# Logical Operators
#################################################

# NOT-0x40
instructions[0x40][2] = L2
instructions[0x40][3] = TR

# AND-0x41
instructions[0x41][2] = MI + CO
instructions[0x41][3] = RO + MI
instructions[0x41][4] = RO + BI
instructions[0x41][5] = AI + L0 + CE + FI
instructions[0x41][6] = TR

# ANDN-0x42
instructions[0x42][2] = MI + CO
instructions[0x42][3] = RO + BI
instructions[0x42][4] = AI + L0 + CE + FI
instructions[0x42][5] = TR

# OR- 0x43
instructions[0x43][2] = MI + CO
instructions[0x43][3] = RO + MI
instructions[0x43][4] = RO + BI
instructions[0x43][5] = AI + L1 + CE + FI
instructions[0x43][6] = TR

# ORN- 0x44
instructions[0x44][2] = MI + CO
instructions[0x44][3] = RO + BI
instructions[0x44][4] = AI + L1 + CE + FI
instructions[0x44][5] = TR


# XOR- 0x45
instructions[0x45][2] = MI + CO
instructions[0x45][3] = RO + MI
instructions[0x45][4] = RO + BI
instructions[0x45][5] = AI + L0 + L1 + CE + FI
instructions[0x45][6] = TR

# XORN- 0x46
instructions[0x46][2] = MI + CO
instructions[0x46][3] = RO + BI
instructions[0x46][4] = AI + L0 + L1 + CE + FI
instructions[0x46][5] = TR

# SHL-0x47
instructions[0x47][2] = AI + L2 + L0 + FI
instructions[0x47][3] = TR

# SHR-0x48
instructions[0x48][2] = AI + L2 + L1 + FI
instructions[0x48][3] = TR


# Program Flow
#################################################

# JMP-0x60
instructions[0x60][2] = MI + CO
instructions[0x60][3] = RO + J + CE
instructions[0x60][4] = TR

# JLZ-0x61 (IO|JLZ)
instructions[0x61][2] = MI + CO
instructions[0x61][3] = RO + JLZ + CE
instructions[0x61][4] = TR

# JGZ-0x62
instructions[0x62][2] = MI + CO
instructions[0x62][3] = RO + JLZ + INV + CE
instructions[0x62][4] = TR

# JC-0x63
instructions[0x63][2] = MI + CO
instructions[0x63][3] = RO + JC + CE
instructions[0x63][4] = TR

# JNC-0x64
instructions[0x64][2] = MI + CO
instructions[0x64][3] = RO + JC + INV + CE
instructions[0x64][4] = TR

# JZ-0x65
instructions[0x65][2] = MI + CO
instructions[0x65][3] = RO + JZ + CE
instructions[0x65][4] = TR

# JNZ-0x66
instructions[0x66][2] = MI + CO
instructions[0x66][3] = RO + JZ + INV + CE
instructions[0x66][4] = TR

# OUT-0xe0 (AO|OI)
instructions[0xe0][2] = AO + OI
instructions[0xe0][3] = TR
	
# HLT-0xFF (HLT)
instructions[0xff][2] = HLT

##############################################

# write instructions to file
for instr in instructions:
	file.write(" ".join(['{:06X}'.format(microcode) for microcode in instr]))
	file.write(" ")
file.close()
