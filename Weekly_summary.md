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
##09102025
To do's
Compare A5/A6 ( Ask Daria for confirmation on duplication on chromM?) and A7/A8
Adding link to githubacount to IDP. 
Searching for PID of reference genomes to add to the document involving FAIR.

I wrote a Python script to compare 2 vcf files (comparison_vcf.py))
I used the WGS pipeline to produce the last files (Analysis A7 and A8) and used those files in JBrowse2.

