def check_scope():
    def do_local():
        test = "local test"

    def do_non_local():
        nonlocal test
        test = "non local test"

    def do_global():
        global test
        test = "global test"

    test = "original test"
    do_local()
    print("local test sample : " + test)
    do_non_local()
    print("do_local_test sample : " + test)
    do_global()


check_scope()
print("do_global_test sample : " + test)
