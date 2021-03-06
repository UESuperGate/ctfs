from z3 import *

def re4():
    rev_endian = lambda x: (x&0xff)*0x1000000+((x>>8)&0xff)*0x10000+((x>>16)&0xff)*0x100+((x>>24)&0xff)
    equs = ['++-+----++-+--+--++-++++-+-++--+-++--+-++', '-+--+----+-+--+--+-++---+-+--++++++-----+', '-++-+--+-----+--+++++-++++-+-+-++--+++-+-', '-----++----+-+-+-+++-+++--+-++---+-+++-++', '--+--++++-++-+-++-+-+---+---+++-+--+-+---', '++++++++------+-+-++-+-+-++-+-+++---+--++', '-+++-++++-++-++++------++-+++------++--+-', '+---++-++-+-+-+-+--+-+--+-++++++-+-++++--', '--++-+++++--+-++++-++--+++-+-----+--+--+-', '++-+++----+++-++--++---+---+++-++----+-++', '-++--++----+++-+-+++-+---+--+-++--+--+-++', '-+++-++-++----+---++-+-++++-++-----++----', '---+--++-+---+-+-+----+-+-+-+--+++----+--', '-+-+-+-+-+-++++---+++--++--++---+--+---+-', '++---+-+++-+--+++----+++-+++---+++++++---', '-++++-+---+++---+----++++++----+-++++-++-', '-++--+++++-+-+++-+-+-----++++--+--+-+-+-+', '++++-+++--+-+++-+--+-+--+-+-+--+--+-+-++-', '---++-+-++---+--+++--------+++---+------+', '+++--+-------+++-++++-++-++-+++++-+---++-', '+---+-+--++--+--+--++-++--------+-++-+-+-', '---++++---------+--+-+++--+---------+---+', '+++++++-+-+-+++-++--++-+--+-+++-+----+-++', '-++----+--++--+--++--+-++-+-++-------+---', '+-++-++-++----+++-+++++++---++-+++----++-', '-++-++-+++--+-+-+++--++--+-+-+--+----+-++', '++++--+----+-+-+-+--+++++----++---++--+++', '-+-+-------++-+++++----+++-+++----+------', '-+++-++--++-+-+-+++--+----+---+--+++--+++', '+---+++-+--+-++-++-++++-++-+++++--++-++-+', '+++----++---+--+---+--++--+-------+++-+++', '+-++--++++++---++++-+-+--++-+---+-+-+-+--', '-++-++++-++-++-+-+++--+-+++------++++-+-+', '--++++--+++--++-+-+-+++--++-+------+-+---', '+-+---+++++---+-+-+--++--++++-------+++--', '-+++--++--+++--+-++---++--++--++-++++++--', '++----+++-++-++++++++--+----++++----+-++-', '--+-+----+------++---+-+--+--++-+-+--+---', '+++-+++---+++------++-+++++--++--+---+++-', '----+---+-+-++---+++++-+++++-+++++--+++-+', '---+++-++-+---++++++++-++-++-+++--++-++++', '++++++---++-+------+-+--++++------------+']
    assert len(equs) == 42
    dst_org = [rev_endian(each) for each in [2499805183, 956301311, 637599744, 687865855, 285016063, 2483159040, 2667380735, 3926261760, 3690987520, 100663296, 218103807, 4143841279, 2197487615, 3506241535, 2181103616, 3724738560, 1308688384, 2986475520, 3640197119, 1946222592, 2801467391, 3573153791, 3254845440, 2096758783, 1510146048, 1174470656, 1023410175, 351993855, 3456172032, 3691446272, 1224605695, 2550136832, 1577582592, 2969436159, 3170893823, 1845690368, 1325400063, 922288127, 3221553152, 2919628800, 2483421184, 570425344]]
    dst = [(each - 0x100000000) if (each >>31)==1 else each for each in dst_org]
    flag = [Int('f%d'%i) for i in range(42)] # f*ck BitVec
    s = Solver()
    for i,eq in enumerate(equs):
        a = flag[0]
        for j,each in enumerate(eq):
            if each == '+':
                a += flag[j+1]
            else:
                a -= flag[j+1]
        s.add(a == dst[i])

    assert sat == s.check()
    enc_flag = []
    for each in flag:
        enc_flag.append(s.model()[each].as_long())

    # de_ror
    for i in range(42):
        enc_flag[i] ^= i
        enc_flag[i] = (0xff & (enc_flag[i] << 5)) + (enc_flag[i] >> 3)
    
    final_flag = ''.join([chr(each) for each in enc_flag])
    print(final_flag)

if __name__ == '__main__':
    re4()