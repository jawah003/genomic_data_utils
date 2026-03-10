def count_kmers(sequence: str, k: int) -> dict[str, int]:
    """
    Calculates the frequency of all k-mers in a given DNA sequence.

    Parameters
    ----------
    sequence : str
        The nucleotide sequence to analyze.
    k : int
        The length of the k-mers to extract.

    Returns
    -------
    dict[str, int]
        A dictionary mapping each k-mer to its frequency.
    """
    # Handle edge cases gracefully
    if not sequence or k <= 0 or k > len(sequence):
        return {}

    kmer_counts = {}
    
    # Calculate the stopping point to avoid an IndexError
    limit = len(sequence) - k + 1
    
    for i in range(limit):
        # Extract the window
        kmer = sequence[i:i+k]
        
        # .get() retrieves the current count, defaulting to 0 if not found, then adds 1
        kmer_counts[kmer] = kmer_counts.get(kmer, 0) + 1

    return kmer_counts