from code_challenges.hashtables.hashtable import Hashtable


def tree_intersection(tree_a, tree_b):
    hashtable = Hashtable()
    intersections = []

    def create_hashtable(root):
        if root.left:
            create_hashtable(root.left)
        if root.right:
            create_hashtable(root.right)
        if hashtable.has(str(root.value)):
            hashtable.set(str(root.value), hashtable.get(str(root.value)) + 1)
        hashtable.set(str(root.value), 1)

    def find_intersections(root):
        if root.left:
            find_intersections(root.left)
        if root.right:
            find_intersections(root.right)
        if hashtable.has(str(root.value)):
            if hashtable.get(str(root.value)) > 0:
                intersections.append(root.value)
                hashtable.set(str(root.value), hashtable.get(str(root.value)) - 1)

    if tree_a.root and tree_b.root:
        create_hashtable(tree_a.root)
        find_intersections(tree_b.root)
    return intersections





