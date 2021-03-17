# WHAT _IS_ THIS PROJECT?
This is a collection of Dockerfiles each designed serve up compiled documentation for specific Python libraries. 

# WHY DID YOU DO THIS?
Over the past month I've had a number of issues with my internet which affect my ability to actually get work done. The biggest problem I have when the internet stops working is that I lose access to documentation and references for all the libraries / frameworks I just happen to be using at the time.

This collection of Dockerfiles aims to fix that by generating project documentation and hosting it locally via nginx. Documentation generated is _usually_ complete and comes with a search function powered by JS magic (don't ask me how it works, IDK).

# HOW DOES THIS WORK?
Each Dockerfile is multi-stage - the first stage will compile the project documentation using Sphinx / MKDocs / whatever. The second stage will take these files and serve them up via `nginx:stable`.

# HOW DO I USE THEM
1. `docker build -t <your tag here> -f <pick from any one of the files available> .`
1. `docker run -p <port mapping here> <tag specified in step 1 here>`

Adjust the 2nd step to fit into your setups as needed. 

# KNOWN ISSUES
- Each dockerfile checks out the master branch of each project. If you need documentation for a specific version you'll have to edit the command in the Dockerfile to check out a specific tag, or branch, in addition to cloning the repo.
