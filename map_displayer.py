import networkx as nx
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('WXAgg')


from mind_map import MindMapNode

from typing import List


class MapDisplayer:
    def __init__(self):
        pass

    def display_maps(self, mind_maps: List[MindMapNode]):

        fig = plt.figure(figsize=(10, 6), dpi=100, frameon=False)
        #for i, mind_map in enumerate(mind_maps):
        #    plt.figure(i)
        #    self.display_map(mind_map)
        self.display_map(mind_maps[0])

        fig.set_size_inches(12, 6)

        plt.title("")
        plt.box(False)
        # plt.savefig("mind map", dpi=100)
        plt.show()
        return fig


    def __call__(self, mind_maps: List[MindMapNode]):
        self.display_maps(mind_maps)

    def display_map(self, mind_map: MindMapNode):
        graph = nx.DiGraph()
        node_list = mind_map.get_node_list()
        edge_list = [edge.to_nx_tuple() for edge in mind_map.get_edge_list()]

        print(node_list)
        print(edge_list)
        graph.add_nodes_from(node_list)
        graph.add_edges_from(edge_list)

        labels = {
            node: node.name
            for node in node_list
        }

        nx.draw_networkx(
            graph,
            labels=labels,
            pos=nx.spring_layout(
                graph,
                iterations=5000
            ),
            arrows=True,
            node_shape="s",
            edge_color="#1155FF",
            node_color="white",
            node_size=0
        )






