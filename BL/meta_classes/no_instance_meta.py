class NoInstanceMeta(type):
    def __call__(cls, *args, **kwargs):
        raise TypeError(f"Cannot instantiate class {cls.__name__}")
