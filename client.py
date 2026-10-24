"""Dead Code & Unused Symbol Tree-Shaking Pruner.
100% Python Standard Library.
"""

import ast

class DeadCodeTreePruner:
    """Analyzes declared functions vs call sites to detect unreachable dead code."""

    @staticmethod
    def prune_unreferenced_symbols(source_code: str) -> dict:
        tree = ast.parse(source_code)
        declared_funcs = set()
        called_funcs = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and not node.name.startswith("_") and node.name != "main":
                declared_funcs.add(node.name)
            elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                called_funcs.add(node.func.id)

        unused = declared_funcs - called_funcs
        return {
            "declared_functions": sorted(list(declared_funcs)),
            "called_functions": sorted(list(called_funcs)),
            "unused_functions": sorted(list(unused)),
            "pruning_candidate_count": len(unused)
        }
