<<<<<<< HEAD
# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.
=======
# Pysimplero
API client for the Simplero api using the python requests module. 

This is a simple example package. For now you can get lists and add subscribers using this client. The aim of this module is to make it effortless to use python to interact with your Simplero account and setup integrations or automations with other services.

Feel free to contribute to the development of this package! Any help in the form of code review, refactoring, bug fixes, bug reports or feature request will be greatly appreciated!

You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
or Emacs orgmode to write your content.
## Getting started
First things first, start with creating a python virtual environment to install dependencies for the project. 

    
    python3 -m venv .venv
    

After creating the virtual environment go ahead and activate it using source .venv/bin/activate. Or if you are working in emacs orgmode you can activate it and create a session to work in using this snippet of emacs-lisp code:

    (pyvenv-activate ".venv")

And the we upgrade pip in our venv

    # source .venv/bin/activate
    pip install --upgrade pip

### Installing Requests

Requests installation depends on type of operating system on eis using, the basic command anywhere would be to open a command
terminal and run,

    pip install requests


<a id="orgbdb481c"></a>

#### Making a Request

Python requests module has several built-in methods to make Http requests to specified URI using GET, POST, PUT, PATCH or HEAD
requests. A Http request is meant to either retrieve data from a specified URI or to push data to a server. It works as a request-response
protocol between a client and a server. Let’s demonstrate how to make a GET request to an endpoint.
GET method is used to retrieve information from the given server using a given URI. The GET method sends the encoded user information.
## Using Pysimplero
After installing the requests module in your venv go ahead and create a secrets.py file in the src/pysimplero folder with your api_key and user_agent info.

Then you can run python pysimplero to get a list of your mailinglist id's. 
>>>>>>> f53edf2 (update readme.md)
