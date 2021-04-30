FROM python:3.8 as builder
RUN ["mkdir", "/pythonsrc"]
WORKDIR "/pythonsrc"

RUN ["git", "clone", "https://github.com/scrapy/scrapy.git", "."]
WORKDIR "docs/"

RUN ["pip", "install", "-r", "requirements.txt"]
RUN ["make", "html"]

FROM nginx:stable
COPY --from=builder /pythonsrc/docs/build/html /usr/share/nginx/html/scrapy

