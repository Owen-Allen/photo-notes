# photo-notes

### What is it?

Photo Notes is a tool meant to help students take notes in the online environment, but can also be used for convenience.  When taking notes, it often helps to have the professors images and diagrams nested inside of your notes.  When using markdown, this can be inconvenient to do in class.  Using photoNotes, you can take a screenshot of your lecture as its playing and move it to whichever images directory you'd like to use for your class.  PhotoNotes also creates a markdown insertion link so that you can view the image within your notes.

### How does it work?

The tool works by monitoring new input in whatever directory your screenshots are automatically sent to.  When a new file is added to that directory when the program is running, it moves that file to whichever folder the user specifies at start time.


## SETUP

1. Download photoNotes.py file

2. Open photeNotes.py and modify the SCREENSHOTS_PATH variable to reflect the path where your screenshots are stored by default on your computer

3. Install aioconsole by running 'pip install aioconsole==0.3.3'.  To check if you already have it, type 'pip show aioconsole'

4. Move photoNotes.py to a binaries folder available in your PATH.  I used '/usr/local/bin'.  You can also remove the .py extension.


## DEMO

1. Open a Terminal in whichever directory you would like to take notes in.  In this example, I'm taking notes in the demo directory in the file called notes.md

2. If you'd like to store the images in a specific subfolder, create that folder.

![](images/Screen%20Shot%202022-01-06%20at%202.18.36%20PM.jpg)

3. Now that I have my directory set up, I can start taking notes.  I can run the command 'photonotes demoImages' in the background while I'm taking notes.

Taking a screenshot shows the following.

![](images/Screen%20Shot%202022-01-06%20at%202.27.39%20PM.jpg)

I can then copy the insertion link and put it in my notes.

