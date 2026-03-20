from problems.p035_serialize_and_deserialize_binary_tree import (
    solution, TreeNode, build_tree_from_list, tree_to_list,
)


def _roundtrip(values):
    """Build tree, serialize, deserialize, convert back to list."""
    codec = solution()
    root = build_tree_from_list(values)
    data = codec.serialize(root)
    reconstructed = codec.deserialize(data)
    return tree_to_list(reconstructed)


TEST_CASES = [
    {
        "description": "Tree [1,2,3,None,None,4,5] roundtrip",
        "run": lambda: _roundtrip([1, 2, 3, None, None, 4, 5]),
        "expected": [1, 2, 3, None, None, 4, 5],
    },
    {
        "description": "Empty tree roundtrip",
        "run": lambda: _roundtrip([]),
        "expected": [],
    },
    {
        "description": "Single node [1] roundtrip",
        "run": lambda: _roundtrip([1]),
        "expected": [1],
    },
]
