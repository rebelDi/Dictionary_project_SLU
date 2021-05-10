## -------------------------For users------------------------- ##

Right now the application only supports local deployment. In order to run it, you need to have `nodejs, python and pip` installed on your system. 
After you make sure to satisfy the requirement, go with command shell or terminal to directory of this repository on your machine. You need to run the `settings.sh`, which will download all the needed modules for proper work of the application, it is a shell script that you can run in Windows with:
### `sh settings.sh`
In Linux:
**First make it executable**
### `chmod +x settings.sh`
**Then run it:**
### `./settings.sh`

In MacOs:
### `bash settings.sh`

## This application needs two servers - for front end and api. In order to run api, go to the /Api directory of this project and run from the terminal:
### `npm start`
## Then open another terminal and go to the root directory of this project. Run from the terminal:
### `npm start`
You will automatically be transfered to the web page of the application in your local browser. Enjoy!

## Current bug: sometimes you can get a "Unicode misfunction error", our corpus has some special characters, which can break the Unicode while decoding the result. 
## Right now you can only try pulling the example from txt file corpus, if you want to try to access our database, you need to install `psycopg2` module on your machine. Then go to `back end/main.py` and comment line `110`, then uncomment line `111`.

## -------------------------For developers------------------------- ##

**This application is build using ReactJS, in order for it to work on your device make sure you have NodeJS**
  Use this [link](https://nodejs.org/en/download/) to install NodeJS
  Use this [link](https://reactjs.org/) to install all the needed modules and create a React Application to see if eveerything works
  
## To run the application:
  1. Open cmd/ Git Bash
  2. Go to the directory of the local repository on your device
  3. Enter 
### `npm start`
  4. It should open the local web page in your default browser (it is dynamic, so everytime you make a change you do not need to restart it, you make a change in code, it makes a change in web page)
    If not: open [http://localhost:3000](http://localhost:3000) to view it in the browser.

**DO NOT MERGE YOUR BRANCH WITH THE MASTER BRANCH WITHOUT CHECKING IF YOUR BRANCH WORKS AND DISCUSSING IT WITH THE GROUP**

## To make the web page visible globally via GitHub Pages for the Master Branch:
  1. Open Git Bash
  2. Go to the directory of the local repository on your device
  3. Enter 
### `npm install gh-pages --save-dev`

**Side note: if you get Error 126 when doing `npm start` enter 
### `chmod +x ./node_modules/.bin/react-scripts`

  4. Enter 
### `npm run deploy`
  5. Enter 
### `git add .`
  6. Enter 
### `git commit -m "[your commentary]"`
  7. Enter
### `git push origin master`

## To make the web page visible globally via GitHub Pages for the Your Branch:
  1. Open Git Bash
  2. Go to the directory of the local repository on your device
  3. Choose your branch
  4. Change 'master' in *package.json* to the *name of your branch* in 
``` 
...
"scripts": {
    ...
    "deploy": "gh-pages -b master -d build",
    ...
}    
```
  5. Enter 
### `npm install gh-pages --save-dev`
  6. Enter 
### `npm run deploy`
  7. Enter 
### `git add .`
  8. Enter 
### `git commit -m "[your commentary]"`
  9. Enter
### `git push origin [your branch]`
  10. Contact the creator of GitHub repository to change the settings to your branch
