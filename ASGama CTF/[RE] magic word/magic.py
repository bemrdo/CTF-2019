magic = [0x0C0,0x0C3,0x0C1,0x0C2,0x0D8,0x57,0x50,0x0D8,0x57,0x53,0x0D8,0x57,0x51,0x0D8,0x57,0x52,0x1A,0x8C,0x97,0x0D8,0x6F,0x50,0x14,0x4B,0x0E5,0x66,0x0D8,0x6F,0x58,0x29,0x0F4,0x0FA,0x90,0x19,0x94,0x0B4,0x1A,0x87,0x18,0x0C4,0x0B4,0x94,0x2B,0x7B,0x88,0x0D8,0x1D,0x94,0x8F,0x1A,0x80,0x18,0x0C4,0x0B4,0x96,0x1A,0x0C4,0x0B4,0x94,0x18,0x80,0x1A,0x0C4,0x0B4,0x96,0x18,0x0C4,0x0B4,0x94,0x6F,0x53,0x0AB,0x8C,0x0B4,0x0E5,0x71,0x18,0x87,0x0D8,0x6F,0x5B,0x0D8,0x1D,0x84,0x8F,0x0F6,0x1B,0x92,0x0F6,0x6F,0x58,0x0F6,0x19,0x92,0x6F,0x59,0x15,0x59,0x0E5,0x2C,0x0D8,0x13,0x54,0x98,0x0CA,0x0C9,0x0CB,0x0C8,0x53]

cigam = "mbO`^Ifco^DfifPqf@buMf^iFal@flRqQr"
result = []
for i in cigam:
    result.append(chr(ord(i) ^ 144))

print cigam
print ''.join(result)
