import re

def del_spaces(string: str) -> str:
    return "".join(string.split())
    
def norm_expr(string: str) -> str:
    expression = del_spaces(string)
    expression = expression.replace(",", ".")
    expression = expression.lower()
    return expression
    
def solve_pattern(expr: str, var: str, *args) -> float:
    user_vars = del_spaces(var).split(",")
    expression = del_spaces(expr)
    if len(user_vars) != len(args):
        raise IndexError("Uncorrect count of variables or arguments")
    table = []
    for varible in user_vars:
        table.append([varible, args[user_vars.index(varible)]])
    print(table)
    
    for el in table:
        expression = expression.replace(el[0], str(el[1]))
    return eval(expression)
    
    
    

class expression:
    def __init__(self, var: str, expr: str):
        self.var = del_spaces(var)
        self.expr0 = del_spaces(expr)
        
        find_pattern = fr"[+-]\d+{self.var}|[-+*/]\([+-]\d+{self.var}\)|[-+*/]\d+{self.var}|\d+[-+*/]{self.var}"  
        print(re.findall(find_pattern, self.expr0))