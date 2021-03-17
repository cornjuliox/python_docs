FROM python:3.8 as builder
RUN ["mkdir", "/pythonsrc"]
WORKDIR "/pythonsrc"
RUN ["git", "clone", "https://github.com/samuelcolvin/pydantic.git", "."]

RUN ["pip", "install", "-r", "requirements.txt"]
RUN ["pip", "install", "mkdocs"]

# NOTE: These three are copied straight from the Fastapi file.
#       you might not actually need all these. 
RUN ["pip", "install", "pymdown-extensions"]
RUN ["pip", "install", "mkdocs-material"]
RUN ["pip", "install", "mdx_truly_sane_lists"]
RUN ["pip", "install", "markdown-include"]
RUN ["pip", "install", "mkdocs-exclude"]
RUN ["pip", "install", "mkpdfs-mkdocs"]
RUN ["pip", "install", "mkdocs-markdownextradata-plugin"]
RUN ["mkdocs", "build"]

FROM nginx:stable
COPY --from=builder /pythonsrc/site /usr/share/nginx/html
