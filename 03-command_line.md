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
 4. ```cp ```
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
 9. `sort`
     + Takes the standard input and orders it alphabetically for the standard output.
 10. `grep`
     + Searches the files for lines that matches a pattern and returns the result to the standard output.
     + -i to be case insensitive
     + -R searches all of the files in the directory and outputs filenames and lines containing matched results
     + -Rl like above but only filenames.
 11. `sed`
     + Modifies standard input based on an expression before displaying it as output data.

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

>>
 - `ls` List files in the current directory.
 - `ls -a` Adds hidden files to the regular ls.
 - `ls -l` List files in long format. This includes rwx permissions, owner, owner group, file size, date of last modification
 - `ls -lh` Lists files in long format but uses unit suffixes (i.e Bytes -> B) to reduce number of digits.
 - `ls -lah` Lists files, including hidden ones, in the long format with unit suffixes.
 - `ls -t` List files ordered by time modified.
 - `ls -Glp` List files in colorized and long format. Also adds a slash after each filename if that file is a directory.


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> >
- `ls -S` Sort the files by size.
- `ls -u` Sort by time of last access instead of last modification.
- `ls -U` Sort by time of creation instead of last modification.
- `ls -r` Reverse the order of the sort.
- `ls -R` Recursively list subdirectories encountered.

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > It divides the list from standard input into a sublist that we want to do some operation on. It is used in conjunction with find and grep.  
example: `find /tmp -name "*.tmp" | xargs rm`  
This removes all of the files that ends in temp in the tmp/ directory.
