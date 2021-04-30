FROM python:3.8 as builder
RUN ["mkdir", "/pythonsrc"]
WORKDIR "/pythonsrc"
RUN ["git", "clone", "https://github.com/arrow-py/arrow.git", "."]
RUN ["pip", "install", "-r", "requirements.txt"]
WORKDIR "docs"
RUN ["make", "html"]

FROM nginx:stable
COPY --from=builder /pythonsrc/docs/_build/html /usr/share/nginx/html

