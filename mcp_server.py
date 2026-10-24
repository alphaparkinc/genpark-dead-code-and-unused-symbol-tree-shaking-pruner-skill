"""MCP server for Dead Code Tree Pruner."""
import sys
import json
from client import DeadCodeTreePruner

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "detect_dead_symbols",
                "description": "Scans Python AST for unreferenced function declarations and dead code",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "source_code": {"type": "string"}
                    },
                    "required": ["source_code"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "detect_dead_symbols":
            code = params.get("arguments", {}).get("source_code", "")
            res = DeadCodeTreePruner.prune_unreferenced_symbols(code)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
