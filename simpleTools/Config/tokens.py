def _tokenize(expr: str) -> list:
    tokens = []
    expr_len = len(expr)
    i = 0
    
    while i < expr_len:
        sym = ""
        if expr[i].isdigit():
            sym = expr[i]
            try:
                if expr[i - 1] == "-":
                    sym = "-" + sym
                    print("find '-': ", sym)
            except IndexError:
                pass
            
            digit_i = i + 1
            while digit_i < expr_len:
                if expr[digit_i].isdigit() or expr[digit_i] == ".": 
                    sym = sym + expr[digit_i]
                    digit_i += 1
                else:
                    i = digit_i - 1
                    break
            
            tokens.append(("NUM", float(sym)))
            
        elif expr[i].isalpha():
            sym = expr[i]
            tokens.append(("VAR", sym))
            
        elif expr[i] in "+-*/":
            if i != 0:
                sym = expr[i]
                tokens.append(("OPER", sym))
            else:
                print(f"ignore this operator: {expr[i]}, i={i}")
        elif expr[i] == "(":
            sym = expr[i]
            tokens.append(("LPAR", sym))
        elif expr[i] == ")":
            sym = expr[i]
            tokens.append(("RPAR", sym))
        else:
            raise ValueError(f"Unknown token {expr[i]}")
             
        i += 1            
    print(tokens)
    return tokens
    
class _token_expression:
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.tree = None
        self.result = None
        #print(self.tokens)
    
    def find_operand_index(self, tokens: list, operands: str):
        i = None
        for index, token in enumerate(tokens):
            if token[0] == "OPER" and str(token[1]) in operands:
                i = index
        return i
            
    def create_tree(self, tokens):
        if len(tokens) == 1:
            return tokens[0]
            
        i = self.find_operand_index(tokens, "+-")
        if i is not None:
            oper = tokens[i][1]
            left = self.create_tree(tokens[:i])
            right = self.create_tree(tokens[i + 1:])
            return ("OPER", oper, left, right)
        
        i = self.find_operand_index(tokens, "*/")
        if i is not None:
            oper = tokens[i][1]
            left = self.create_tree(tokens[:i])
            right = self.create_tree(tokens[i + 1:])
            return ("OPER", oper, left, right)
        
        raise ValueError(f"Unredable: {tokens}")
            
    def write_tree(self):
        self.tree = self.create_tree(self.tokens)
    
    def show_tree(self, tree: list, margin: int=0):
        if tree[0] == "NUM" or tree[0] == "VAR":
            print(margin * " " + f"{tree}")
        elif tree[0] == "OPER":
            print(margin * " " + f"{tree[:2]}")
            m = margin + 3
            self.show_tree(tree[2], m)
            self.show_tree(tree[3], m)
            
    def convert(self):
        print(self.tree)
        if self.tree and len(self.tree) == 2:
            if self.tree[0] == "NUM":
                self.result = self.tree[1]
                return self.result
        
    def simplify(self, node: list):
        if node[0] in ("NUM", "VAR"):
            return node
        
        if node[0] == "OPER":
            left = self.simplify(node[2])
            right = self.simplify(node[3])
            
            if node[1] == "*" and (right[0] == "NUM" and right[1] == 0): 
                return ("NUM", 0)
            elif node[1] == "*" and (left[0] == "NUM" and left[1] == 0): 
                return ("NUM", 0)
                
            if node[1] == "+" and (right[0] == "NUM" and right[1] == 0): 
                return left
            elif node[1] in "+" and (left[0] == "NUM" and left[1] == 0): 
                return right
            elif node[1] == "-" and (right[0] == "NUM" and right[1] == 0): 
                return left
                
            if node[1] == "*" and (right[0] == "NUM" and right[1] == 1):
                return left
            elif node[1] == "*" and (left[0] == "NUM" and left[1] == 1):
                return right
                
            if node[1] == "+" and left[0] == "NUM" and right[0] == "NUM":
                return ("NUM", left[1] + right[1])
            elif node[1] == "-" and left[0] == "NUM" and right[0] == "NUM":
                return ("NUM", left[1] - right[1])
            elif node[1] == "*" and left[0] == "NUM" and right[0] == "NUM":
                return ("NUM", left[1] * right[1])
            elif node[1] == "/" and left[0] == "NUM" and right[0] == "NUM":
                return ("NUM", left[1] / right[1])
            return node
            
    def simplify_tree(self, node: list):
        self.tree = self.simplify(node)
        res = self.convert()
        return res
        
        
                        
        
        
    
            
                
