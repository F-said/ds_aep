# Data Analytics AREP Assessment

Welcome to the Data Analytics Alumni Re-Engagement Program Assessment!

This assessment is designed to test your skills in data manipulation. It includes various coding tasks that will challenge your ability to write code in Python, manipulate dataframes in pandas, and interpret statistical concepts.

To get started, complete the setup steps outlined in the section titled "Installation" and then proceed to the challenges listed in "Assessment." The entire assessment should take about 4 hours to complete. Examples are provided in each coding challenge, and helpful resources are listed in the section titled "FAQ."

Each Jupyter notebook in this repository entails a coding challenge for you to solve. For each notebook, there will be a code block that you can use to test your solution. Just be sure to run your solution block before running the test block. 

Feel free to use documentation and other learning resources. However, resist the urge to copy solutions that you may find online. Remember, the purpose of this assessment is to get a gauge on your fundamentals. If you are unable to implement a fully functioning solution, give it your best shot and leave comments on your thought process.

Imperfect human solutions entail more creativity and knowledge than a perfect LLM solution.

Good luck. 

## Installation

To get started with this repository, follow along with the steps below:

1. [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) this repository to your GitHub profile.

2. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) your forked repository to your computer. You should clone your repository into an easily accessible location (such as your Desktop) using your terminal (MacOS) or command prompt (Windows).

3. Install the required Python packages from the `requirements.txt` file using [pip](https://note.nkmk.me/en/python-pip-install-requirements/). **Note:** If you have pandas already installed on your computer, you can safely skip this step.

4. Begin the assessment!

## Assessment

### Max Profits

You are given a list of stock prices, where the stock's price on the `ith` day is stored as the `ith` element of the prices list.

Use base Python to solve this challenge in the `max_profits.ipynb` Jupyter notebook. 

### Recyclable and Low Fat Products

Write a solution to find the id's of products that are both low fat and recyclable.

Use pandas to create a boolean filter to select the products that satisfy these two conditions in the `max_profits.ipynb` Jupyter notebook. 

### Delete Duplicate Emails

Return the result table in any order. Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

Use pandas to drop duplicate emails from your dataframe in the `delete_dupes.ipynb` Jupyter notebook.

### Modify Columns

A company intends to give its employees a pay rise.

Write a solution to modify the salary column by increasing salary by 100%

Use pandas to modify the `salary` column to reflect a 100% raise for each employee in the `modify_column.ipynb` Jupyter notebook.

### Top Travelers

Write a solution to report the distance traveled by each user.

Use pandas to join, group by, and sort your dataframe in the `top_travelers.ipynb` Jupyter notebook.

### Find Users with Valid E-Mails

Write a solution to find the users who have valid emails.

Use pandas and [regex](https://regex101.com/) to filter out all invalid emails in the `valid_emails.ipynb` Jupyter notebook.

## FAQ

1. **I'm stuck on one problem, what should I do?**

If you've exhausted all possible resources (such as documentation & googling) and a problem has taken you longer than 40 minutes to solve, we recommend that you move on to the next problem, and attempt to solve the original problem at a later time. 

Remember, fresh eyes will always help! If you've been working for too long, a break might be in your best interest.

2. **Which documentation should I use?**

While googling is always your best bet, the next best resources that you should consult include:

* [The Pandas API](https://pandas.pydata.org/docs/reference/index.html)
* [RegexOne](https://regexone.com/)
* [GeeksforGeeks](https://www.geeksforgeeks.org/pandas-tutorial/)
* [RealPython](https://realpython.com/pandas-dataframe/)

3. **Will I get partial credit?**

If your solution is partially correct, yes! 

4. **How can I tell if my solution is correct?**

Each Jupyter notebook entails a testing block. If the code within the testing block evaluates to True, your solution is correct.

## Submission

To submit your solution, send over a link to your forked repository. The only files that should be changed are the Jupyter notebooks within this repository.