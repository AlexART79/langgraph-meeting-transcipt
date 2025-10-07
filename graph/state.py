from typing import List, Dict, TypedDict, Annotated, Optional

def merge_dicts(existing: dict, new: dict) -> dict:
    """Merges two dictionaries. The new dict overrides existing keys."""
    merged = existing.copy() if existing else {}
    merged.update(new)
    return merged

def keep_last(existing: Optional[str], new: Optional[str]) -> Optional[str]:
    """Last-wins: overwrite with the latest concurrent update."""
    return new if new is not None else existing

class State(TypedDict):
    file_path: Annotated[str, keep_last]
    docs: Annotated[List[str], keep_last]
    generation: Annotated[Dict[str, str], merge_dicts]