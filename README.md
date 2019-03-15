# csc648-fa18-Team10

## Please do the following steps before completing Milestone 0.
1. Change the name of the repo from csc648-fa18-TeamNN. All that needs to chanage is the NN to your respective team number. Team numbers whos value is less than 10, please pad with a 0. Ex team 1 is Team01 team 11 is Team11. Please make sure to also remove the username from the repo as well.

1. PLEASE REMOVE THE USERNAME FROM THE REPO!!!

2. Add ALL members of your team to this repo. For it to count, they must ACCEPT the invite.

## Workflow
1. Create issue in GitHub (either created by yourself, or by others and then assigned to you).

2. ```git pull origin dev``` to pull code from the remote dev branch to your local dev branch so that you have the most up-to-date version of the code.

3. ```git checkout -b [your_branch_name] origin/dev``` to create a branch off of origin/dev and check out that new branch for development. Use this format to name your branch: milestone#/issue#, e.g. m2/issue1

4. Make changes in your feature branch, commit your code to save changes locally. Make sure you put your issue number in your final commit. One trick is that, if you add the keyword "fix" with your issue number in your commit message, GitHub will automatically close the issue for you when your branch is merged into master. e.g. ```git commit -am "fix #2: Added styling to home page"```

5. When you're ready to push, make a final test and screenshot your test result.

6. ```git push origin [your_branch_name]``` to push changes to GitHub.

7. It'll prompt you to make a pull request on GitHub to merge your feature branch to dev. So do that (add the issue # and your test screenshot to the pull request) and add someone who knows your code well to be the reviewer.

8. The reviewer will review the code (review the diffs or create a new branch in your local environment and pull the changes to test it out). If everything looks good, approve and assign the request back to the developer.

9. The developer merges his own code to dev and close the issue (if you used the trick mentioned in step 4, the issue should be automatically closed for you).

## How to Get Web Application Running Locally
1. Have Python 3.6 and PostgreSQL 9.4 installed on your local environment.

2. Run ```git clone https://github.com/CSC-648-SFSU/csc648-fa18-Team10.git``` to clone the repository to your local PC.

3. Run ```python3 -m venv venv``` in the csc648-fa18-Team10 directory to create a virtual environment called "venv" for Django application development.

4. Run ```source venv/bin/activate``` to enter virtual environment.

5. Run ```pip install -r requirements.txt``` to install the dependencies for this environment (Django is included).

6. Install PgAdmin or use psql to connect to your local database host and create a database with the name "onlinestore_db".

7. Run ```python manage.py migrate``` to create database tables according to the settings in team10_project/settings.py (if you make database changes for the onlinestore application, run ```python manage.py makemigrations onlinestore``` to create a migration and then run ```python manage.py migrate``` to update your sql database).

8. Run ```python manage.py runserver``` and enter your local IP address to your browser to see your web application.
