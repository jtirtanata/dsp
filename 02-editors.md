# Choose and learn your editor(s)


Computing's interface is text. To work effectively, you need to be fluent with this interface.


### Typing

It may sound silly, but [make sure](http://www.typingtest.com/) you know how to type. You should be comfortable typing with perfect accuracy at 60 words per minute, at least. If you currently can't, practice until you can.

A lot of your work will be done in a text editor. You have to know how to use your editor. Any editor will work, but knowing a powerful editor well will make you faster, more comfortable, and more effective.

---

### Terminal Editor

Sometimes you will need to use a non-graphical text editor. This means an editor that will run entirely inside a terminal window, without spawning a new window, entirely without mouse input.

Make sure that you know at least one of these well enough to do basic editing in a terminal:

 * Emacs
 * vim
 * nano

You should know at least enough vim to be able to get out of it, because it is the default on many systems and you might find yourself in it even if you didn't mean to be.

If you intend to use a graphical editor that doesn't run in a terminal, nano might be a good choice for you because it is very simple.

Both Emacs and vim have built-in interactive tutorials that you can try.



---

###Graphical Editor

You will probably spend most of your time with access to a graphical interface, where you have more choices in editors and integrated development environments.

Popular editors and IDEs include:

 * Emacs
 * vim
 * Sublime
 * Atom
 * Spyder
 * PyCharm
 * [Rodeo](http://blog.yhat.com/posts/introducing-rodeo.html)

If you choose Emacs or vim, you will have essentially the same editor experience across graphical and non-graphical environments, which is nice. It's also nice to be able to work without ever having to use a mouse. Emacs and vim have somewhat steep learning curves, but they give you the ability to customize your environment quite a lot to make it exactly what you want.

Sublime is probably the most popular editor for new coders. You can set it up to integrate with Python fairly well. Atom is pretty similar to Sublime but has an interesting open architecture and is developed by folks at GitHub.

Spyder and PyCharm are IDEs for Python. They try to give you a fully configured setup out of the box.

We will also use Jupyter (IPython) notebooks, but this does not remove the need for proficiency in an editor or IDE.

---

###Q1. Terminal Editor

What terminal editor will you use? How did you make your decision?

>>I will use **vim**. I have used it for a long time, it's awesome, I am familiar with a lot of the shortcuts and can code in it fairly quickly.
--

###Q2. Graphical Editor

What graphical editor will you use? How did you make your decision? What are some interesting features of your editor? What are some useful keyboard shortcuts for your editor? How do you customize your editor?

>>I will use Atom. I think it looks great, there are plenty of plugins to choose from, and the short cuts are also easy to use. It is also created by github, which means that it has some cool features that are uber github! (i.e. a markdown editor, for one) Some of my favorite features are the multiple panes, and the indexing of your files and folders to allow search!

I also found a couple of useful keyboard shortcuts:
 1. **Multiple cursors**
    Hold ```cmd``` and click in every place you want the cursor in.
 2. **Moving the line up and down**
    ```cmd+ctrl+up``` or ```cmd+ctrl+down``` to move the line your cursor is currently on the the line above or under it.
 3. **Duplicating a line**
    ```cmd+shift+d``` to duplicate the line your cursor is currently on.
 4. **Finding and selecting a matching word**
    ```cmd+d``` to select the next matching word.
    ```cmd+u``` to unselect the next matching word.
    ```ctrl+cmd+g``` to select all matching words.
 5. **Live preview markdown**
    ```ctrl+shift+m``` to toggle markdown preview.
 6. **Search tool**
    ```cmd+t``` to open the search box.
 7. **Tree view**
    ```cmd+\``` to toggle the tree view. Hide it to have more space when you're coding, and quickly open it again to navigate to another file!
 8.



How I'm customizing my atom editor:
 1. Creating the shortcut ```cmd+i``` for fixing my identations.
 2. Installed atom material theme
 3. Installed the color-picker plugin. ```cmd+shift+c``` will open the color picker and give me the RGB values
 4. Installed docblockr plugin that will detect the details of a function and autofill a corresponding comment.
 5. Installed linter-python. It will detect, visualize, and notify your python errors.
 6. Installed autocomplete-python. It can autocomplete packages, variables, methods, functions and its arguments.
