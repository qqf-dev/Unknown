from TNumber import *


def integrate(li) -> str:
    t = 0
    temp_array = []
    if li[0].islower():
        while li[t].isnumeric() or li[t].islower():
            temp_array.append(li[t])
            t += 1
            if t + 1 > len(li):
                break
    else:
        while li[t].isnumeric():
            temp_array.append(li[t])
            t += 1
            if t + 1 > len(li):
                break
    return "".join(temp_array)


class BNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.item)

    def node_id(self):
        result = [id(self.item)]
        if self.left:
            result + self.left.node_id()
        if self.left:
            result + self.left.node_id()

        return result

    def __eq__(self, other):
        if isinstance(other, BNode):
            return self.node_id() == other.node_id()
        return False


def check(element) -> BNode:
    if not isinstance(element, BNode):
        element = BNode(element)
    return element


class BTree:
    def __init__(self):
        self.root = BNode('root')

    def __str__(self):
        return str(self.dict_order(self.root))

    def dict_order(self, node):  # an cen shu chu
        if not node:
            return []
        if not (node.left or node.right):
            return node.item
        return [node.item] + [[self.dict_order(node.left)]] + [[self.dict_order(node.right)]]

    def p_order(self, node):
        if not node:
            return []

        m: [] = [node]
        result = [node]
        while node.right:
            result.append(node.right)
            node = node.right
            m.append(node)

        for k in m:
            if k.left:
                result = result + self.p_order(k.left)

        return result

    def inorder(self, node) -> list:  # 中序遍历
        if node is None:
            return []
        result = [node]
        left_item = self.inorder(node.left)
        right_item = self.inorder(node.right)
        return left_item + result + right_item

    def postorder(self, node) -> list:  # 后序遍历
        if node is None:
            return []
        result = [node]
        left_item = self.postorder(node.left)
        right_item = self.postorder(node.right)
        return left_item + right_item + result

    def preorder(self, node) -> list:  # 先序遍历
        if node is None:
            return []
        result = [node]
        left_item = self.preorder(node.left)
        right_item = self.preorder(node.right)
        return result + left_item + right_item

    def add(self, node):
        node = check(node)

        if self.root.item == 'root':
            self.root = node
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node

                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def add_r(self, str_node, node):
        node = check(node)

        if self.root.item == 'root':
            self.root = node
        else:
            q = [str_node]
            while True:
                pop_node = q.pop(0)
                if not pop_node.right:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.right)

    def add_l(self, str_node, node):
        node = check(node)

        if self.root.item == 'root':
            self.root = node
        else:
            q = [str_node]
            while True:
                pop_node = q.pop(0)
                if not pop_node.left:
                    pop_node.left = node
                    return
                else:
                    q.append(pop_node.left)

    def search(self, element) -> BNode:
        element = check(element)
        li: [] = self.p_order(self.root)

        for result in li:
            if result == element:
                return result


class ValueTree:
    def __init__(self, value):
        self.stack = []
        self.tree = []
        if self.to_stack(value):
            self.to_tree()

    def set_stack(self, stack):
        self.stack = stack

    def to_stack(self, value):
        stack = []
        li = []
        if isinstance(value, str):
            li = list(value)
        else:
            raise ValueError("value should be string and length > 0")

        length = len(li)

        # integrate
        i = 0
        while i < length:
            m = li[i]
            if m.isnumeric() or m.islower():
                t = integrate(li[i:])
                stack.append(t)
                i += len(t)
                if i < length:
                    if li[i].islower():
                        stack.append('*')
            else:
                stack.append(m)
                i += 1

        # enter the stack
        stack_p = []
        for item in stack:
            if item.isnumeric() or item.islower():  # 如果当前字符为数字那么直接放入结果列表
                self.stack.append(item)
            else:  # 如果当前字符为一切其他操作符
                if len(stack_p) == 0:  # 如果栈空，直接入栈
                    stack_p.append(item)
                elif item in lever(3) or item == '(':  # 如果当前字符为 ^(，直接入栈
                    stack_p.append(item)
                elif item == ')':  # 如果右括号则全部弹出（碰到左括号停止）
                    t = stack_p.pop()
                    while t != '(':
                        self.stack.append(t)
                        t = stack_p.pop()
                # 如果当前字符为加减且栈顶为乘除or power，则开始弹出
                elif item in lever(1) and (stack_p[-1] in lever(2) or stack_p[-1] in lever(3)):
                    if stack_p.count('(') == 0:  # 如果没有左括号，弹出所有
                        while stack_p:
                            self.stack.append(stack_p.pop())
                    else:  # 如果有左括号，弹到左括号为止
                        t = stack_p.pop()
                        while t != '(':
                            self.stack.append(t)
                            t = stack_p.pop()
                        stack_p.append('(')
                    stack_p.append(item)  # 弹出操作完成后将‘+-’入栈
                elif item in lever(2) and stack_p[-1] in lever(3):
                    if stack_p.count('(') == 0:  # 如果没有左括号，弹出所有
                        while stack_p:
                            self.stack.append(stack_p.pop())
                    else:  # 如果有左括号，弹到左括号为止
                        t = stack_p.pop()
                        while t != '(':
                            self.stack.append(t)
                            t = stack_p.pop()
                        stack_p.append('(')
                    stack_p.append(item)  # 弹出操作完成后将‘*/’入栈:
                else:
                    stack_p.append(item)  # 其余情况直接入栈（如当前字符为+，栈顶为+-

        while stack_p:
            self.stack.append(stack_p.pop())

        return self.stack

    def to_tree(self):
        if not self.stack:
            return

        stack = self.stack[::-1]
        b = BTree()

        p_node = b.root
        fi = False
        c = []
        for i in stack:
            if isinstance(i, str):
                if not fi:
                    if i.islower() or i.isnumeric():
                        b.add_r(p_node, i)
                        fi = True
                    else:
                        if p_node.item == 'root':
                            b.add(i)
                            p_node = b.root
                            c.append(p_node)
                        else:
                            b.add_r(p_node, i)
                            p_node = p_node.right
                            c.append(p_node)
                else:
                    t = c.pop()
                    b.add_l(t, i)
                    p_node = t.left
                    if not c:
                        fi = False
                        c.append(p_node)

        self.tree = b

    def out(self):
        return self

    def get_size(self):
        return len(self.stack)


if __name__ == '__main__':
    a = ValueTree('2a*b+c*d^2')
    print(a.tree)
