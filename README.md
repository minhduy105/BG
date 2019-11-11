This project is for the Berkshire Grey Coding Problem:

1. Write a python script to recurse a given directory location and return a list of files whose names match a regex (or maybe just whose size is > than some number)

The code only using the regex "*" and we only have 2 cases: at the begining of the search "*txt" or at the end of the search "abc*". This code assumes the files will consist of only letters and numbers. The search algorithm is case insensitive. 

+ The test_set.txt is for the users to input the search pharse. 

+ The folder Files is the folder that the algorithm will search on. The users can add or delete any files. 

+ The FileSearch.py has the search algorithm

+ The main.py has the main function to run the code

2. Write unit tests for the above.  Demonstrate your code coverage and justify it (i.e. why is this good enough)

I tested the two extreme cases, which are the first file and the last file in the folder. Then, I tested a few random cases for the files inside the folder. I included both letter and number cases in my test set. Additionally, I also included 2 searche cases.


3. Demonstrate execution time.  How might this be improved?

The time is between O(n) and O(log(n)):

The reason is that when the "*" is at the end of the search phrase (abc*), the name list is sorted and I can use binary search to get the results. The execution time would be O(log(n))
When the "*" is at the beginning of the search phrase (*.txt), the name list in the folder is not sorted backward. So, I just have to do the iterative search method. The execution time would be O(n).

