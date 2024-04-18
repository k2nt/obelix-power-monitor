import re


def is_node_name(s: str) -> bool:
    return bool(re.match(r"^obelix\d+$", s))
