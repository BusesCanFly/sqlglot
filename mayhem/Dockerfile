FROM fuzzers/atheris:2.0.7-python3.9

RUN pip install sqlglot
COPY . /src
WORKDIR /src
RUN chmod +x /src/mayhem/fuzz_sqlglot.py
CMD ["/src/mayhem/fuzz_sqlglot.py"]
