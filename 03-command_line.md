# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

>>
 1. ```pwd``` 
     + print working directory
     + basically telling you where you are (which directory you're in)
 2. ```touch <new-file>```
     + Create an empty file.
 3. ***ls options***
     + ```ls -a``` Views hidden files. Hidden files are files that starts with a ```.```
     + ```ls -l``` Lists file in the long format. This includes rwx permissions, owner, owner group, file size, date of last modification.
     + ```ls -t``` Lists file and directories based on the time they were last modified.
 4. ```cp```
     + The last argument is the destination.
     + The rest of the arguments are the files to be copied to the destination.
     + Remember that cp works also with ```*``` - select all or partial files in a directory.
     + note: the same tricks also work for ```mv```
 5. ```rm -r```
     + recursively remove. This means, we can delete a directory and its child directories.
 6. ```>```
     + redirection
     + it redirects the output of the LHS as input to the RHS
     + it *overwrites* all of the original content of the RHS.
 7. ```>>```
     + Like the single ```>``` above, it redirects. The difference is, ```>>``` appends the content instead of overwriting it.
 8. ```<```
     + Take the file on the RHS as input to the LHS.
     + Difference from just the opposite of ```>```, you don't need to "cat" the file on the RHS, it simple takes the file contents as input to the LHS
 9.

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

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE
