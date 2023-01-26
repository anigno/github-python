class AnonimousObject(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__

anon = AnonimousObject(id=7, registered=True)  # ctor addition of attributes
anon.val = 4  # normal addition of attributes

print(anon)

if anon.registered:
    print(f"it's registered a={anon.val}")
