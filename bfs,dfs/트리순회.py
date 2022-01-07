import sys

input=sys.stdin.readline

n = int(input())

graph={}
for i in range(n):
    root,left,right = map(str,input().strip().split())
    graph[root]=[left,right]

def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(graph[root][0])  # left
        preorder(graph[root][1])  # right
 
 
def inorder(root):
    if root != '.':
        inorder(graph[root][0])  # left
        print(root, end='')  # root
        inorder(graph[root][1])  # right
 
 
def postorder(root):
    if root != '.':
        postorder(graph[root][0])  # left
        postorder(graph[root][1])  # right
        print(root, end='')  # root
 
 
preorder('A')
print()
inorder('A')
print()
postorder('A')
