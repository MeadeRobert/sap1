# 8-Bit Computer Assembly RMX (Robert Meade Assembly) version H0.1 (Hardware 0.1)

## Misc Instructions

**NOP (0x00)**- No operation, wait 8 T-states and then fetch next instruction
*note: instructions bytes not used are programmed as NOP instructions*

**HLT (0xff)**- Halt; Halt and Catch Fire (HCF)

## Basic Memory Operations

**LDA (0x01)**- Load A; puts value in memory location specified by next byte into the A register

**LDAI (0x10->0x1f)**- Load A  Immediate; takes the value of the least significant 4 bits of the instruction and puts it in the A register

**LDAN (0x02)**- Load A Next; takes the value of the next bytes and puts it directly into the A register

**STA (0x03)**- Store A; stores the value in the A register in the memory location specified by the next byte in memory

## Addition/Subtraction

**ADD (0x20)**- Add; adds the value at the location in memory specified by the next byte and updates flags accordingly

**INC (0x21->0x2e)**- Increment (Add Immediate); adds the value contained in the least significant 4 bits of the instruction byte to the A register and updates flags accordingly

**ADDN (0x2f)**- Add Next; adds the value contained in the next byte of memory to the A register and updates flags accordingly

**SUB (0x30)**- Subtract; subtracts the value at the location in memory specified by the next byte and updates flags accordingly

**DEC (0x31->0x3e)**- Decrement (Subtract Immediate); subtracts the value contained in the least significant 4 bits of the instruction byte to the A register and updates flags accordingly

**SUBN (0x3f)**- Subtract Next; subtracts the value contained in the next byte of memory to the A register and updates flags accordingly

## Logical Operators

**NOT (0x40)**- Logical Not (bitwise); applies the bitwise NOT operator to the contents of the A register, places the result in the A register, and updates flags accordingly

**AND (0x41)**- Logical And (bitwise); applies the bitwise AND operator to the contents of the A register and the value at the location in memory specified by the next byte in memory, places the result in the A register, and updates flags accordingly 

**ANDN (0x42)**- Logical And Next (bitwise); applies the bitwise AND operator to the contents of the A register and the value held in the next byte of memory, puts the result in the A register, and updates flags accordingly

**OR (0x43)**- Logical OR (bitwise); aplies the bitwise OR operator to the contents of the A register and the value at the location in memory specified by the next byte in memory, places the result in the A register, and updates flags accordingly

**ORN (0x44)**- Logical OR Next (bitwise); applies the bitwise OR operator to the contents of the A register and the value held in the next byte of memory, puts the result in the A register, and updates the flags accordingly

**XOR (0x45)**- Logical XOR (bitwise); aplies the bitwise XOR operator to the contents of the A register and the value at the location in memory specified by the next byte in memory, places the result in the A register, and updates flags accordingly

**XORN (0x46)**-  Logical XOR Next (bitwise); applies the bitwise XOR operator to the contents of the A register and the value held in the next byte of memory, puts the result in the A register, and updates the flags accordingly

## Bit Shifts and Rotates

**SHL (0x47)**- Shift Left- shifts the contents of the A register 1 bit to the left and updates flags accordingly

**SHR (0x48)**- Shift Right- shifts the contents of the A register 1 bit to the right and updates flags accordingly

**ROL (0x49)**- Rotate Left- rotates the contents of the A register 1 bit to the left and updates flags accordingly

**ROR (0x4a)**- Rotate right- rotates the contents of the A register 1 bit to the right and updates flags accordingly

**SAL (0x4b)**- Arithmetic Shift Left- shifts the contents of the A register 1 bit to the left and updates flags accordingly

**SAR (0x4c)**- Arithmetic Shift Right- shifts the contents of the A register 1 bit to the right, preserving the sign bit, and updates flags accordingly

## Jump Instructions

**JMP (0x60)**- Jump Unconditionally- Performs an unconditional jump to the location in memory specified by the next byte in memory

**JLZ (0x61)**- Jump Less Than Zero- Performs a jump to the location in memory specified by the next byte in memory if the sign flag is set

**JGZ (0x62)**- Jump Greater Than Zero- Performs a jump to the location in memory specified by the next byte in memory if the sign flag is not set

**JC (0x63)**- Jump Carry- Performs a jump to the location in memory specified by the next byte in memory if the carry flag is set

**JNC (0x64)**- Jump Not Carry- Performs a jump to the location in memory specified by the next byte in memory if the carry flag is not set

**JZ (0x63)**- Jump Zero- Performs a jump to the location in memory specified by the next byte in memory if the zero flag is set

**JNZ (0x64)**- Jump Not Zero- Performs a jump to the location in memory specified by the next byte in memory if the zero flag is not set

## Comparison Instructions

**CMP (0x07)**- Compare; Updates flags based on the result of subtraction between the value in the A register and the value in the memory location specified by the next bytes in memory without updating the contents of the A register

**CMPI (0x70->0x7e)** Compare Immediate; Updates the flags based on the result of subtraction between the value in the A register and the value in the least significant 4 bits of this instruction byte without altering the contents of the A register

**CMPN (0x7f)** Compare Next; Updates the flags based on the result of subtraction between the value in the A register and the value in the next byte of memory without altering the contents of the A register

**CMP_NLD (0xf1)** Compare No Load; Updates the flags based on the result of subtraction between the value in the B register and the value in the A register without altering the contents of the A register

## Stack Operations

**LSP (0x80)**- Load Stack Pointer; initializes the location of the stack in memory to an arbitrary value stored in the memory location referred to by the next byte in memory

**LSPN (0x81)**- Load Stack Pointer Next; initializes the location of the stack in memory to an arbitrary value stored in the next byte of memory

**PSH (0x82)**- Push; pushes a value onto the stack from the A register (grows upward -> decrements stack pointer)

**POP (0x83)**- Pop; pops a value off the stack and into the A register (shrinks downward -> increments stack pointer)

**PEEK (0x84)**- Peek; loads the value on the top of the stack into the A register

**CALL (0x90)**- Call (for function/subroutine call); calls a subroutine by pushing the current memory address referred to by the counter onto the stack and jumping to the location specified by the next byte of memory (limitation: untested)

**RET (0x91)** Return (return from a function/subroutine); picks the top value off the stack and begins execution there

## Output Instructions

**A_OUT (0xe0)**- Output A; puts the contents of the A register into the output register

**B_OUT (0xe1)**- Output B; puts the contents of the B register into the output register

**SP_OUT (0xe1)**- Output SP; puts the contents of the stack pointer (SP) register into the output register

**OUT (0x0d)**- Output; puts the value at the location in memory specified by the next byte in memory into the output register

**OUTI (0xd0->0xdf)**- Output Immediate; puts the value of the least significant 4 bits of this instruction into the output register

**OUTN (0x0e)**- Output Next; puts the value in the next byte of memory into the output register
