# WHAT IS THIS PROJECT?
This is a collection of Dockerfiles each designed serve up compiled documentation for specific Python libraries. It achieves this through the use of multi-stage Docker builds, with the final stage copying the generated html files and static assets into the webroot of a stock nginx Docker container.

# WHY DID YOU DO THIS?
Over the past month I've had a number of issues with my internet which affect my ability to actually get work done. The biggest problem I have when the internet stops working is that I lose access to documentation and references for all the libraries / frameworks I just happen to be using at the time.

# HOW DOES THIS WORK?
Each Dockerfile is multi-stage - the first stage will compile the project documentation using Sphinx / MKDocs / etc. The second stage will take these files and serve them up via `nginx:stable`.

# HOW DO I USE THEM INDIVIDUALLY? 
1. `docker build -t <your tag here> -f <folder (arrow/cpython/etc)>/Dockerfile .`
1. `docker run -p <port mapping here> <tag specified in step 1 here>`
1. Documentation should then be available at `http://localhost:<port>/<library_name>`

Adjust the 2nd step to fit into your setups as needed. 

# HOW DO I USE THE DOCKER-COMPOSE FILE
`docker-compose up` will build every image in the project and start up containers for each of them.

`entrypoint` will be exposed on port 80, and serves up a simple listing of available documentation. Internally it will `proxy_pass` all requests to one of the running containers.

# KNOWN ISSUES
- Each dockerfile checks out the master branch of each project. If you need documentation for a specific version you'll have to edit the command in the Dockerfile to check out a specific tag, or branch, in addition to cloning the repo.
