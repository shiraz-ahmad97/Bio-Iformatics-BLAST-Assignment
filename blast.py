
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

matched_kmers = []
matched_kmers_position = []
counter = 0

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



print ('\n                                                   MATCHED K-MERS                               \n')
print('KMER Name' + '\t\t' + 'Seq.No.in QUERY' + '\t\t' + 'Position in QUERY' + '\t\t' + 'Seq.No. in DB' + '\t\t' + 'Position in DB')

for i in range(len(kmers_input)):
    if kmers_input[i] in match_file_kmers:
        counter += 1
        db_index = match_file_kmers.index(kmers_input[i])
        match_file_kmers[db_index] = ''
        matched_kmers.append(kmers_input[i])
        matched_kmers_position.append(pos_input[i])

        print('%s' % (kmers_input[i]) + '\t\t\t\t' + '%d' % int(seq_input[i]) + '\t\t\t\t\t' + '%d' % int(pos_input[i]) + '\t\t\t\t\t' + '%d' % int(match_file_sequence[db_index]) + '\t\t\t\t\t' + '%d' % int(match_file_pos[db_index]))

print('\nNumber of matched K-MERS : %d\n' % counter)

print(matched_kmers_position)
print(kmers_input)


# cont_seq = []
# for m in range(len(matched_kmers_position)):
#     temp_a = matched_kmers_position[m+1]
#     temp_b = matched_kmers_position[m] + 1
#     # print(temp_a)
#     # print(temp_b)
#     if temp_a == temp_b:
#         # cont_seq.append(kmers_input[m:m+1])
#         # cont_seq = cont_seq.join(kmers_input[m:m + 1])
#         cont_seq.append(matched_kmers[m])
#         print("It can be a continuous sequence")
#     else:
#         print("Cannot be continuous")
#     print(cont_seq)
