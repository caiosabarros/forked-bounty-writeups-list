import hashlib

def hash_leaf(leaf):
    # Convert the leaf to bytes
    leaf_bytes = str(leaf).encode('utf-8')

    # Calculate the hash of the leaf using SHA-256
    hash_object = hashlib.sha256(leaf_bytes)
    leaf_hash = hash_object.hexdigest()

    return leaf_hash

def construct_tree(nodes):
    # If there's only one node, it is the root
    if len(nodes) == 1:
        return nodes[0]

    parents = []
    num_nodes = len(nodes)

    # Sort the nodes
    sorted_nodes = sorted(nodes)

    # Pair up adjacent nodes and hash them
    for i in range(0, num_nodes, 2):
        node1 = sorted_nodes[i]
        # If there's an odd number of nodes, duplicate the last node
        if i == num_nodes - 1:
            node2 = sorted_nodes[i]
        else:
            node2 = sorted_nodes[i + 1]

        # Concatenate and hash the two nodes
        parent = hash_leaf(node1 + node2)
        parents.append(parent)

    # Recursively construct the tree with the parent nodes
    return construct_tree(parents)

def check_leaf_in_tree(leaf, leaves):
    # Hash the leaf to match the tree structure
    hashed_leaf = hash_leaf(leaf)

    # Check if the hashed leaf is in the list of hashed leaves
    return hashed_leaf in leaves

# Leaf nodes
leaves = ['6', '7']

# Hash the leaf nodes
hashed_leaves = [hash_leaf(leaf) for leaf in leaves]

# Construct the Merkle Patricia Tree
root = construct_tree(hashed_leaves)

# Print the root node
print("Root Node:", root)

# Check if a leaf is in the tree
leaf_to_check = '6'
is_leaf_in_tree = check_leaf_in_tree(leaf_to_check, hashed_leaves)

if is_leaf_in_tree:
    print(f"Leaf {leaf_to_check} is in the tree.")
else:
    print(f"Leaf {leaf_to_check} is not in the tree.")

# Print 0+root hash:
print("Child of Root Hash:", hash_leaf(root + '0'))
root = hash_leaf(root + '0')

leaf_to_check = '8'
is_leaf_in_tree = check_leaf_in_tree(leaf_to_check, hashed_leaves)

if is_leaf_in_tree:
    print(f"Leaf {leaf_to_check} is in the tree.")
else:
    print(f"Leaf {leaf_to_check} is not in the tree.")