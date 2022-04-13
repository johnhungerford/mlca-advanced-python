## Using this repository on your computer

### 1. Clone
To clone this repository (create a copy of it on your computer):

1. Click the green drop-down button on the top right-hand side of the screen
2. Select the tab labeled `HTTPS`
3. Click the two boxes to the right of the url (this will copy the url to your clipboard)
4. Find or create a directory on your computer where the repository will go (note that when the repository is cloned, it will create 
   another directory)
5. In your terminal, navigate to the directory and enter the following command:

```bash
git clone [copied-url]
```

This will create a new directory named `mlca-advanced-python` in your current working directory with the latest version of this 
repository in the "master" branch.

### 2. Set up environment

It is a good practice to use a "virtual environment" for Python development to keep your library 
dependencies separate for each project you may be working on.

This repository comes with scripts that will set this up for you. 

*IMPORTANT: Python files in this project will not execute properly without running these scripts first.*

#### OSX or Linux

1. Open a terminal window at the root directory of this project
2. Run the following command: `source scripts/set_env.sh`

#### Windows

1. Open a terminal window at the root directory of this project
2. Run the following command: `scripts\set_env.bat`

## Challenge Problems

The `algorithms` directory contains challenge problems. Your task will be to *implement a single function 
with a precisely-defined expected behavior*. This function will be at the top of each file. Its expected 
behavior will be described in its docstring, and its body will be `pass`. Your task is to replace that 
with a correct implementation, using the given function parameters.

To test your implementation, you need only to run:

```bash
python [path_to_file]
```

It will run a series of tests using different input values, and will display the results. To successfully 
meet the challenge, all tests should be *green*.

Note that passing tests display the execution time of your implementation. Even if you pass all the tests, 
you can optionally challenge yourself to reduce your execution time.
