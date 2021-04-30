FROM python:3.8 as builder
RUN ["mkdir", "/pythonsrc"]
WORKDIR "/pythonsrc"
RUN ["git", "clone", "https://github.com/pytest-dev/pytest.git", "."]
# RUN ["pip", "install", "poetry"]
# RUN ["poetry", "install"]
RUN ["pip", "install", "tox"]
RUN ["tox", "-e", "docs"]
# WORKDIR "/pythonsrc/doc/en"
# RUN ["pip", "install", "-r", "requirements.txt"]

FROM nginx:stable
COPY --from=builder /pythonsrc/doc/en/_build/html /usr/share/nginx/html/pytest
