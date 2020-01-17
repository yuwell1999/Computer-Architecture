#规定树的左边节点为大的值，右边为小的值
#上往下生长，左边为1，右边为0
code_length = 0
class Node:
    def __init__(self,freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq
        self.depth = 1;
    def isLeft(self):
        return self.father.left == self

def createNodes(freqs):
    return [Node(freq) for freq in freqs]

def createHuffmanTree(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item:item.freq)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.freq + node_right.freq)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        node_father.depth += 1
        queue.append(node_father)
    queue[0].father = None
    return queue[0]

def huffmanEncoding(nodes,root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.isLeft():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_tmp = node_tmp.father
    return codes

if __name__ == '__main__':
    chars_freqs = [('P1',0.45),('P2',0.3),('P3',0.15),('P4',0.05),('P5',0.03),('P6',0.01),('P7',0.01)]
    nodes = createNodes([item[1] for item in chars_freqs])
    root = createHuffmanTree(nodes)
    codes = huffmanEncoding(nodes,root)
    for item in zip(chars_freqs,codes):
        print ('%s  Huffman编码: %s' % (item[0][0],item[1]))
        code_length = code_length + item[0][1]*len(item[1])
    print("最短编码长度为：",code_length)