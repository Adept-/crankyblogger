#!/usr/bin/env python
import json, webbrowser, getopt, os.path, sys
import httplib2
from oauth2client import client
from apiclient.discovery import build
from oauth2client.file import Storage

blogId = 4346786333440044000 # put your blog ID here
isDraft = True # Don't change this unless you are prepared to modify the script
postfile = ''
title = 'Default Title' # Change this to the default title you prefer

# comma delimited list of labels for the post.
# If you set a default list it will be overwritten
# if lables are supplied in the command line args
# otherwise the default list is used
labels = 'linux, rocks'

# At a minimum we must include the file containing our blog post
if(len(sys.argv) < 2):
    print("Usage: %s -f \"Filename\" [-t] \"My Title\" [-l] \"label,label\" [--publish]" % sys.argv[0])
    print("Post's are uploaded as drafts by default. Use --publish if you want to "
            "publish immediatly\n")
    sys.exit()
 
# Handle arguments
myopts, args = getopt.getopt(sys.argv[1:], "f:t:l:", ['publish'])
for o, a in myopts:
    if o == '-f':
        postfile = a
    elif o == '--publish':
        isDraft = False
    elif o == '-t':
        title = a
    elif o == '-l':
        labels = a

# If we want to publish we must supply a title
if(isDraft == False and title == 'Default Title'):
    print("You must provide a title if you want to publish")
    sys.exit()


# If there is no userkey authenticate with Google and save the key.
if(os.path.exists('userkey') == False):
    flow = client.flow_from_clientsecrets('client_id.json',
            scope='https://www.googleapis.com/auth/blogger',
            redirect_uri='urn:ietf:wg:oauth:2.0:oob'
            )

    auth_uri = flow.step1_get_authorize_url()
    webbrowser.open_new(auth_uri)
    auth_code = raw_input('Enter the auth code: ')
    credentials = flow.step2_exchange(auth_code)
    http_auth = credentials.authorize(httplib2.Http())

    # Store the credentials
    storage = Storage('userkey')
    storage.put(credentials)

# If the userkey already exists use it.
else:
    storage = Storage('userkey')
    credentials = storage.get()
    http_auth = credentials.authorize(httplib2.Http())

# Initialize the blogger service and get the blog
blogger_service = build('blogger', 'v3', http=http_auth)

# Open file for reading
try:
    f = open(postfile, 'r')
except:
    print("Error open file. Aborting...")
    sys.exit()

#build a label list
labels_list = labels.split(',')

#build body object
body = {
        "content": f.read(),
        "title": title,
        "labels": labels_list
        }
#Insert the post
try:
    post = blogger_service.posts().insert(blogId=blogId, body=body, isDraft=isDraft).execute()
except:
    print("Something went wrong uploading this post")
    sys.exit()

print("Title: %s" % post['title'])
print("Is Draft: %s" % isDraft)
if(isDraft == False):
    print("URL: %s" % post['url'])
print("Labels: %s" % post['labels'])


