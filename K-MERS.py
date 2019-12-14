import operator

with open('FASTA.txt', 'r') as f:
    seq = ""
    key = ""

    index_list = []
    sequence_list = []
    for line in f.readlines():
        if line.startswith(">"):
            if key and seq:
                index_list.append(key)
                sequence_list.append(seq)
            key = line[1:].strip()
            seq = ""
        else:
            seq += line.strip()
    index_list.append(key)
    sequence_list.append(seq)


j = 0
for k in range(3, 8):
    kmers = []
    pos = []
    seq = []
    for j in range(len(sequence_list)):
        for l in range(len(sequence_list[j]) - k + 1):
            kmers.append(sequence_list[j][l:l + k])
            seq.append(j)
            pos.append(l)

    with open('db-' + str(k) + '.txt', 'w') as fout:
        for i in range(len(kmers)):
            fout.write(kmers[i] + '\t' + str(seq[i]) + '\t' + str(pos[i]) + '\n')