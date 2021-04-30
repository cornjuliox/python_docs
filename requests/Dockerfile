FROM python:3.8 as builder
RUN ["mkdir", "/pythonsrc"]
WORKDIR "/pythonsrc"

RUN ["git", "clone", "https://github.com/psf/requests.git", "."]
RUN ["pip", "install", "sphinx"]

WORKDIR "docs/"

RUN ["make", "html"]

FROM nginx:stable
COPY --from=builder /pythonsrc/docs/_build/html /usr/share/nginx/html/requests
