
filename = input("Enter the FASTA filename: ")

with open(filename, 'r') as inp:
    print(filename + " opened")

    seq_input = ""
    key_input = ""

    index_input = []
    sequence_input = []
    for line in inp.readlines():
        if line.startswith(">"):
            if key_input and seq_input:
                index_input.append(key_input)
                sequence_input.append(seq_input)
            key_input = line[1:].strip()
            seq_input = ""
        else:
            seq_input += line.strip()
    index_input.append(key_input)
    sequence_input.append(seq_input)
k_value = input("Enter the value of k: ")
print(k_value, "- mers will be formed")

j=0
l=0
kmers_input = []
pos_input = []
seq_input = []

match_file_kmers = []
match_file_pos = []
match_file_sequence = []

for j in range(len(sequence_input)):
    for l in range(len(sequence_input[j]) - (int(k_value)) + 1):
        kmers_input.append(sequence_input[j][l:l + (int(k_value))])
        seq_input.append(j)
        pos_input.append(l)

# print(kmers_input)

with open ('db-' + k_value + '.txt', 'r') as match_file:
    line = match_file.readline()
    while line:
        match_file_kmers.append(line.split('\t')[0])
        match_file_sequence.append(line.split('\t')[1])
        match_file_pos.append(line.split('\t')[2].rstrip('\n'))
        line = match_file.readline()

# print(match_file_kmers)
# print(match_file_pos)


print('KMER Name' + '\t' + 'Seq.No.in Query' + '\t' + 'Position in QUERY' + '\t' + 'Seq.No. in DB' + '\t' + 'Position in DB')

for i in range(len(kmers_input)):
    if kmers_input[i] in match_file_kmers:
        db_index = match_file_kmers.index(kmers_input[i])
        match_file_kmers[db_index] = ''
        print('%s' % (kmers_input[i]) + '\t\t' + '%d' % int(seq_input[i]) + '\t\t\t' + '%d' % int(pos_input[i]) + '\t\t\t' + '%d' % int(match_file_sequence[db_index]) + '\t\t\t' + '%d' % int(match_file_pos[db_index]))
        # print('%d seq in QUERY' % int(seq_input[i]))
        # print('%d position in QUERY' % int(pos_input[i]))
        # print('%d seq in DB' % int(match_file_sequence[db_index]))
        # print('%d position in DB' % int(match_file_pos[db_index]))

# for k in range(len(match_file_kmers)):
# for m in range(len(kmers_input)):
