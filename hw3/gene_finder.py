# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
from random import shuffle

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    # "".join(L) will work great
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    l = []
    for x in range(0,len(dna)/3*3,3): # Why do you multiply by 3 and then divide by 3 again...
        cod = dna[x:x+3]
        l.append(get_amino_acid_for_codon(cod))
    return collapse(l)
    
def get_amino_acid_for_codon(c):
    for i in range(len(codons)):
        if c in codons[i]:
            return aa[i]
       
def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """        
    
    print 'input :'+str(['ATGTGTCGTTAG']), 'expected output : MCR|', 'actual output :' + coding_strand_to_AA('ATGTGTCGTTAG')
    print 'input :'+str(['ATGCCCTGTGAATT']), 'expected output : MPCE', 'actual output :' + coding_strand_to_AA('ATGCCCTGTGAATT')

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    d = list(dna)
    for i in range(0,len(d)):
        if d[i] == 'A':
            d[i] = 'T'
        elif d[i] == 'T':
            d[i] = 'A'
        elif d[i] == 'C':
            d[i] = 'G'
        elif d[i] == 'G':
            d[i] = 'C'
    n = d[::-1]
    return collapse(n)
    
    
        
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """

    print 'input :'+str(['ATGTGTCGTTAG']), 'expected output : CTAACGACACAT', 'actual output :' + get_reverse_complement('ATGTGTCGTTAG')
    print 'input :' + str(['ATCCGT']), 'expected output : ACGGAT', 'actual output :' + get_reverse_complement('ATCCGT')

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    for i in range(0,len(dna),3):
        cod = dna[i:i+3]
        if cod == ('TAG' or 'TAA' or 'TGA'):
            return dna[0:i]
    return dna
        

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
        
    # YOUR IMPLEMENTATION HERE
    print 'input :'+str(['ATGTGTCGTTAG']), 'expected output : ATGTGTCGT', 'actual output :' + rest_of_ORF('ATGTGTCGTTAG')
    print 'input :' + str(['ATGTCTATGCCCTAA']), 'expected output : ATGTCTATGCCCTAA','actual output :' + rest_of_ORF('ATGTCTATGCCCTAA')
    
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    # YOUR IMPLEMENTATION HERE        
    # GCA TGA ATG TAG
    # ATG CGA ATG TAG CAT CAA A
    val = []
    while len(dna)>2:
        for x in range(0,len(dna),3):
            if dna[x:x+3] == 'ATG':
                k = dna[x:]
                sth = rest_of_ORF(k)
                #print dna, k, sth
                val.append(sth)
                dna = dna[x + len(sth)+3:]
                break
            else:
                dna = dna[3:]
                break
    return val
              
        
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    # YOUR IMPLEMENTATION HERE
    print 'input :'+str(['ATGCGATAGTCTATGCCC']), "expected output :['ATGCGA','ATGCCC']" , 'actual output :' + str(find_all_ORFs_oneframe('ATGCGATAGTCTATGCCC'))
    print 'input :'+str(['TCTATGCCCTA']), "expected output : ['ATGCCCTA']",'actual output :'+str(find_all_ORFs_oneframe('TCTATGCCCTA'))    
    
def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    # YOUR IMPLEMENTATION HERE
    val = []
    for j in range(0,3):
        dnanew = dna[j:]
        #print dnanew
        # ATG CGA ATG TAG CAT CAA A
        things = find_all_ORFs_oneframe(dnanew)
        #print dnanew, things
        val += things
    return val
"""
ATG CAT GAA TGT AG
TGC ATG AAT GTA G
GCA TGA ATG TAG
"""

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    # YOUR IMPLEMENTATION HERE
    print 'input :'+str(['ATGCCGAATGTACC']), "expected output: ['ATGCCGAATGTACC', 'ATGTACC']",'actual output :'+str(find_all_ORFs('ATGCCGAATGTACC'))
    print 'input :'+str(['TACGATGTACCG']), "expected output: ['ATGTACCG']",'actual output :'+str(find_all_ORFs('TACGATGTACCG'))
    
def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    # YOUR IMPLEMENTATION HERE
    val = []
    k = find_all_ORFs(dna)
    val = k
    revdna = get_reverse_complement(dna)
    l = find_all_ORFs(revdna)
    val += l
    return val
    
