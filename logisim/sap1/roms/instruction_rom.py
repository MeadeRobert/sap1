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
JLZ = 1 << 7

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
		
# NOP-0x00 ()

# LDA-0x01 (IO|MI, RO|AI)
instructions[1][2] = MI + CO
instructions[1][3] = MI + RO
instructions[1][4] = RO + AI + CE
instructions[1][5] = TR

# ADD-0x02 (IO|MI, RO|BI, EO|AI)
instructions[2][2] = MI + CO
instructions[2][3] = MI + RO
instructions[2][4] = RO + BI
instructions[2][5] = EO + AI + CE 
instructions[2][6] = TR

# SUB-0x03 (IO|MI, RO|BI, EO|AI)
instructions[3][2] = MI + CO
instructions[3][3] = MI + RO
instructions[3][4] = RO + BI
instructions[3][5] = EO + AI + SU + CE
instructions[3][6] = TR

# STA-0x04 (IO|MI, AO|RI)
instructions[4][2] = MI + CO
instructions[4][3] = MI + RO
instructions[4][5] = RO + AI + CE
instructions[4][6] = TR

# JMP-0x06
instructions[6][2] = MI + CO
instructions[6][3] = RO + J + CE
instructions[6][4] = TR

# JLZ-0x7 (IO|JLZ)
instructions[7][2] = IO + JLZ

# OUT-0xe0 (AO|OI)
instructions[0xe0][2] = AO + OI
instructions[0xe0][3] = TR

# ADDS-0x20
for i in range(0, 16):
	instructions[0x20+i][2] = IO + MI
	instructions[0x20+i][3] = RO + BI
	instructions[0x20+i][4] = EO + AI
	instructions[0x20+i][5] = TR

# SUBS-0x30
for i in range(0, 16):
	instructions[0x30+i][2] = IO + MI
	instructions[0x30+i][3] = RO + BI
	instructions[0x30+i][4] = EO + AI + SU
	instructions[0x30+i][5] = TR

# STAS-0x40
for i in range(0, 16):
	instructions[0x40+i][2] = IO + MI
	instructions[0x40+i][3] = AO + RI
	instructions[0x40+i][4] = TR

# LDI-0x50
for i in range(0, 16):
	instructions[0x50+i][2] = IO + AI
	instructions[0x50+i][3] = TR

# JS-0x60
for i in range(0, 16):
	instructions[0x60+i][2] = IO + J
	instructions[0x60+i][3] = TR

	
	
# HLT-0xFF (HLT)
instructions[0xff][2] = HLT

# write instructions to file
for instr in instructions:
	file.write(" ".join(['{:06X}'.format(microcode) for microcode in instr]))
	file.write(" ")
file.close()

print(instructions)
print(len(instructions))

