def generate_kmer_counts_table(nt_seq, kmer_num):
    k_mer_list = []
    for position in list(range(len(nt_seq))):
        nt_add = position + kmer_num
        k_mer = nt_seq[position:nt_add]
        if len(k_mer) == kmer_num:
            k_mer_list.append(k_mer)
    k_mer_counts = []
    for value in k_mer_list:
        occurrences = nt_seq.count(value)
        k_mer_counts.append(occurrences)
        data = [{k: v} for k,v in zip(k_mer_list, k_mer_counts)]
    return data
