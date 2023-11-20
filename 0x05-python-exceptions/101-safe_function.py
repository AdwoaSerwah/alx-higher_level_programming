#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        sk_res = fct(*args)
        return sk_res
    except Exception as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return None
