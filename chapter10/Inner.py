class External:
    def __init__(self):
        print("External constructor")
    def external_method(self):
        print("External method")
    class Internal:
        def __init__(self):
            print("Internal constructor")
        def internal_method(self):
            print("Internal method")

ext = External()
ext.external_method()
internal = ext.Internal()
internal.internal_method()