LD A 60
LD B 66
LD C -87
LD D -123
CLR
LD &4 A
LD &5 B
LD &6 C
LD &7 D
LD &8 D
LD &9 C
LD &10 B
LD &11 A
NOP
LD A 4
NOP
LD B &A
NOP ROL B B ;550800
LD &A B
ADD A A 1
EQ B A 12
JNZ B 14
PCU 0
PCL 16