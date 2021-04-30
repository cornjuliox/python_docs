FROM python:2 as builder
RUN ["mkdir", "/pythonsrc"]
WORKDIR "/pythonsrc"
RUN ["git", "clone", "https://github.com/mongodb/docs.git", "."]
RUN ["pip", "install", "-r", "requirements.txt"]
RUN ["which", "sphinx-build"]
RUN ["make", "html"]

# FROM nginx:stable
# COPY --from=builder /pythonsrc/docs/_build/html /usr/share/nginx/html
