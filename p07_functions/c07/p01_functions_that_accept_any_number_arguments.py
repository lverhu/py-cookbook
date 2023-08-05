import html


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

def make_element(name, value, **attrs):
    keyvals = ['%s=%s' % item for item in attrs.items()]
    attr_str = ' '.join(keyvals)
    element = '<{name} {attrs}>{value}</{name}>'.format(
        name = name,
        attrs = attr_str,
        value = html.escape(value)
    )
    # print(attr_str)
    return element


# if __name__ == '__main__':
#     ele = make_element('item', 'Albatross', size='large', quantity=6)
#     print(ele)