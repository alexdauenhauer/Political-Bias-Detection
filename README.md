# Detecting Political Bias
## W266 Final Project - Summer 2019
## Alex Dauenhauer & Ahsen Qamar

This repo attempts to bring to life our goal for our final project for W266. Helping to detect political bias in text as a way to provide more context to everyday readers of political news.

## Files
### BERT
  - `bert_train.ipynb`
    - This file houses the model training and saving aspect of this project
  - `bert_eval.ipynb`
    - This file contains the model evaluation aspect of this project
  - `convert_examples_to_features.py`, `tools.py`
    - This file contains utility functions used by both the train and eval scripts
  - `dataConverter.ipynb`
    - Used to convert sentences into tsv formats accepted by BERT
  - `dataConverterDocs.ipynb`
    - Used to convert documents into tsv formats accepted by BERT
    
### Data
  - `all-the-news.ipynb`
    - This file is used for exploring, processing and filtering the *AllTheNews* corpus
  - `convote.ipynb`
    - This file is used for exploring, processing and filtering the *Convote* corpus
  - `loadIBC.py`
    - This is a helper script for loading the IBC data, provided by Mohit Iyyer
  - `prelimDataExploration.ipynb`
    - This file is used for exploring and processing the *IBC* corpus
  - `treeUtil.py`
    - This is a helper library for parsing and manipulating the custom data format of the IBC data, provided by Mohit Iyyer
    
The analysis and conclusions of our experiments can be found in the [final report](https://github.com/ahsenq/w266_final_project/blob/master/PoliticalBias_finalReport/Political%20Bias%20Detection%20with%20BERT.pdf).
