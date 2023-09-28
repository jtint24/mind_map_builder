from typing import List, Tuple


class MindMapNode:
    def __init__(self, name: str, child_nodes: "List[MindMapNode]" = None):
        if child_nodes is None:
            child_nodes = []
        self.name: str = name
        self.edges: List[MindMapEdge] = [MindMapEdge(self, node) for node in child_nodes]

    def add_child(self, new_child: "MindMapNode"):
        self.edges.append(MindMapEdge(self, new_child))

    def repr_indent_level(self, indent_level: int = 0) -> str:
        head = "\t" * indent_level + " - " + self.name + "\n"
        for edge in self.edges:
            head += edge.target.repr_indent_level(indent_level+1)
        return head

    def get_node_list(self, existing_list: List["MindMapNode"] = None) -> List["MindMapNode"]:
        if existing_list is None:
            existing_list = []
        existing_list.append(self)
        for edge in self.edges:
            existing_list += edge.target.get_node_list()
        return existing_list

    def get_edge_list(self, existing_list: List["MindMapEdge"] = None) -> List["MindMapEdge"]:
        if existing_list is None:
            existing_list = []
        existing_list += self.edges
        for edge in self.edges:
            existing_list += edge.target.get_edge_list()
        return existing_list

    def __repr__(self):
        return self.repr_indent_level(0)


class MindMapEdge:
    def __init__(self, origin: MindMapNode, target: MindMapNode):
        self.origin: MindMapNode = origin
        self.target: MindMapNode = target

    def to_nx_tuple(self) -> Tuple[MindMapNode, MindMapNode]:
        return self.origin, self.target
