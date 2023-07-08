from typing import List, Tuple, Set

from mind_map import MindMapNode, MindMapEdge


class MapBuilder:
    """
    MapBuilder

    This class is responsible with converting a list of ranked keywords and a list of keyword relationships into a map.
    """

    def __init__(self):
        pass

    def __call__(self, keywords: List[str], relationships: Set[Tuple[str, str]]) -> List[MindMapNode]:
        return self.make_maps(keywords, relationships)

    def make_maps(self, keywords: List[str], relationships: Set[Tuple[str, str]]) -> List[MindMapNode]:
        """
        make_maps

        Returns a minimal list of maps which together contain all the keywords in a list linked by all the relationships in the list.

        :param keywords: List of keywords in descending order of significance
        :param relationships: List of possible relationships of keywords
        :return: List of finished maps
        """
        mind_maps = []

        while len(keywords) != 0:
            headNode = MindMapNode(keywords.pop(0))
            nodesToFill = [headNode]
            while len(nodesToFill) > 0:
                nodeToFill = nodesToFill.pop(0)
                subNodes = MapBuilder.fillNode(nodeToFill, keywords, relationships)
                for subNode in subNodes:
                    keywords.remove(subNode.name)
                nodesToFill += subNodes

            mind_maps.append(headNode)

        return mind_maps

    @staticmethod
    def fillNode(nodeToFill: MindMapNode,
                 keywords: List[str],
                 relationships: Set[Tuple[str, str]]) -> List[MindMapNode]:
        subKeywords = [
            keyword for keyword in keywords
            if MapBuilder._has_relationship(relationships, keyword, nodeToFill.name)
        ]

        subNodes = [MindMapNode(kw) for kw in subKeywords]

        for subNode in subNodes:
            nodeToFill.add_child(subNode)

        return subNodes

    @staticmethod
    def _has_relationship(relationships: Set[Tuple[str, str]], keywordA: str, keywordB):
        return (keywordA, keywordB) in relationships or (keywordB, keywordA) in relationships
