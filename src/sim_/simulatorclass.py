from instruc import *
#---------------DONT DELETE THIS FOR NOWwWWWWWWWWWWWWWWWWWWW--------------
# def read(instruc):
#     opcode = instruc[-1:-8:-1]
    
#     opcode = opcode[::-1]
#     if opcode == list(R_.values())[1][0]:
#         x =parse(instruc,[7,12,17,20,25,32])
#     elif opcode in [i[0] for i in I_.values()]:
#         x =parse(instruc,[12,17,20,25,32])
#         execute_I(x)
#     elif opcode in [i for i in S_.values()]:
#         x =parse(instruc,[7,12,17,20,25,32])
#     elif opcode == list(B_.values())[1][0]:
#         x=parse(instruc,[7,12,17,20,25,32])
#     elif opcode in [i for i in U_.values()]:
#         x=parse(instruc,[20,25,32])
#     elif opcode in [i for i in J_.values()]:
#         x=parse(instruc,[20,25,32])
#     elif opcode in [i for i in bonus_.values()]:
#         pass
#     else:
#         raise Exception (f"{opcode} is an invalid opcode")   
    

# read('00000000001000011000000100010011')


class simulator:
    def __init__(self,instruc:list,pc:int):
        self.instruc_list = instruc
        self.pc = pc
        #opcode diff for same type instruc asw
    # def pc_incr(self): #either pc increment b4 instr execution OR start pc = 4
    #     self.pc += 4
    def print_state(self, outpf):
        prefix = '0b'
        w = ''
        w+= prefix+format(self.pc,'032b')+' '
        print(prefix+format(self.pc,'032b'),end = ' ')
        for reg_v in list(reg_vals.values()):
            if reg_v >= 0:
                w+=prefix+format(reg_v,'032b') + ' '
                print(prefix+format(reg_v,'032b'),end = ' ')
            else:
                reg_v = 2**32 + reg_v
                w+=prefix+format(reg_v,'032b') + ' '
                print(prefix+format(reg_v,'032b'),end = ' ')
        w += '\n'
        with open(outpf,'a') as f:
            f.write(w)
        
        print('pc = ', self.pc)
        print('s0 = ', reg_vals['01000'])
        print('s1 = ', reg_vals['01001'])
        print('s2 = ', reg_vals['10010'])
        print('s3 = ', reg_vals['10011'])
        print()
        return w
    def print_mem(self, outpf):
        prefixB, prefixH,w = '0b', '0x', ''
        for i in range(65536, 65661,4):
            mem_k = i; mem_v = mem[mem_k]
            # print('memk = ', mem_k)
            w += prefixH+format(mem_k,'08x')+':'
            print(prefixH+format(mem_k,'08x')+':', end = '')
            if mem_v>=0: 
                w += prefixB+format(mem_v,'032b') + '\n'
                print(prefixB+format(mem_v,'032b'))

            else: 
                w += prefixB+format(mem_v+2**32,'032b') + '\n'
                print(prefixB+format(mem_v+2**32,'032b'))
        with open(outpf,'a') as f:
            f.write(w)
        return w
        
    def execute(self, outpf):
        while self.instruc_list[self.pc//4] != '00000000000000000000000001100011':
        # for i in range(30):
            pointer = self.pc//4
            print(pointer)
            opcode = self.instruc_list[pointer][-7:] 
            # print([i for i in S_.values()])
            ex = None
            if opcode == list(R_.values())[1][0]:
                ex = R_type(self.instruc_list[pointer], self.pc)
                
            elif opcode in [i[0] for i in I_.values()]:
                ex = I_type(self.instruc_list[pointer],self.pc)
            elif opcode in [i[0] for i in S_.values()]:
                ex = S_type(self.instruc_list[pointer], self.pc)
            elif opcode == list(B_.values())[1][0]:
                ex = B_type(self.instruc_list[pointer], self.pc)
            elif opcode in [i for i in U_.values()]:
                ex = U_type(self.instruc_list[pointer], self.pc)
            elif opcode in [i for i in J_.values()]:
                ex = J_type(self.instruc_list[pointer],self.pc) 
            elif opcode in [i for i in bonus_.values()]:
                pass
            else:
                raise Exception (f"{opcode} is an invalid opcode")
            ex.execute()
            reg_vals['00000'] = 0 #zero reg is hard wired 0, so any changes to it must be reverted
            self.pc = ex.pc
            if self.pc < 0:
                self.pc = 2**32 + self.pc
                self.print_state(outpf)
                break
            self.print_state(outpf)
            # print(format(self.pc,'032b'))
        self.print_state(outpf)
        self.print_mem(outpf)

# print('''0b00000000000000000000000000000100 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000100000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000'''=='''0b00000000000000000000000000000100 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000100000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000 0b00000000000000000000000000000000''')