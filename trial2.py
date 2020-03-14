import ast

tree = ast.parse("print('hello world')")
print(ast.dump(tree))

exec(compile(tree, filename="<ast>", mode="exec"))
