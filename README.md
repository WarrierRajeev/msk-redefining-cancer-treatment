# msk-redefining-cancer-treatment

## Installation

- Clone/Download the repo
- Download the data from https://www.kaggle.com/c/msk-redefining-cancer-treatment/data
- Extract the contents from their zips and place them in the data folder
- The description of the files and the method is described below: 

### In this repo, the cancer-EDA does exploratory data analysis on the dataset, cancer-model is the actual model classification and the last ipynb is the cancer-API_client which actually just checks whether the API is up and running.

#### The dataset given was not well distributed and that affected the accuracy of the model. Initially, I went for SVM with bag of words and then with TfIdf but in the stage 1 dataset, it gave poor results. So after looking around testing how well models are doing on a confusion matrix, I decided to finally go with XGBoost which performed the best with word2vec. It gave me 15th rank in the private Leaderboard. To improve, I guess using doc2vec along with some intense feature engineering would result in something better. The data can be downloaded from kaggle as github would not allow over 25 mb files to be uploaded. The submissions.csv is submission for the stage 1 test data or just test_var and test_text. The submissions2.csv is the second and actually accepted csv file. The pickles were turning out to be huge so I deleted them from the repo.

#### For the API I would have liked to make it more flashy but I was quite short on time. What I would like to do is to use tornado instead of flask so that multiple queries simultaneously are actually allowed. This wonderful talk, https://www.youtube.com/watch?v=n8j-ResxY78 made me want to change the practice by using tornado.