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

## 16102025
Checked with JBrowse2 if the variants (present in file unique_to_vcf1.vcf, these are variants unique to CBS and not present in NVBIv2) are confirmed by short and long reads. 

Discussed the results of last week (unique to vcf2) because some variants were not seen in the ref.genome of OPENPichia. Daria suggested it could be better to do a chromosome-to -chromosome allignment instead of genome -to --genome allignment. The paf files of the genome to genome allignment seem to have irregularities. 

Because no long reads were seen in this analysis I checked the vcf and bam files. The chromosome names had suffixes and could not match any genome in the JBrowse2. The vcf file was changed with Notepad++(outputlrchanged.vcf) but the bam file was changed with commands in het commandline (usage of samtools to change bam <-> sam-file and sed command). Files: reference_cleaned>sam/bam. 

Looked voor Gene ontologytools: 
DEEPROTGO 
FAIRFUN4Biodiversity 
GetENRICH(Beschikbaar als webinterface én command-line tool.) 

## 23102025
Checked to confirm an insertion in CBS in comparison to NCBIv2. 
Used samtools in VScode to get the longreads filtered on length so we could see which longreads overlap the area of insertion. 

Installed Rstudio en libraries to get started with gene-ontology. 
Adapted via Rstudio Quickgo (gene ontology table ) and a Excellfile (differential expression results )to have the correct columns for the GSEA in Rstudio. 

## 28102025
Reviewed and modified the existing RStudio code for gene annotation using GSEA. Updated the workflow to generate three separate TSV tables corresponding to Biological Processes (BP), Molecular Functions (MF), and Cellular Components (CC).

Enhanced the code to produce well-scaled dot plots using clusterProfiler, including one dot plot per condition and per gene annotation, as well as network plots.

Additionally, implemented custom dot plot generation directly from the TSV tables, allowing comparison of gene enrichment or suppression across different conditions.

## 30102025
Changed the code in Rstudio to make well visualised netwerkplots(plots with gene labels and plots without gene lables). Used documentation to find out which settings needed to be changed.Saved the plots as pdf and .png files locally and in the cloud.  

## 06112025
Tried to install the Fantasia annotation tool on the laptop of VIB (didn’t went smoothly_lot of errors) 
The proposal of Daria was to check if this tool suggest more GO terms in comparison with the gene annotation done last week with Quick GO.  
I ran the Fantasia pipeline with the 2 refseq (Uniprot and NCBI). There were no results. I changed the header of one of these fasta files to see if it would change but no results.  
While installing the tool I checked the last vcf mutations in JBrowse between NCBI and CBS. 
Added code to the Rstudioproject for gsea so that every table (F,BP and C) was compared with a UNiPROT dataset. If the proteins in the “core enrichment” colum of the tsv table were also present in the Uniprot table, the gene name (present in Uniprot data) was added to an extra colum in the tsv tables. 
Search for installation guides for a functional annotation tool (Fantasia)

## 13112025

=======
