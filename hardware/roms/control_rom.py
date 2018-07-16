rom1 = open("control_rom_1.bin", "w")
rom2 = open("control_rom_2.bin", "w")
rom3 = open("control_rom_3.bin", "w")
rom4 = open("control_rom_4.bin", "w")

# rom1 control bits
OI = 1 # output register In
BI = 1 << 1 # B register In
BO = 1 << 2 # B register Out
AI = 1 << 3 # A register In
AO = 1 << 4 # A register Out
II = 1 << 5 # Instruction Register In
IO = 1 << 6 # Instruction Register Out (4 LSB Only)
EO = 1 << 7 # ALU Out

# rom2 control bits
M = 1 << 8 # 74ls181 ALU Mode Select
S0 = 1 << 9 # 74ls181 ALU S0
S1 = 1 << 10 # 74ls181 ALU S1
S2 = 1 << 11 # 74ls181 ALU S2
S3 = 1 << 12 # 74ls181 ALU S3
L0 = 1 << 13 # Bit Shift Rom Input 0
L1 = 1 << 14 # Bit Shift Rom Input 1
L2 = 1 << 15 # Bit Shift Rom Input 2

# rom3 control bits
J = 1 << 16 # Unconditional Jump
JZ = 1 << 17 # Jump Zero Flag
JC = 1 << 18 # Jump Carry Flag
JLZ = 1 << 19 # Jump Less than Zero Flag
CO = 1 << 20 # Counter Out
CE = 1 << 21 # Count Enable
RI = 1 << 22 # RAM In
RO = 1 << 23 # RAM Out

# rom4 control bits
MI = 1 << 24 # Memory Register in
SPI = 1 << 25 # Stack Pointer In
SPO = 1 << 26 # Stack Pointer Out
Cn = 1 << 27 # ALU Carry In
INV = 1 << 28 # Flag Invert Action
FI = 1 << 29 # Flags Register Input
TR = 1 << 30 # T-State Reset
HLT = 1 << 31 # Halt and Catch Fire

# initialize rom instruction array
instructions = [[0 for i in range(0,8)] for j in range(0, 256)]

# make fetch cycle for all instructions
for instr in instructions:
	instr[0] = CO + MI
	instr[1] = RO + II + CE

# this is where the fun begins...

# NOP-0x00

# memory operations
#################################################

# LDA-0x01
instructions[1][2] = MI + CO
instructions[1][3] = MI + RO
instructions[1][4] = RO + AI + CE
instructions[1][5] = TR

# LDAI-0x10->1f
for i in range(0, 16):
	instructions[0x10+i][2] = IO + AI
	instructions[0x10+i][3] = TR
	
# LDAN-0x02
instructions[2][2] = MI + CO
instructions[2][3] = RO + AI + CE
instructions[2][4] = TR
	
# STA-0x03
instructions[0x3][2] = MI + CO
instructions[0x3][3] = MI + RO
instructions[0x3][4] = RI + AO + CE
instructions[0x3][5] = TR

	
# arithmetic operators
#################################################

# ADD-0x20
instructions[0x20][2] = MI + CO
instructions[0x20][3] = MI + RO
instructions[0x20][4] = RO + BI
instructions[0x20][5] = EO + AI + S3 + S0 + Cn + CE + FI # CN,S3,S0 -> S=0010, Cn=1, M=0 -> 74ls181 A plus B
instructions[0x20][6] = TR

# INC- 0x21->0x2e
for i in range(0, 0xe):
	instructions[0x21+i][2] = IO + BI
	instructions[0x21+i][3] = EO + AI + S3 + S0 + Cn + FI # CN,S3,S0 -> S=0010, Cn=1, M=0 -> 74ls181 A plus B
	instructions[0x21+i][4] = TR

# ADDN-0x2f
instructions[0x2f][2] = MI + CO
instructions[0x2f][3] = RO + BI
instructions[0x2f][4] = EO + AI + S3 + S0 + Cn + CE + FI # CN,S3,S0 -> S=0010, Cn=1, M=0 -> 74ls181 A plus B
instructions[0x2f][5] = TR

