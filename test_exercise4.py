from exercise4 import gc_blocks, gc_map
import numpy as np

def test_gc_blocks():
    assert gc_blocks('', 10) == tuple()
    assert gc_blocks('gcgcgcgcg', 10) == tuple()
    assert gc_blocks('gcgcgcg', 4) == (1.0,)
    assert gc_blocks('gcgcgcgcat', 4) == (1.0, 1.0)

    test_tuple = gc_blocks('gcgcgcgcat', 4)
    assert np.isclose(test_tuple[0], 0.75) and test_tuple[1] == 1

test_gc_blocks()