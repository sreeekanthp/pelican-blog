Title: Pelican with github pages
Date: 2014-05-01 10:00
Category: Python
Tags: python, pelican
Author: Sreekanth
Summary: Getting started with pelican and github pages

Pelican is a static site generator written in python which allows you to write your content directly using [reStructuredText](http://docutils.sourceforge.net/rst.html) or [Markdown](http://daringfireball.net/projects/markdown/). In this blog post, we will discuss how to create and host a static site using pelican and github pages.

**Installation**

Lets wrap all our installations inside a separate virtual environment using python virtual environment wrapper. 

[Install python virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)

Create a new virtual environment for our project:

    $ mkvirtualenv pelican-blog
    $ workon pelican-blog

Run pelican installation:

    $ pip install pelican

[Checkout more installation options for pelican](http://docs.getpelican.com/en/3.1.1/getting_started.html#installing-pelican)

Run markdown installation:

    $ pip install Markdown

You can also use reStructuredText  for writing your content.


**Quickstart your blog**

Now we have finished all our installations and lets create a skeleton for our site using the pelican *quickstart* command. This will ask you few questions and will pre-populate the settings data as per your answers. These settings can be changed at any point of time.

    $ pelican-quickstart

Please see how I have answered the quickstart questions below:

    Welcome to pelican-quickstart v3.4.0.
    
    This script will help you create a new Pelican-based website.
    
    Please answer the following questions so this script can generate the files needed by Pelican.
    
    > Where do you want to create your new web site? [.]
    > What will be the title of this web site? Sreekanth's Blog 
    > Who will be the author of this web site? Sreekanth
    > What will be the default language of this web site? [en]  
    > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n)  
    > What is your URL prefix? (see above example; no trailing slash) http://sreekanthkaralmanna.github.io  
    > Do you want to enable article pagination? (Y/n)  How many articles per page do you want? [10]  
    > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)  
    > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)  
    > Do you want to upload your website using FTP? (y/N)  Do you want to upload your website using SSH? (y/N)  
    > Do you want to upload your website using Dropbox? (y/N)  
    > Do you want to upload your website using S3? (y/N)
    > Do you want to upload your website using Rackspace Cloud Files? (y/N)  
    > Do you want to upload your website using GitHub Pages? (y/N)  
    Done. Your new project is available at /home/sreekanth/Documents

Once you finish with all those questions, you will be having a directory structure as follows:

    yourproject/
    ├── content
    │   └── (pages)
    ├── output
    ├── develop_server.sh
    ├── fabfile.py
    ├── Makefile
    ├── pelicanconf.py       # Main settings file
    └── publishconf.py       # Settings to use when ready to publish 

**Customise your theme**

Pelican comes with  a default theme for every sites generated. You can use a variety of other themes to beautify your site.  I have used [flasky](https://github.com/fjavieralba/flasky) theme for creating this site.
[Pelican themes](https://github.com/getpelican/pelican-themes)

In order to include your desired theme, clone your preferred theme and save the theme to a theme directory inside your project folder. Now tell pelican that it has to use  this particular theme to generate html for your site. In `pelicanconfig.py`, add the following:

    THEME = "themes/flasky"

Also make sure to change your pelican settings as per the settinfgs given in the theme documentations(if any)

**Writing blog content**

We are done with configuring our pelican site, now let's start writing our blog contents. Below given is a sample markdown file. 

    Title: Pelican Test Blog 
    Date: 2014-05-01 10:00 
    Category: Python 
    Tags: python  
    Author: Sreekanth  
    Summary: Pelican blog for testing.
    
    A Pelican blog for testing


**Generate html files and run your site**

We are all done to test our site locally

The following command will create the output folder for your site and serves your site locally at http://localhost:8000.

    $ make devserver

To stop the localhost server, run the following command:

    $ ./devserver stop

**Publish your blog using Github pages**

For hosting your blog using github pages, create a repository named *username*.github.io and this will be the remote repository for your site. Contents of your output directory needs to be stored in this repository.

After creating the github repository, push your output files to the remote repository. Follow the steps given below for doing the same.

    $ cd output
    $ git init
    $ git remote add origin https://github.com/username/username.github.io.git
    $ git add --all
    $ git commit -m "initial commit"
    $ git push origin master

In order to backup your content Markdown files, configuration files, and theme files, it's good to initialise your main site directory with a different git repository.

We are done with that too. Checkout username.github.com to see your site running properly.

