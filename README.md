# LEGO-sets
## Introduction
The project is a personal project out of personal interest. It uses original data from rebrickable.com and crawls data from brickset.com. It creates visualizations to explore the historical evolution of LEGO sets and recommends sets that a user can build from the currently owned sets. It can be quite fun for those who have grown up with Lego and are still playing with the bricks. 

## Problems addressed
1. Pricing strategy of sets
2. Rating of sets
3. Other characteristics of sets: yearly release of sets, sets customization strategy
4. Recommendation of sets

## Tools used
1. Python: crawl data, data cleaning and preprocessing, use plotly to create interactive and highly customized charts
2. WinDesign: plot the conceptual entity-relationship schema and the logical snowflake schema
3. Tableau: Data visualization

## Files
#### Crawl data part
See code in [LEGO_scraper.py](https://github.com/twinklenoisland/LEGO-sets/blob/master/LEGO_scraper.py)
All the output raw data from web scraper is store in Brickset

#### Data preprocessing
Code for data cleaning process: [LEGO database clean.ipynb](https://github.com/twinklenoisland/LEGO-sets/blob/master/LEGO%20database%20clean.ipynb),[preprocess_merge.ipynb](https://github.com/twinklenoisland/LEGO-sets/blob/master/preprocess_merge.ipynb),[price.ipynb](https://github.com/twinklenoisland/LEGO-sets/blob/master/price.ipynb)

#### Data visualization
Most of data visualization are designed in Tableau, but for some parts that are hard to customize in Tableau, I used Python Plotly to do the job. See code in [Visual.ipynb](https://github.com/twinklenoisland/LEGO-sets/blob/master/Visual.ipynb).

#### Recommendation of sets
See code in [recommendation.ipynb](https://github.com/twinklenoisland/LEGO-sets/blob/master/recommendation.ipynb)

## Reports
See pre.pptx and Report.pdf

