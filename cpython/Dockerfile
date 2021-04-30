FROM python:3.8 as builder
RUN ["mkdir", "/pythonsrc"]
WORKDIR "/pythonsrc"
RUN ["git", "clone", "https://github.com/python/cpython.git", "."]
WORKDIR "Doc"
RUN ["pwd"]
RUN ["make", "venv"]
RUN ["make", "html"]

FROM nginx:stable
COPY --from=builder /pythonsrc/Doc/build/html /usr/share/nginx/html/python