def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    # YOUR IMPLEMENTATION HERE
    print 'input :'+str('ATGCTAAGGTAGTTGTGATAA'), "expected output: ['ATGCTAAGG']",'actual output :'+str(find_all_ORFs_both_strands('ATGCTAAGGTAGTTGTGATAA'))
    print 'input :'+str('TAGCGATGTTCTGAGGTAA'), "expected output: ['ATGTTCTGAGGTAA']",'actual output :'+str(find_all_ORFs_both_strands('TAGCGATGTTCTGAGGTAA'))
    print 'input :' + str('ATGCGAATGTAGCATCAAA'),"expected output: ['ATGCGAATG', 'ATGCTACATTCGCAT']",'actual output :'+str(find_all_ORFs_both_strands('ATGCGAATGTAGCATCAAA'))
def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    # YOUR IMPLEMENTATION HERE
    k = find_all_ORFs_both_strands(dna)
    return max(k, key=len)
    

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    # YOUR IMPLEMENTATION HERE
    print 'input :'+str('ATGCCGTTGTACAGTTAGG'), "expected output: ATGCCGTTGTACAGT",'actual output :'+str(longest_ORF('ATGCCGTTGTACAGTTAGG'))
    print 'input :'+str('TGCAATATGCGATTTTAG'), "expected output: ATGCGATTT",'actual output :'+str(longest_ORF('TGCAATATGCGATTTTAG'))
    
def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    # YOUR IMPLEMENTATION HERE
    a = list(dna)
    shuffle(a)
    b = collapse(a)
    c = longest_ORF(b)
    return c


def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """

    # YOUR IMPLEMENTATION HERE
    val = []
    a = find_all_ORFs_both_strands(dna)
    for i in a:
        if len(i) >= threshold:
            a = coding_strand_to_AA(i)
            val.append(a)
        return val
            
'''
I used gene_finder with the salmonella dna data and a threshold of about 800 because
after I did a couple of random trials I got numbers from about 600 to 1200. So, I decided
to go with 800 as the threshold.

['MGIFASAGCGKTMLMHMLIEQTEADVFVIGLIGERGREVTEFVDMLRASHKKEKCVLVFATSDFPSVDRCNAAQ
LATTVAEYFRDQGKRVVLFIDSMTRYARALRDVALASGERPARRGYPASVFDNLPRLLERPGATSEGSITAFYTVL
LESEEEADPMADEIRSILDGHLYLSRKLAGQGHYPAIDVLKSVSRVFGQVTTPTHAEQASAVRKLMTRLEELQLFI
DLGEYRPGENIDNDRAMQMRDSLKAWLCQPVAQYSSFDDTLSGMNAFADQN|SIAAALYGISFTV|VDITSLSG|
GPRAAGRGGGDP|TNSGSEIVIRYAACRKQTAQS|GNLYVIT|AVYCSPADKRFRTPDYTNSGKTERAGKEKGRV
SEKK|ILVAQRRELSTLDNPSEKILYPARDTAGRGRVRGDNLMGDVSAVSSSGNILLPQQDEVGGLSEALKKAVE
KHKTEYSGDKKDRDYGDAFVMHKETALPLLLAAWRHGAPAKSEHHNGNVSGLHHNGKSELRIAEKLLKVTAEKSV
GLISAEAKVDKSAALLSSKNRPLESVSGKKLSADLKAVESVSEVTDNATGISDDNIKALPGDNKAIAGEGVRKEG
APLARDVAPARMAAANTGKPEDKDHKKVKDVSQLPLQPTTIADLSQLTGGDEKMPLAAQSKPMMTIFPTADGVKG
EDSSLTYRFQRWGNDYSVNIQARQAGEFSLIPSNTQVEHRLHDQWQNGNPQRWHLTRDDQQNPQQQQHRQQSGEE
DDA|CHCV|DRLIVANGYWRKPRQNASAMAGKRRWNIRRDRECGFG|AMQKNGGRPGLNLGTGLSMSLPLWLGRR
FLLALSTWSFPGLLQQSDRLSCPCRICPVGVYA']

This is what I got from gene_finder.
I put this in BLAST.
'''