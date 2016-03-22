#Cranky Blogger CLI

This script interacts with the Google Blogger API V3. Its purpose is to enable
command line blog posting. Its functions are as follows

-f "Filename"       # is required
--publish           # sets the post to publish immediatly, the default is draft
-t "My topic"       # Sets the topic and is required when --publish is present
-l "label1, label2" # to set labels

Before you can run the program you will need to login into the google API
console setup an app and download a blogger key. Put the .json file in the same
directory as the script.

When you first run the program a web browser will launch and you will give the
app permission to access your blogger account.

Don't forget to edit the following configurable variables

labels # defaults are used when no labels are given on CLI
blogId # The id of your blog
title  # The default title to use if one is not specified

#You're post should be a plain text html file. Common tags include
-<br />Put two line breaks between paragraphs
-<pre>Good for multi-line code snippets</pre>
-<code>Single line code snippet</code>
-<a href="linkurl">My cool link</a>

#TIPS
-You can use html2text to view the post in the command line or simply fire it up
in a browser to see if formating is correct.
-Don't forget to use the spellcheck in your editor :)
-Please enjoy and I welcome public contributions!

#TODO
Implement editing and deleting of blog posts


#LICENSE
Do what ever you want with it. No WARRANTY. If you share a copy with someone
else, it must be under the same license.
