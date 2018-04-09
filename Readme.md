# Arabic Text Categorization

Based on  
TALLA PAPER


## Starting Project

* Make sure you have installed pip (Python 3)
    ```text
    How to install pip
    ```

* Make sure you have NLTK (Natural Language Tool Kit) installed  (Python 3)
    ```text
    pip install nltk
    ```
  
## Project layout 

```text
.  
├── docs                    <- All documentation about project
│   ├── reports             <- Reports for current project advancement 
│   ├── references          <- All references papers, links related to this project goes here   
│   └── sphinx              <- Automaticaly genereated API documentation form stringdocs in code
│
├── lib                     <- All project's source code goes here
│   ├── data-generation     <- Code for data generation if needed 
│   └── preprocessing       <- Code for data preprocessing 
│ 
├── models                  <- Contains code to train, test and run models 
│   ├── dumps               <- trained models file
│   └── scripts             <- script to run models 
│ 
├── Readme.md               <- Contains current project info
├── requirements.txt        <- Packages and modules needed for the current project to run
└── tests                   <- Unit test for the code in lib/ 
    └── lib  
        ├── analysis  
        ├── data-generation   
        └── preprocessing
   
```
  
## Guide lines

### Data

* Symlink to your Raw data
    ```text
        user@host:~$ ln -s /path/to/your/raw/data . 
    ```

* Data location must follow this structure:

```
data  
├── raw             <- Raw data
├── temp            <- transformed data stored temporarily if needed 
└── preprocessed    <- preprocessed data to run in a model
```
#### Data is immutable  
* Treat the data/raw (and its format) as immutable. Don't ever edit your raw data, especially not manually, and 
especially not in Excel.
* Don't overwrite your raw data. Don't save multiple versions of the raw data.
* The code you write should move the raw data through a pipeline to your final analysis.
* You shouldn't have to run all of the steps every time you want to make a new figure, 
but anyone should be able to reproduce the final products with only the code in lib/ and the data in data/raw.