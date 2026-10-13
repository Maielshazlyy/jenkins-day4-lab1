# Two Jenkins pipelines: Node.js and Python Docker apps

This project has two independent Jenkins pipelines. Each checks out this GitHub repository, builds its app's Docker image, runs a small web server in a container, and pushes the image to Docker Hub tagged with the Jenkins build number.

## Project layout

```text
jenkins-two-apps/
├── Jenkinsfile-node
├── Jenkinsfile-python
├── node-app/
│   ├── app.js
│   └── Dockerfile
└── python-app/
    ├── app.py
    └── Dockerfile
```

## 1. Create the GitHub repository

Create a repository and push the contents of this folder to its `main` branch. The Jenkinsfiles and both app folders must be at the repository root, as shown above.

## 2. Create Jenkins credentials

In Jenkins, open **Manage Jenkins → Credentials → System → Global credentials → Add Credentials**.

For GitHub, create a personal access token that can read the repository. Add it as:

- Kind: **Username with password**
- Username: your GitHub username
- Password: your GitHub token
- ID: `github-token`

For a public repository, you can remove the `credentialsId` from both Jenkinsfiles and checkout anonymously.

For Docker Hub, create an access token and add:

- Kind: **Username with password**
- Username: your Docker Hub username
- Password: your Docker Hub access token
- ID: `dockerhub`

Keep tokens in Jenkins credentials; do not commit them to GitHub.

## 3. Set the repository URL

In both `Jenkinsfile-node` and `Jenkinsfile-python`, replace `https://github.com/USERNAME/REPOSITORY.git` with your GitHub repository URL. Commit and push those edits.

## 4. Create the Node.js Jenkins job

Create a Pipeline job named `hello-node`. Under **Pipeline**, select **Pipeline script from SCM**, then configure:

- SCM: **Git**
- Repository URL: your GitHub repository URL
- Credentials: `github-token` (if required)
- Branch: `*/main`
- Script Path: `Jenkinsfile-node`

Save and run **Build Now**. It starts the app on port 3000 and publishes `YOUR_DOCKERHUB_USERNAME/hello-node:<BUILD_NUMBER>`.

## 5. Create the Python Jenkins job

Create another Pipeline job named `hello-python` with the same SCM settings, but set **Script Path** to `Jenkinsfile-python`. Save and run **Build Now**. It starts the app on port 5000 and publishes `YOUR_DOCKERHUB_USERNAME/hello-python:<BUILD_NUMBER>`.

## Docker mount

## View the apps

After each pipeline succeeds, open `http://localhost:3000` for Node.js or `http://localhost:5000` for Python on the machine running Docker. The pipelines replace the previous named container when rerun. If Jenkins runs inside Docker on another machine, use that machine's hostname or IP instead of `localhost`.

## Agent requirements

The Jenkins agent needs Git and Docker installed, permission to run Docker, and network access to GitHub and Docker Hub.
