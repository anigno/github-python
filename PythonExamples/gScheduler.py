import greenlet

def foo():
    print("Foo 1")
    gr2.switch()
    print("Foo 2")
    gr2.switch()
    print("Foo 3")

def bar():
    print("Bar 1")
    gr1.switch()
    print("Bar 2")
    gr1.switch()

# Create two greenlets
gr1 = greenlet.greenlet(foo)
gr2 = greenlet.greenlet(bar)

# Start execution of the first greenlet
gr1.switch()

"""
Bar 1
Foo 2
Bar 2
Foo 3
"""