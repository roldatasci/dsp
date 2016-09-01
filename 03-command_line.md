# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > Command                | Result
> > ---------------------- | ------
> > pwd | print working directory
> > man command | access the 'manual'/documentation (use 'q' to exit)
> > rm file1 file2 | remove multiple files
> > pushd new_dir | 'push' current directory to a list, then go to new_dir
> > popd | 'pop' up the last saved directory location and go there
> > cp file1 file2 | 'copy' contents of file1 to file2
> > cp file new_path | 'copy' file to a new directory (new_path) without changing original file
> > cp -r dir1 dir2 | 'copy' 'recursively' all contents of dir1 to dir2
> > cp -r . ../new_dir | 'copy' 'recursively' all contents of current working directory to a new directory one level up 
> > mv file1 file2 | rename file1 as file2 ('move' contents of file1 to file2)
> > mv dir1 dir2 | rename dir1 as dir2
> > mv file dir | move file to dir
> > less file	| page through a file ('q' to exit)
> > cat file.ext | print whole file ('q' to exit)
> > cat file1 file2 | join both files and print ('q' to exit)
> > find startdir pattern | finds in starting directory files that match pattern 
> > grep -i pattern file | case 'insensitve' search for string pattern in file
> > clear | 'clear' all output in terminal/console

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`


> > Command | Result
> > ------- | ------
> > ls | list contents of current directory
> > ls -a | list 'all' contents of working directory (including hidden files)
> > ls -l | list in 'long format' contents of current directory
> > ls -lh | list in 'long format' with 'human readable' file sizes (B, M = MB, K = KB)
> > ls -lah | list in 'long format' 'all' contents, with 'human readable' file size
> > ls -t | list contents sorted by 'timestamp' (last modified)
> > ls -Glp | list in 'long format', with directories highighted and a'p'pended with '/'

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > Command | Result
> > ------- | ------
> > ls -o | list in 'long format', no gr'o'up names
> > ls -u | list contents sorted by time it was accessed
> > ls -1 | list contents in rows only (no multiple columns)
> > ls -R dirname | list subdi'R'ectories of dirname and their contents
> > ls -G1p | list in rows only (no multiple columns),  directories highlighted in blue,  and with a'p'pended with '/'

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` is a command that can take the output from one command and 'execute' it as an input 'argument' for the next command, where the two commands are separated by a pipe ('|'). This effectively facilitates the execution of a series of commands, each with their own inputs/arguments and outputs that are chained together, with `xargs` passing output from one as input to another.

> > A common use of `xargs` is to combine it with `find` and `grep`, though there are [other handy uses](http://javarevisited.blogspot.com/2012/06/10-xargs-command-example-in-linux-unix.html). `find` can return multiples files as output, each of which `grep` can use as its argument to search for a "pattern".

> > As a concrete example, suppose you need to search through all your python scripts for a Car class you have previously constructed.

`find . -name "*.py" | xargs grep "Car"`

> > The above series of commands will find all files in the current working directory (.) or below that are named with a .py extension (i.e. all python files). The result of this first query (to the left of the pipe '|') would be a collection of files that are then passed by `xargs` as input for the next query (to the right of the pipe '|') using `grep`. `grep` will go through each of those files to search for "Car" inside each file.
