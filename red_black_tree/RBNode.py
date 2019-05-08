class RBT:
    def __init__(self):
        #self.items[]
        self.root = None
        self.zlist = []

    def LEFT_ROTATE(self,node):
        #node是一个红黑树节点
        y = node.right
        if y is None
            #右节点为空
            return 0
        else :
            beta = y.left 
            node.right = beta
            if beta is not None:
                beta.parent = node
            p = node.parent
            y.parent = p
            if p is None:
                #node原来是root
                self.root = y
            elif node == p.left:
                p.left = y
            else:
                p.right = y
            y.left = node
            node.parent = y
        
    
    def RIGHT_ROTATE(self,y):
        #y也是一个节点
        node = y.left
        if node is None:
            #则右节点为空不旋转
            return 0
        else:
            beta = node.right
            y.left = beta
            if beta is not None:
                beta.parent = y
            p = y.parent
            node.parent = p
            if p is None:
                #y原来是根节点
                self.root = node
            elif y == p.left:
                p.left = node
            else:
                p.right = node
            node.right = y
            y.rightn = node
    #对红黑数进行插入新数z的操作
    def INSERT(self,val):
        z = RBTnode(val)
        y = None
        node = self.root
        while node is not None:
            y = node
            if z.val < node.val:
                node = node.left 
        z.PAINT(RED)
        z.parent = y
        if y is None:
            #那么插入Z之前的RBT为空
            self.root = z
            self.INSERT_FIXUP(z)
            return 0
        if z.val < y.val:
            y.left = z
        else:
            y.right = z
        if y.color == RED:
            #Z的父节点是Y 此时的Y是红色 ，需要修正红黑树
            #如果Z的父亲节点是黑色的话，那么不需要对此修正
            self.INSERT_FIXUP(z)
        else:
            return 0
    def INSERT_FIXUP(self,z):
        #如果满足：Z为根节点
        if z.parent is None:
            z.PAINT(BLACK)
            self.root = z
            return 0
        #如果Z的父节点为黑色
        if z.parent.color == BLACK:
            #可能此时的Z处于第二层
            #如Z为最后一个的话，感觉没有必要将其修正
            return 0
        #之后的条件都是在满足Z的父节点是红色的时候
        #节点Y应该在逻辑上是Z的舅舅
        if z.parent.color == RED:
            p = z.parent
            #g应该是node的祖父节点
            g = p.parent
            if g is None:
                return 0
            if g.right == p:
                y = g.left
            else:
                y = g.right
         #现在若满足Z没有叔叔，也就是Y是空节点的时候
         # PS：此时Z的父节点一定是红色
         if y == None:
             if z == p.right and p == p.parent.left:
                #现在若满足Z没有叔叔，也就是Y是空节点的时候
                #Z为有儿子，且P为左儿子，则把P左旋转
                self.LEFT_ROTATE(p)
                p,z = z,p
                g.PAINT(RED)
                p.PAINT(BLACK)
                if p == g.left:
                    #现在若满足Z没有叔叔，也就是Y是空节点的时候
                    #p为g的左儿子
                    self.RIGHT_ROTATE(g)
                else:
                    #现在若满足Z没有叔叔，也就是Y是空节点的时候
                    #p为g的右儿子
                    self.LEFT_ROTATE(g)
                return 0
        #现在假如Z有黑色的叔叔
        elif y.color == BLACK:
            if p.right == z and p.parent.left == p:
                 #现在假如Z有黑色的叔叔
                 #Z此时为右儿子，P为左儿子，则左旋转P
                 #转化为Z此时为左儿子，则右旋转g
                 self.LEFT_ROTATE(p)
                 p,z = z,p
            elif p.left == z and p.parent.right == p:
                self.RIGHT_ROTATE(p)
                p,z = z,p
            p = z,parent
            g = p.parent

            P.PAINT(BLACK)
            g.PAINT(RED)
            if p == g.left:
                 #现在假如Z有黑色的叔叔
                 #Z此时为左儿子，则右旋转g
                 self.RIGHT_ROTATE(g)
            else:
                 #现在假如Z有黑色的叔叔
                 #Z此时为右儿子，则左旋转g
                 self.LEFT_ROTATE(g)
            return 0
        else:
            #Z有红色叔叔
            #那么黑父亲和叔叔，将叔叔变为红色，递归调用
            y.PAINT(BLACK)
            P.PAINT(BLACK)
            new_z = g
            self.INSERT_FIXUP(new_z)

    def DELETE(self,val):
        curNode = self.root
        while curNode is not None:
            if val < curNode.val:
                curNode = curNode.left 
            elif val > curNode.val:
                curNode = curNode.right
            else:
                #此时找到了val的元素，开始删除
                if curNode.left is None and curNode.right is  None:
                    #第一种情况：curNode为叶子节点：直接删除该节点
                    if curNode == self.root:
                        self.root = None
                    else:
                        p = curNode.parent
                        if curNode == p.left:
                            p.left = None
                        else:
                            p.right = None
                elif curNode.left is not None and curNode.right is not None:
                    sucNode = self.SUCCESOR(curNode)
                    curNode.val,sucNode.val = sucNode.val,curNode.val
                    self.DELETE(sucNode.val)
                else:
                    p = curNode.parent
                    if curNode.left is None:
                        node = curNode.right
                    else:
                        node = curNode.left 
                    if curNode == p.left:
                        p.left = node
                    else:
                        p.right = node 
                    node.parent = p
                    if curNode.color == BLACK:
                        self.DELETE_FIXUP(node)
                curNode = None
        return False
    
    def DELETE_FIXUP(self,node):
        p = node.parent
        #w:为node的兄弟节点
        if x == p.left:
            w = x.right
        else:
            w = x.left

        # case1:x的兄弟w是红色的
        if w.color == RED:
            p.PAINT(RED)
            w.PAINT(BLACK)
            if w == p.right:
                self.LEFT_ROTATE(p)
            else:
                self.RIGHT_ROTATE(p)

        if w.color == BLACK:
            # case2:x的兄弟w是黑色的，而且w的两个孩子都是黑色的
            if w.left.color == BLACK and w.right.color == BLACK:
                w.PAINT(RED)
                if p.color == BLACK:
                    return
                else:
                    p.color = BLACK
                    self.DELETE_FIXUP(p)

            # case3:x的兄弟w是黑色的，而且w的左儿子是红色的，右儿子是黑色的
            if w.left.color == RED and w.color == BLACK:
                w.left.PAINT(BLACK)
                w.PAINT(RED)
                self.RIGHT_ROTATE(w)

            # case4:x的兄弟w是黑色的，而且w的右儿子是红
            if w.right.color == RED:
                p.PAINT(BLACK)
                w.PAINT(RED)
                if w == p.right:
                    self.LEFT_ROTATE(p)
                else:
                    self.RIGHT_ROTATE(p)

    def SHOW(self):
        self.DISPLAY1(self.root)
        return self.zlist

    def DISPLAY1(self, node):
        if node is None:
            return
        self.DISPLAY1(node.left)
        self.zlist.append(node.val)
        self.DISPLAY1(node.right)

    def DISPLAY2(self, node):
        if node is None:
            return
        self.DISPLAY2(node.left)
        print node.val,
        self.DISPLAY2(node.right)

    def DISPLAY3(self, node):
        if node is None:
            return
        self.DISPLAY3(node.left)
        self.DISPLAY3(node.right)
        print node.val,






class RBTnode:
    '''红黑树的节点类型'''
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def PAINT(self, color):
        self.color = color


def zuoxuan(b, c):
    a = b.parent
    a.left = c
    c.parent = a
    b.parent = c
    c.left = b

if __name__ == '__main__':
    rbt=RBT()
    b = []

    for i in range(100):
        m = randint(0, 500)
        rbt.INSERT(m)
        b.append(m)

    a = rbt.SHOW()
    b.sort()
    equal = True
    for i in range(100):
        if a[i] != b[i]:
            equal = False
            break

    if not equal:
        print 'wrong'
    else:
        print 'OK!'

