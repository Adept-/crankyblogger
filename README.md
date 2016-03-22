#Cranky Blogger CLI

This script interacts with the Google Blogger API V3. Its purpose is to enable
command line blog posting. Its functions are as follows

1. -f "Filename"        is required
2. --publish            sets the post to publish immediatly, the default is draft
3. -t "My topic"        Sets the topic and is required when --publish is present
4. -l "label1, label2"  to set labels

Before you can run the program you will need to login into the google API
console setup an app and download a blogger key. Put the .json file in the same
directory as the script.

When you first run the program a web browser will launch and you will give the
app permission to access your blogger account.

Don't forget to edit the following configurable variables

1. labels  defaults are used when no labels are given on CLI
2. blogId  The id of your blog
3. title   The default title to use if one is not specified

#TIPS
1. You can use html2text to view the post in the command line 
2. or simply fire it up in a browser to see if formating is correct.
3. Don't forget to use the spellcheck in your editor :)
4. Your post should be a plain html file
5. Please enjoy and I welcome public contributions!

#TODO
Implement editing and deleting of blog posts


#LICENSE
Do what ever you want with it. No WARRANTY. If you share a copy with someone
else, it must be under the same license.
