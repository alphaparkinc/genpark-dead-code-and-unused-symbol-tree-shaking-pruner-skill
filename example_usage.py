"""Example usage for Dead Code Tree Pruner."""
from client import DeadCodeTreePruner

if __name__ == "__main__":
    code = """
def useful(): return 1
def dead(): return 2
def main(): print(useful())
"""
    res = DeadCodeTreePruner.prune_unreferenced_symbols(code)
    print("Unused Functions:", res["unused_functions"])
