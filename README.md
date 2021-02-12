# Loan repayment behaviour prediction

**Objective**: case study of a machine learning model that can be used to predict loan repayment behaviour of currently excluded customers of formal financial services. 
Traditional metrics for credit scoring were excluded to create this model (e.g. credit card repayment, previous bank loans).

**Data source**: [Kaggle Home Credit Dataset](https://www.kaggle.com/c/home-credit-default-risk)

# Notebook structure
## I - Exploratory Data Analysis** which explores the dataset in preparation of the cleaning and modelling


## II - Basic data cleaning & modelling
Data cleaning and modelling which can quickly be deployed and used to develop a benchmark predition model

** Notebooks:**
- Data cleaning notebook
- Modelling notebook


## III - Advanced data cleaning & modelling
Showcase of more advanced techniques that can be applied to improve model performance. The notebook is meant to showcase some techniques, but may not necessarily apply to this project.

Examples of more advanced techniques:
- *IQR outlier removal* - Statistical method which removes outliers falling outside the Inter Quartile Range (IQR)
- *Missing data prediction* - Estimate missing values using machine learning algorithms
- 




** Notebooks:**
- Data cleaning notebook
- Modelling notebook






# Potential improvements

**I - Use a different method of feature selection** 
A combination of Regression and Random Forest mode was used to select the best performing features. More advanced techniques can be used (*e.g. Recursive feature selection*)

**II - Research based feature engineering**
Research on loan repayment could lead to new and improved features. This could be based supplemented based on interviews with loan repayment experts.

**III - Include more parameters as part of the Hyper Parameter Tuning process**
Because HPT is a resource intensive process, only a select amount of hyper parameters have been used. Expanding testing parameters will likely lead to improved model performance.

**IV - Include more or different algorithms**
As per HPT, testing algorithms is a resources intensive process. 

**V - Choose a different balancing method**
The majority of customers (91%) did not experience any repayment difficulties, creating an unbalanced dataset. Depending on the algorithm, this may lead to skewed results. For instance, if a model would predict that no customers experience payment difficulties, it would likely be correct 91% of the cases. While this is great model accuracy, this does not help in identifying customers with payment difficulties.

**VI - Optimise code**
Code can run a lot faster when optimised.


For this dataset I decided to balance the dataset using upsampling, but other resampling techniques can be used. For instance:
- Random under-sampling;
- Syntetic sampling - application of Machine Learning algorithms to artificially add to the dataset;
- undersampling (not recommended due to the relatively small size of the dataset).

Use unbalanced dataset vs artificially balanced
- Use a different method of feature selection (*e.g. correlation, Recursive feature selection*) 
- Include more or different algorithms
- Include more parameters as part of the Hyper Parameter Tuning process



# Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
                              generated with `pip freeze > requirements.txt`


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
