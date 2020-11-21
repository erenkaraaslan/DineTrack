# DineTrack
THIS IS THE PROTOTYPE BRANCH

Development Startup Steps

I recommend a virtual environment for development purposes. From there, all of the JS necessities should be in the repository meaning you can run "npm install ." to install necessary npm tools which will be read from package.json. The JS can be packed together using webpack so run "npx webpack" on each code change or run "npx webpack --watch" to automatically realize JS changes.

The bin folder holds scripts to make our life easier when developing. Run ./bin/dinetrackrun to start a server to host the website and check functionality. Make sure dinetrackrun is an executable by running chmod +x on it.
