file = open("bitshift_rom.bin", "w")

# Output Disabled (NOP)
for i in range(0, 256):
	file.write("\x00")

# Logical Left Shift (SHL)
# LOP=001
for i in range(0, 256):
	file.write(chr((i << 1) % 256))
	
# Logical Right Shift (SHR)
# LOP=010
for i in range(0, 256):
	file.write(chr(i >> 1))
	
# Rotate Left (ROL)
# LOP=011
for i in range(0, 256):
	file.write(chr((i << 1) % 256 + 1 if i & 128 == 128 else (i << 1) % 256))

# Rotate Right (ROR)
# LOP=100
for i in range(0, 256):
	file.write(chr(i >> 1 if i & 1 == 0 else (i >> 1) + 128))
	
# Arithmetic Shift Left (SAL)
# note: same as SHL
# LOP=101
for i in range(0, 256):
	file.write(chr((i << 1) % 256))
	
# Arithmetic Shift Right (SAR)
# LOP=110
for i in range(0, 256):
	file.write(chr((i >> 1) if i < 128 else (128 + (i >> 1))))
	
# NOP
# LOP=111
for i in range(0, 256):
	file.write("\x00")