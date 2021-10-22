import re
def gc_blocks(seq, block_size):
    blocks = re.findall('.{' + str(block_size) + '}', seq, re.IGNORECASE)
    gc_tot = seq.count('G') + seq.count('C')
    gc_count = []
    for block in blocks:
        gc_count.append((block.count('G') + block.count('C')) / len(block))
    return tuple(gc_count)

def gc_map(seq, block_size, gc_thres):
    seq = seq.lower()
    blocks = re.findall('.{' + str(block_size) + '}', seq, re.IGNORECASE)
    gc_tot = seq.count('g') + seq.count('c')
    for block in blocks:
        percent = (block.count('g') + block.count('c')) / gc_tot
        print(percent)
        if percent > gc_thres:
            seq = seq.replace(block, block.upper())
    return seq

def read_fasta(file):
    with open(file, 'r') as f:
        descriptor = f.readline().rstrip()

        seq = ''
        line = f.readline().rstrip()
        while line != '':
            seq += line
            line = f.readline().rstrip()
    
    return descriptor, seq


# seq = 'ACGGTCGAC'
# seq = seq.lower()
# print(seq)
# block_size = 4
# print(seq.replace('acgg', 'ACGG'))

print(gc_map('ATGACTACGT', 4, 0.4))

descriptor, seq = read_fasta('data/salmonella_spi1_region.fna')
print(gc_blocks(seq, 1000))
