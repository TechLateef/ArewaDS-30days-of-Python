# Setting up Virtual Environments

# To start with project, it would be better to have a virtual environment. Virtual environment can help us to create an isolated or separate environment. This will help us to avoid conflicts in dependencies across projects. If you write pip freeze on your terminal you will see all the installed packages on your computer. If we use virtualenv, we will access only packages which are specific for that project. Open your terminal and install virtualenv

# asabeneh@Asabeneh:~$ pip install virtualenv

# Inside the 30DaysOfPython folder create a flask_project folder.

# After installing the virtualenv package go to your project folder and create a virtual env by writing:

# For Mac/Linux:

# asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project\$ virtualenv venv

# For Windows:

# C:\Users\User\Documents\30DaysOfPython\flask_project>python -m venv venv


# Let us activate the virtual environment by writing the following command at our project folder.

# For Mac/Linux:

# asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ source venv/bin/activate

# Activation of the virtual environment in Windows may very on Windows Power shell and git bash.

# For Windows Power Shell:

# C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\activate

# For Windows Git bash:

# C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\. activate


# Now, lets check the available packages in this project by writing pip freeze. You will not see any packages.

# We are going to do a small flask project so let us install flask package to this project.

# (venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip install Flask


# When you finish you should dactivate active project using deactivate.