# SUB-0x30
instructions[0x30][2] = MI + CO
instructions[0x30][3] = MI + RO
instructions[0x30][4] = RO + BI
instructions[0x30][5] = EO + AI + S2 + S1 + CE + FI # S2,S1 -> S=0110, Cn=0, M=0 -> 74ls181 A minus B
instructions[0x30][6] = TR

# DEC- 0x31->0x3e
for i in range(0, 0xe):
	instructions[0x31+i][2] = IO + BI
	instructions[0x31+i][3] = EO + AI + S2 + S1 + FI # S2,S1 -> S=0110, Cn=0, M=0 -> 74ls181 A minus B
	instructions[0x31+i][4] = TR
	
# SUBN-0x3f
instructions[0x3f][2] = MI + CO
instructions[0x3f][4] = RO + BI
instructions[0x3f][5] = EO + AI + S2 + S1 + CE + FI # S2,S1 -> S=0110, Cn=0, M=0 -> 74ls181 A minus B
instructions[0x3f][6] = TR

# Logical Operators
#################################################

# NOT-0x40
instructions[0x40][2] = EO + Cn + M + CE + AI + FI # M,Cn -> S=0000, Cn=1, M=1 -> 74ls181 !A
instructions[0x40][3] = TR

# AND-0x41
instructions[0x41][2] = MI + CO
instructions[0x41][3] = RO + MI
instructions[0x41][4] = RO + BI
instructions[0x41][5] = EO + AI + S3 + S1 + S0 + M + Cn + CE + FI # S3,S1,S0,M,Cn -> S=1011, Cn=1, M=1 -> 74ls181 AB
instructions[0x41][6] = TR

# ANDN-0x42
instructions[0x42][2] = MI + CO
instructions[0x42][3] = RO + BI
instructions[0x42][4] = EO + AI + S3 + S1 + S0 + M + Cn + CE + FI # S3,S1,S0,M,Cn -> S=1011, Cn=1, M=1 -> 74ls181 AB
instructions[0x42][5] = TR

# OR- 0x43
instructions[0x43][2] = MI + CO
instructions[0x43][3] = RO + MI
instructions[0x43][4] = RO + BI
instructions[0x43][5] = EO + AI + S0 + Cn + CE + FI # S0,Cn -> S=0001, Cn=1, M=0 -> 74ls181 A + B
instructions[0x43][6] = TR

# ORN- 0x44
instructions[0x44][2] = MI + CO
instructions[0x44][3] = RO + BI
instructions[0x44][4] = EO + AI + S0 + Cn + CE + FI # S0,Cn -> S=0001, Cn=1, M=0 -> 74ls181 A + B
instructions[0x44][5] = TR

# XOR- 0x45
instructions[0x45][2] = MI + CO
instructions[0x45][3] = RO + MI
instructions[0x45][4] = RO + BI
instructions[0x45][5] = EO + AI + S2 + S1 + Cn + M + CE + FI # S2,S1,Cn,M -> S=0110, Cn=1, M=1 -> 74ls181 A xor B
instructions[0x45][6] = TR

# XORN- 0x46
instructions[0x46][2] = MI + CO
instructions[0x46][3] = RO + BI
instructions[0x46][4] = EO + AI + S2 + S1 + Cn + M + CE + FI
instructions[0x46][5] = TR

# SHL-0x47
instructions[0x47][2] = EO + AI + L0 + M + FI
instructions[0x47][3] = TR

# SHR-0x48
instructions[0x48][2] = EO + AI + L1 + FI
instructions[0x48][3] = TR

# ROL-0x49
instructions[0x49][2] = EO + AI + L1 + L0 + FI
instructions[0x49][3] = TR

# ROR-0x4a 
instructions[0x4a][2] = EO + AI + L2 + FI
instructions[0x4a][3] = TR

# SAL-0x4b
instructions[0x4b][2] = EO + AI + L2 + L0 + FI
instructions[0x4b][3] = TR

# SAR-0x4c
instructions[0x4c][2] = EO + AI + L2 + L1 + FI
instructions[0x4c][3] = TR

# Jump Instructions
#################################################

# JMP-0x60
instructions[0x60][2] = MI + CO
instructions[0x60][3] = RO + J + CE
instructions[0x60][4] = TR

# JLZ-0x61
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

# Comparison Instructions
#############################################

