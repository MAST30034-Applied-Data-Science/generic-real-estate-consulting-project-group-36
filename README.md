# Generic Real Estate Consulting Project

**Research Goal:** Predict rental prices for both residential properties and apartments throughout Victoria,Australia

**Timeline:** The timeline for the research area is 01/09/2022-08/10/2022.

To run the pipeline, please visit the `scripts` directory and run the files in order:
1. `01_get_facility.ipynb`: This downloads the external data such as fitness and parks into the `data/curated` director.
2. `02_income_clean.ipynb`: This notebook details income data cleaning steps and outputs it to the `data/curated` directory.
3. `03_hosptial_clean.ipynb`: This notebook details hosptial data cleaning steps and outputs it to the `data/curated` directory.
4. `04_domain_cleaned.ipynb`: This notebook details domain data cleaning steps and outputs it to the `data/curated` directory.
5. `05_geo_code.ipynb`: This notebook calculates the longitudes and latitudes of external data and outputs it to the `data/curated` directory.
6. `06_geo_code_cleaned.ipynb`: This notebook details the coordinates of external data cleaning steps and outputs it to the `data/curated` directory.
7. `07_shopping_malls_scrape.ipynb`: This notebook uses web scraping to collect the data of shopping malls  and outputs it to the `data/raw` directory.
8. `08_cloest_distance.ipynb`: This notebook calculates the cloest distance of external data such as parks and train stations of each apartment and outputs it to the `data/curated` directory.
9. `09_Data preprocessing.ipynb`: This notebook details the useful data of population cleaning steps and outputs it to the `data/curated` directory.
10. `10_pop_pred.ipynb`: This notebook details the prediction from 2021-2025 of population and outputs it to the `data/curated` directory.
11. `11_income&price_pred.ipynb`: This notebook details the prediction from 2021-2025 of income as well as house price and outputs it to the `data/curated` directory.
12. `12_merge_datasets.ipynb`: This notebook merges all the useful columns and outputs it to the `data/curated` directory.
13. `13_remove_outliers.ipynb`: This notebook removes all the outliers of the dataset saved above and outputs it to the `data/curated` directory.
14. `14_readme.txt`: This notebook instructs the reader to run models under the `models` directory.
15. `15_House_Model_fitting-Copy1.ipynb`: This notebook runs all the models which predict the house price and outputs the plots to the `plots` directory.
16. `16_Apart_Model_fitting.ipynb`: This notebook runs all the models which predict the apart price and outputs the plots to the `plots` directory.
17. `17_xgboost.ipynb`: This notebook runs the best performance model and outputs it to the `data/curated` directory.
18. `18_geomap.ipynb`: This notebook draws the map visualization of house and apartment price VS suburbs and outputs the maps to the `plots` directory.
19. `19_growth_rate.ipynb`: This notebooks calculated the top 10 price growth rate suburbs and outputs the plots to the `plots` directory.
20. `20_affordbility.ipynb`: This notebooks calculated the top 10 affordable suburbs and outputs the plots to the `plots` directory and the top 10 livable suburbs and outputs the plots to the `plots` directory.
21. `Summary_notebook.ipynb`: This notebooks covered the prediction analysis and answers to 3 major questions.
