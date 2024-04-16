# SPECS_scraper
This is an unofficial script to get results from specs.cmgg.be/gene_data (SPECS: A non-parametric method to identify tissue-specific molecular features for unbalanced sample groups).

SPECS is a score, that will allow you to understand, what tissue a gene is most expressed in (https://github.com/celineeveraert/SPECS).
A Website based on GTEX data can be found here (https://specs.cmgg.be/).

I wrote a python script that allows to input a list of genes (Ensemble ID) and get an data_frame with the top 5 tissues a gene is expressed in based on SPECS Score by accessing the SPECS Website.

To run the script you just have to install python, pandas and reques (via pip3) and change the input and output path. Your input .csv should contain a "Ensemble_ID" column with the Ensemble IDs.

Disclaimer: This repository and its created data artefacts are unnofficial. For official, up-to-date data, please visit specs.cmgg.be.
