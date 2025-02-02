def upper(fn):
    def inner(*args):
        args = [arg.title() for arg in args]
        return fn(*args)

    return inner


def reverse(fn):
    def inner(name):
        return fn(name[::-1])

    return inner


def html(tag="h1"):
    def wrapper(fn):
        def inner(*args):
            args_ = list(args)
            args_[0] = '<b>' + args_[0]
            args_[-1] = args_[-1] + '</b>'

            html_text = f'<{tag}>{fn(*args_)}</{tag}>'
            return html_text

        return inner
    return wrapper


@upper
@html()
def hello(name):
    return f'Hello {name}!'


@upper
@html(tag="h2")
def bye(name, last_name):
    return f'Bye {name} {last_name}!'


print(hello("john"))    # <h1>Hello <b>John</b></h1>
print(bye('john', 'smith'))      # <h2>Bye <b>John Smith</b></h2>
