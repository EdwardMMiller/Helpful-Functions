# Helpful-Functions
A couple of helpful functions I've made 

basic_text_preprocessor(text_df, col_name):

There are almost assuredly lots of superior functions to this one with lots less code, and that run far more efficiently than mine does.
However, I am still new to Python and Machine Learning and until I make a better one or find one that fits my needs better,
I've been re-using this quite frequently, and so far it hasn't failed me. This function is also needed in the function below

Model_Stacking_String_Matrix(df, col_name, X, Y, **params):

While I'm still quite new to Python and also Machine Learning, I've used this custom function
more than once for binary classification with multiple data types in a dataset. This function was useful for when
I've needed to do model stacking and run Logistic Regression on a column
of string data to get a column of prediction probabilities, which would then be put into a
second model to get final predictions for a test data set. This function is specifically something 
that would be used near the end of a project once the best parameters have already been found,
and it has been determined that Logistic Regression
is the best choice of model for the string data. However, one could easily modify this and add a model type
as one of the parameters to the function, so that another type of model can be used besides Logistic Regression
and I may very well do this myself in the future, however, at the time, this function does what
I need it to do quite well, and it returns a dataframe that replaces a column of string data with a column of 
prediction probabilities, and so far, it has worked seamlessly for me for my assignements.

NOTE: It is important that the training string column and training target column used for X and Y resepectively 
in this function are the same exact columns that were used in training the model up, otherwise
there will be incorrect prediction probabilities due to the model not being fit on the training data. 
If there are missing values or other issues, those
can be added as an extra step in the previous function, or addressed before using this function.

ALSO - The code for these two functions includes two small dummy test dataframes solely for quick debugging of the functions. These are certainly
not large enough for any meaningful model predictions, they only serve to ensure that the formatting and functionalty work, and nothing more.


## Added 9-13-23

After a little break from Python, I decided to get back into it, and add some basic functions just for practice. None of the functions
used import any packages and only use the basic Python library in Python 3

string_to_integer_list(string)

The function extracts only numbers from a string inputted by the user containing letters, special characters, and digits, and returns a list of numbers. 

list_updater(num_list)

The function takes a list of numbers and doubles any number found twice in the list and returns a list with the numbers doubled.
If no doubles are found, it just returns the same list.
