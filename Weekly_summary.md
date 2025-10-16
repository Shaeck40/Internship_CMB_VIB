# Internship_CMB_VIB
Progress of my internship @ VIB_CMB

## 18092025
Installed the necessary software (VS code, linked it to my Githubaccount, JDBrowse, 7-zip, RadminViewer), downloaded genome data.
I got an introduction on the WGSPichiapipeline and get to know how to use JDBrowse.

## 25092025
A summary of the use of the WGS pipeline, including which data is used for the analysis, the required analysis steps, and how to clean and organize the data. 
An overview of how to use JBrowse2, including how to interpret the results and visualizations. 
Practical application of the pipeline: I conducted three analyses independently. I then uploaded the results to JBrowse2 and examined them for confirmation of mutations in both long and short reads. 
As JBrowse2 frequently crashed, Daria recommended installing IGV. After completing the installation and reviewing the user manual, I was able to continue with further analysis
## 02102025
Further analysis using the WGSpipeline. 

Checking long and short reads with JBrowse2 for confirmation of mutations. 

The long reads of OpenPichia did not seem visible in JBrowse2, neither was de bamfile of the long reads visible. Did some research and found out that all the variants where not coded like the reference genome so it could not find it`s match. 

Together with Daria looked for a solution (changed the vcf file for the long reads) and also compared genomes of NCBIv2 and OPenPichia. 
## 09102025
I wrote a Python script to compare 2 vcf files (comparison_vcf_extended2.py)
Used the results of this Pythonscript to check the genome vs genome alignment of OPENPicha vs NVBIv2.
I used the WGS pipeline to produce the last files (Analysis A7 and A8) and used those files in JBrowse2.

##16102025
Checked with JBrowse2 if the variants (present in file unique_to_vcf1.vcf, these are variants unique to CBS and not present in NVBIv2) are confirmed by short and long reads. 

Discussed the results of last week (unique to vcf2) because some variants were not seen in the ref.genome of OPENPichia. Daria suggested it could be better to do a chromosome-to -chromosome allignment instead of genome -to --genome allignment. The paf files of the genome to genome allignment seem to have irregularities. 

Because no long reads were seen in this analysis I checked the vcf and bam files. The chromosome names had suffixes and could not match any genome in the JBrowse2. The vcf file was changed with Notepad++(outputlrchanged.vcf) but the bam file was changed with commands in het commandline (usage of samtools to change bam <-> sam-file and sed command). Files: reference_cleaned>sam/bam. 

Looked voor Gene ontologytools: 
DEEPROTGO 
FAIRFUN4Biodiversity 
GetENRICH(Beschikbaar als webinterface én command-line tool.) 
