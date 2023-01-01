#! /usr/bin/python3

import atheris
import sys

with atheris.instrument_imports():
    import sqlglot
    from sqlglot import parse_one, exp
    from sqlglot.optimizer import optimize


@atheris.instrument_func
def test_input(input_bytes):
    fdp = atheris.FuzzedDataProvider(input_bytes)
    input_string = fdp.ConsumeUnicodeNoSurrogates(sys.maxsize)
    input_str_w_surrogates = fdp.ConsumeUnicode(sys.maxsize)
    input_int = fdp.ConsumeInt(sys.maxsize)
    
    try:
        # sqlglot.transpile(input_string, read=input_string, write=input_string)
        parse_one(input_string).find_all(exp.Column)
        # optimize(sqlglot.parse_one(input_string), 
        #     schema={input_string: {input_string: input_string}}
        #     ).sql(pretty=True)
    except AttributeError: # NoneType.something()
        pass
    except ValueError: # might be missing some good errors
        pass

def main():
    atheris.Setup(sys.argv, test_input)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
