FROM python:3.8 as builder
RUN ["mkdir", "/pythonsrc"]
WORKDIR "/pythonsrc"
RUN ["git", "clone", "https://github.com/mongodb/motor.git", "."]
RUN ["pip", "install", "sphinx"]
RUN ["pip", "install", "pymongo"]
WORKDIR "doc"
RUN ["pip", "install", "-r", "docs-requirements.txt"]
RUN ["make", "html"]

FROM nginx:stable
COPY --from=builder /pythonsrc/doc/_build/html /usr/share/nginx/html/motor
