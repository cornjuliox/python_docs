FROM python:3.8 as builder
RUN ["mkdir", "/pythonsrc"]
WORKDIR "/pythonsrc"
RUN ["git", "clone", "https://github.com/mongodb/mongo-python-driver.git", "."]
RUN ["pip", "install", "sphinx"]
WORKDIR "doc"
RUN ["make", "html"]

From nginx:stable
Copy --from=builder /pythonsrc/doc/_build/html /usr/share/nginx/html
