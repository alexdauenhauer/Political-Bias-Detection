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
    - //TBD
  - `convote.ipynb`
    - //TBD
  - `loadIBC.py`
    - //TBD
  - `prelimDataExploration.ipynb`
    - //TBD
  - `treeUtil.py`
    - //TBD
    
The analysis and conclusions of our experiments can be found in the [final report](https://github.com/ahsenq/w266_final_project/blob/master/PoliticalBias_finalReport/Political%20Bias%20Detection%20with%20BERT.pdf).
