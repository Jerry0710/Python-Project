# 将运算式表示成后缀写法
# 例如： A * B + C * D 可以表示为 A B * C D * +
#       A * ( B + C ) * D 可以表示为 A B C + * D *

def infix_to_postfix(infix:str):
    infix_list = infix.strip().split()
    postfix_list = []
    stack = []
    prec = {'*':3, '/':3, '+':2, '-':2}
    prec.update({'(':1})
    for token in infix_list:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            postfix_list.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                postfix_list.append(stack.pop())
            stack.pop()
        else:
            while stack != [] and prec.get(token) < prec.get(stack[-1]):
                postfix_list.append(stack.pop())
            stack.append(token)
    while stack != []:
        postfix_list.append(stack.pop())
    return ' '.join(postfix_list)


if __name__ == '__main__':
    print(infix_to_postfix(' ( A + B ) * ( C + D )'))
    print(infix_to_postfix('( A + B ) * C '))
