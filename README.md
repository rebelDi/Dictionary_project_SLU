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
  

**Other commands**
### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
