# Naïve Bayes and SGD
Using Naive Bayes and SGD ML algorithms to predict if a new car for sale will decrease in price.

## The Data Set

| Vin           | Make          | Model     | Trim      | Color    | Dealership   | Location      | Price Change* |
|---------------|---------------| ----------|-----------|----------|--------------|---------------|---------------|
| 1X234...      | Volkswagen    | Jetta     | SE        | Red      | Brady        | VW of Boston  | 1000          |
| 4C353...      | BMW           | x5        | XT        | Green    | Elway        | BMW of Denver | 0             |
| 9E434...      | Volvo         | s60       | SV-600    | Blue     | Rodgers      | Volvo of GB   | 52            |

*price change must be > $100 to be considered to have changed

## Data Set Size
|                  |           |
|------------------|----------:|
| Total            | 13311 cars|
| # price change   | 6067 cars |
| # no price change| 7244 cars |


## Training Corpus 

["volkswagen jetta se red brady vw of boston", 
"bmw x5 xt green elway bmw of denver"]

## Test Corpus
["volvo s60 sv-600 blue rogers volvo of gb"]

## Training Target
[1,0]

## Test Target
[0]

## Results
|           |  precision   |  recall  | f1-score | support |
|-----------|--------------|----------|----------|---------|
|  no_change|       0.88   |   0.80   |   0.84   |   2197  |
|     change|       0.79   |   0.87   |   0.83   |   1866  |
|avg / total|       0.84   |   0.83   |   0.83   |   4063  |

Overall acurracy on test set: 83.2%
