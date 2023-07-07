from typing import List


class MindMapNode:
    def __init__(self, name: str, child_nodes: "List[MindMapNode]" = None):
        if child_nodes is None:
            child_nodes = []
        self.name: str = name
        self.edges: List[MindMapEdge] = [MindMapEdge(node) for node in child_nodes]

    def add_child(self, new_child: "MindMapNode"):
        self.edges.append(MindMapEdge(new_child))

    def repr_indent_level(self, indent_level: int = 0) -> str:
        head = "\t" * indent_level + " - " + self.name + "\n"
        for edge in self.edges:
            head += edge.target.repr_indent_level(indent_level+1) + "\n"
        return head

    def __repr__(self):
        return self.repr_indent_level(0)


class MindMapEdge:
    def __init__(self, target: MindMapNode):
        self.target: MindMapNode = target
