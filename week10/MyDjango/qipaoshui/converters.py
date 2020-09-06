class IntConverter:
    regex = '[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)

class IndexConverter:
    regex = '[a-z.a-z]'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value