# CMP-0x07
instructions[0x70][2] = MI + CO
instructions[0x70][3] = MI + RO
instructions[0x70][4] = RO + BI
instructions[0x70][5] = EO + S2 + S1 + CE + FI # S2,S1 -> S=0110, Cn=0, M=0 -> 74ls181 A minus B

# CMPI-0x70->0x7e
for i in range(0, 0xe):
	instructions[0x70+i][2] = IO + BI
	instructions[0x70+i][3] = EO + S2 + S1 + FI # S2,S1 -> S=0110, Cn=0, M=0 -> 74ls181 A minus B
	instructions[0x70+i][4] = TR
	
# CMPN-0x7f
instructions[0x7f][2] = MI + CO
instructions[0x7f][4] = RO + BI
instructions[0x7f][5] = EO + S2 + S1 + CE + FI # S2,S1 -> S=0110, Cn=0, M=0 -> 74ls181 A minus B
instructions[0x7f][6] = TR

# CMP_NLD-0xf1
instructions[0xf1][2] = EO + S2 + S1 + CE + FI # S2,S1 -> S=0110, Cn=0, M=0 -> 74ls181 A minus B
instructions[0xf1][3] = TR

# Stack Operations
#############################

# LSP
instructions[0x80][2] = MI + CO
instructions[0x80][3] = MI + RO
instructions[0x80][4] = RO + SPI + CE
instructions[0x80][5] = TR

# LSPN
instructions[0x81][2] = MI + CO
instructions[0x81][3] = RO + SPI + CE
instructions[0x81][4] = TR

# PSH
instructions[0x82][2] = AO + BI
instructions[0x82][3] = SPO + AI
instructions[0x82][4] = EO + Cn + S3 + S2 + S1 + S0 + SPI # decrement stack pointer by 1
instructions[0x82][5] = SPO + MI
instructions[0x82][6] = BO + RI + AI
instructions[0x82][7] = TR

# POP
instructions[0x83][2] = SPO + MI + AI
instructions[0x83][3] = EO + SPI # increment stack pointer 
instructions[0x83][4] = RO + AI
instructions[0x83][5] = TR

# PEEK
instructions[0x84][2] = SPO + MI
instructions[0x84][3] = RO + AI
instructions[0x84][4] = TR

# CALL
instructions[0x90][2] = MI + CO
instructions[0x90][3] = RO + BI + CE
instructions[0x90][4] = SPO + MI
instructions[0x90][5] = CO + RI
instructions[0x90][6] = BO + MI
instructions[0x90][7] = RO + J

# RET
instructions[0x91][2] = SPO + MI
instructions[0x91][3] = RO + J
instructions[0x91][4] = AO + BI
instructions[0x91][5] = SPO + AI
instructions[0x91][6] = EO + Cn + S3 + S2 + S1 + S0 + SPI # decrement stack pointer by 1
instructions[0x91][7] = BO + AI

# Output Instructions
#############################

# A_OUT-0xe0
instructions[0xe0][2] = AO + OI
instructions[0xe0][3] = TR

# B_OUT-0xe1
instructions[0xe1][2] = AO + OI
instructions[0xe1][3] = TR

# SP_OUT-0xe2 
instructions[0xe2][2] = SPO + OI
instructions[0xe2][3] = TR

# OUT-0x0d
instructions[0x0d][2] = MI + CO
instructions[0x0d][3] = MI + RO
instructions[0x0d][4] = RO + OI + CE
instructions[0x0d][5] = TR

# OUTI-0xd0->0xdf
for i in range(0, 0xf):
	instructions[0xd0+i][2] = IO + CE
	instructions[0xd0+i][3] = TR

# OUTN-0x0e
instructions[0x0e][2] = MI + CO
instructions[0x0e][3] = RO + OI + CE
instructions[0x0e][4] = TR

#############################################

# HLT-0xff
instructions[0xff][2] = HLT

##############################################

# write binary files for control roms
for instr in instructions:
	for microcode in instr:
		rom1.write(chr(microcode & 0xff))
		rom2.write(chr((microcode & (0xff << 8)) >> 8))
		rom3.write(chr((microcode & (0xff << 16)) >> 16))
		rom4.write(chr((microcode & (0xff << 24)) >> 24))
	
rom1.close()
rom2.close()
rom3.close()
rom4.close()
