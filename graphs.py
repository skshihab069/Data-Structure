class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.edges_dict = {}
        for start, end in self.edges:
            if start in self.edges_dict:
                self.edges_dict[start].append(end)
            else:
                self.edges_dict[start] = [end]
        print("Edge dict :", self.edges_dict)


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Bangladesh", "Mumbai"),
        ("Bangladesh", "Soudi Arabia"),
        ("Mumbai", "Paris"),
        ("Paris", "India"),
        ("Paris", "Bangladesh")
    ]

    routes_edges = Graph(routes)
