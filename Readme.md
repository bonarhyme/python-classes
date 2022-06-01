# Steps to create a virtual environment, install packages, install and run django on windows using vscode

1. create a virtual environment in a folder: `virtualenv theEnvFolderName`
2. activate virtual environment: `theEnvFolderName\Scripts\activate`
3. install a package e.g `pip install django`: `pip install package_name`
4. deactivate virtual environment: `deactivate`
5. create django project in the xerst folder: `django-admin startproject xerst ./`
6. migrate project: `python manage.py migrate`
7. run development server: `python manage.py runserver`
