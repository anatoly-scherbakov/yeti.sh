"""Check absolute imports against this fixture's YAML-LD layer boundary."""
import ast
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parent


def imports(source):
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            yield from (alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                raise ValueError("The fixture uses absolute imports")
            if node.module:
                yield node.module
                yield from (node.module + "." + alias.name for alias in node.names)


def violations(source, forbidden):
    return sorted({
        name for name in imports(source)
        if name == forbidden
        or name.startswith(forbidden + ".")
    })


def check():
    graph = yaml.safe_load((ROOT / "invoice-export.yamlld").read_text())["$included"]
    nodes = {node["$id"]: node for node in graph}
    rule = nodes["RepositoryBoundary"]
    source = nodes[rule["sourceLayer"]]["modulePrefix"]
    forbidden = nodes[rule["forbiddenTargetLayer"]]["modulePrefix"]
    path = ROOT.joinpath(*source.split(".")).with_suffix(".py")
    found = violations(path.read_text(), forbidden)
    if found:
        print(f"FAIL {source}: forbidden imports {found}")
        return 1
    print(f"PASS {source}: boundary respected")
    return 0


if __name__ == "__main__":
    sys.exit(check())
