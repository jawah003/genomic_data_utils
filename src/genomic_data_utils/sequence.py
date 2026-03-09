import math

class DnaSequence:
    def __init__(self, sequence):
        # Store the sequence as an attribute of the object
        self.sequence = sequence

    def calculate_gc(self):
        """Calculates the GC content of the sequence"""
        guanine = "G"
        cytosine = "C"
        gc = ((self.sequence.count(guanine) + self.sequence.count(cytosine))/len(self.sequence))*100
        return gc
    
    def transcribe(self):
        """Transcribes the given sequence"""
        rna = self.sequence.replace("T", "U")
        return rna
    
sequence = DnaSequence("ATGC")
sequence_gc = sequence.calculate_gc()
sequence_rna = sequence.transcribe()
print(sequence_gc)
print(sequence_rna)