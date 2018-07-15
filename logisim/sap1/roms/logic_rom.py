file = open("logic_rom.rom", "w")
file.write("v2.0 raw\n")

# Output Disabled (NOP)
for i in range(0, 256):
	file.write("00 ")

# AND
# LOP=001
for i in range(0, 256):
	file.write('{:02X}'.format((((i >> 4) & (i % 16)) << 4) + ((i >> 4) & (i % 16))) + " ")
	#print i, bin(i >> 4), bin(i % 2**4)
	
# OR
# LOP=010
for i in range(0, 256):
	file.write('{:02X}'.format((((i >> 4) | (i % 16)) << 4) + ((i >> 4) | (i % 16))) + " ")
	
# XOR
# LOP=011
for i in range(0, 256):
	file.write('{:02X}'.format((((i >> 4) ^ (i % 16)) << 4) + ((i >> 4) ^ (i % 16))) + " ")

# NOT
# LOP=100
for i in range(0, 256):
	file.write('{:02X}'.format((~i%256)) + " ")
	
# Logical Left Shift (SHL)
# LOP=101
for i in range(0, 256):
	file.write('{:02X}'.format((i<<1)%256) + " ")
	
# Logical Right Shift (SHR)
# LOP=110
for i in range(0, 256):
	file.write('{:02X}'.format((i>>1)%256) + " ")
	
# Arithmetic Shift Right (SAR)
# LOP=111
for i in range(0, 256):
	file.write('{:02X}'.format(((i>>1)%256) | (i & 0x1 << 7)) + " ")
