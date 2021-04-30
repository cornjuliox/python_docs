FROM python:3.8 as builder
RUN ["mkdir", "/pythonsrc"]
WORKDIR "/pythonsrc"
RUN ["git", "clone", "https://github.com/tiangolo/fastapi.git", "."]
RUN ["git", "checkout", "0.63.0"]
WORKDIR "docs/en"

# I absolutely refuse to install Poetry.
RUN ["pip", "install", "mkdocs"]
RUN ["pip", "install", "pymdown-extensions"]
RUN ["pip", "install", "mkdocs-material"]
RUN ["pip", "install", "markdown-include"]
RUN ["pip", "install", "mkdocs-markdownextradata-plugin"]
RUN ["mkdocs", "build"]

FROM nginx:stable
COPY --from=builder /pythonsrc/docs/en/site /usr/share/nginx/html/fastapi
