cpp_keywords = {"auto", "double", "int", "struct", "break", "else", "long", "switch", "case", "enum", "register", "typedef", "char", "extern", "return", "union", "const", "float", "short", "unsigned", "continue", "for", "signed", "void", "default", "goto", "sizeof", "volatile", "do", "if", "static", "while", "asm", "dynamic_cast", "namespace", "reinterpret_cast", "bool", "explicit", "new", "static_cast", "catch", "false", "operator", "template", "class", "friend", "private", "this", "const_cast", "inline", "public", "throw", "delete", "mutable", "protected", "true", "try", "typeid", "typename", "using", "virtual", "wchar_t"}

operators = {"!=","!", "==", "=", "+", "-", "/", ",", "*", "|", "&", "||", "&&", "%", "^", "<=", ">=", "<", ">", "(", ")"}

def Token_Analyzer(statements):

    parameters = {"keywords":0, "operators":0, "identifiers": 0}
    tokens = []

    for statement in statements.split(";"):
        if statement != "":
            start = 0
            flag = None
            if statement[0] in operators:
                flag = "op"
            else:
                flag = "word"

            for i in range(1,len(statement)):
                if statement[i] in operators:
                    if flag=="op":
                        pass
                    else:
                        token = statement[start:i]
                        l1 = token.split()
                        if len(l1) == 1:
                            tokens.append(token)
                            start = i
                            flag = "op"
                        else:
                            tokens.extend(l1)
                            start = i
                            flag = "op"
                else:
                    if flag=="word":
                        pass
                    else:
                        tokens.append(statement[start:i])
                        start = i
                        flag = "word"
            tokens.append(statement[start:])

    for token in tokens:
        if token.strip() in cpp_keywords:
            parameters["keywords"] += 1
        elif token.strip() in operators:
            parameters["operators"] += 1
        elif token.strip().isidentifier()==True:
            parameters["identifiers"] += 1
        else:
            pass

    return parameters


if __name__=="__main__":
    statements = input()
    print(Token_Analyzer(statements))