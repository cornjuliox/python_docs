FROM python:3.8 as builder
RUN ["mkdir", "/pythonsrc"]
WORKDIR "/pythonsrc"
RUN ["git", "clone", "https://github.com/aio-libs/aiohttp.git", "."]
RUN ["pip", "install", "-r", "requirements/doc.txt"]
RUN ["pip", "install", "-r", "requirements/doc-spelling.txt"]
WORKDIR "docs"
RUN ["pwd"]
RUN ["make", "html"]

FROM nginx:stable
COPY --from=builder /pythonsrc/docs/_build/html /usr/share/nginx/html
