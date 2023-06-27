# Understand Vulnerability

Vulnerability Classification: Logic Error

Bug Found:
A Merkle Patricia Tree on the OZ implementation was built using a leaf list, a proof list and a proof flags list. 
1. Leaf list: the leaves that will build up the tree
2. Proof list: a list of the concatenation of two siblings leaves.
3. Proof Flags list: a list 0's or 1's indicating where the element to be concanenated next will be gotten from: the hashes or the leaves list.

In the bug found, an element of the Proof list was gotten when the flags list had a 0. The thing is that, therefore, there should exist a check to check the same amount of 0's as there was of elements in the proof list.

# Situations

1. The first situation is if there were less proofs than there were 0's: this would lead to a revert, since there would be a trial to access the proof list, but it would have been already run over of elements, since there are more 0's than elements in the list:
Example:
proof = [1, 2, 4, 7]
flags = [1, 0, 0, 0, 1, 0, 0]
The `1.` would happen as soon as the flags list would check both the penultimo element in the flags list and also the penultimo element in the flags list.

2. There would be more elements in the proof list than there were 0's in the flags list. Basically, this would leave some elements in the proof list out, which would then lead to an incorrect build of the tree and also many leaves that contribute to the making of that proof would not be verified correctly, since there'd no record of them.

# Metric:
1. Understanding of the bug: 7/10