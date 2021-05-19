class Indenter:
    def __init__(self):
        self.indent_count = -1
        self.indent = '\t'
        self.indent_print = ''

    def print(self, string: str):
        self.indent_print = self.indent * self.indent_count
        print(self.indent_print, string,sep='')

    def __enter__(self):
        self.indent_count += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.indent_count -= 1
        return True


with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('talk is cheap')
        with indent:
            indent.print('show me the code ')
    indent.print('Torvalds')

# output is :

"""
hi!
	talk is cheap
		show me the code 
Torvalds



"""
