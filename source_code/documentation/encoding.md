# Genotype Information

Genotypes are encoded into the application via the input file which contains a YAML entry for `genotype_info`. This structure is organized as `loci` with the assoicated `alleles` that may be mutated during model execution. The following table outlines loci and alleles that are included in the sample configuration file.

**Outline of loci and allel encoding**

| Locus | Allele | Short Name | Description |
| --- | --- | --- | --- |
| PfCRT | K76 | K | Lumefantrine resistant; Amodiaquine sensitive |
| | 76T | T |  Lumefantrine sensitive; Amodiaquine resistant |
| PfMDR1 | N86 Y184, Single-Copy |  NY-- | Partial-Lumefantrine and Partial-Amodiaquine resistant |
| | 86Y Y184, Single-Copy | YY-- | Amodiaquine resistant |
| | N86 184F, Single-Copy | NF-- | Lumefantrine resistant |
| | 86Y 184F, Single-Copy | YF-- | Partial-Amodiaquine and Partial-Lumefantrine resistant |
| | N86 Y184, Double-Copy | NYNY | Partial-Lumefantrine and Partial-Amodiaquine resistant, higher strength; Mefloquine selects strongly for multi-copy |
| | 86Y Y184, Double-Copy | YYYY | Amodiaquine resistant, higher strength; Mefloquine selects strongly for multi-copy |
| | N86 184F, Double-Copy | NFNF | Lumefantrine resistant, higher strength; Mefloquine selects strongly for multi-copy |
| | 86Y 184F, Double-Copy | YFYF | Partial-Amodiaquine and Partial-Lumefantrine resistant, higher strength; Mefloquine selects strongly for multi-copy |
| K13 Propeller | C580 | C | Artemisinin sensitive |
| | 580Y | Y | Artemisinin resistant |
| Plasmepsin 2-3 | Plasmepsin 2-3 Single-Copy | 1 | Piperaquine sensitive |
| | Plasmepsin 2-3 Double-Copy | 2 | Piperaquine resistant |
| Hypothetical locus for multiple use | naïve | x | Experimental use in the model |
| | mutant | X | Experimental use in the model |

The short name field requires addtional note since genotype results generated by the model are based upon the short names. For example:

> KNY--C1x

Indicates that the parasite has the K76 allele from the pfcrt locus (K), N86 Y184 one copy of pfmdr1 (NY--), C580 from K13 Propeller locus (C), Plasmepsin 2-3 one copy (1), and is a naïve copy of the hypotehtical locus (x). 
