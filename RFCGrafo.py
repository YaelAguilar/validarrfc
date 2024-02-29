import re
import networkx as nx
import matplotlib.pyplot as plt

entrada_usuario = input("Ingrese una cadena: ")

def draw_graph(expression, graph_name):
    G = nx.DiGraph()
    entrada_con_c = 'c' + entrada_usuario[1:]
    if expression.match(entrada_con_c):
        nodes = set(re.findall('[a-zA-Z]', entrada_con_c))
        G.add_nodes_from(nodes)

        for i in range(len(entrada_con_c) - 1):
            G.add_edge(entrada_con_c[i], entrada_con_c[i + 1], label=entrada_con_c[i] + '->' + entrada_con_c[i + 1])

        pos = nx.shell_layout(G)
        
        nx.draw_networkx_nodes(G, pos, nodelist=[entrada_con_c[0]], node_shape='^', node_color='yellow', node_size=1000)
        
        nx.draw_networkx_nodes(G, pos, nodelist=[entrada_con_c[-1]], node_shape='o', node_color='yellow', node_size=1000, linewidths=2, edgecolors='black')
        
        nx.draw_networkx_nodes(G, pos, nodelist=list(set(G.nodes()) - set([entrada_con_c[0], entrada_con_c[-1]])), node_color='yellow', node_size=1000)
        
        nx.draw(G, pos, with_labels=False, font_weight='bold', node_color='yellow', font_color='black', arrows=True, connectionstyle='arc3,rad=0.1', edgecolors='k', node_size=1000)
        edge_labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

        labels = {node: f'q{i}' for i, node in enumerate(sorted(G.nodes()))}
        nx.draw_networkx_labels(G, pos, labels, font_color='black')

        plt.title(graph_name)
        plt.legend()
        plt.show()

# Definir las expresiones regulares
expresion_regular_1 = re.compile(r'^(c(u(a(y)?)?)?)?$', re.IGNORECASE)
expresion_regular_2 = re.compile(r'^C(uay)*$', re.IGNORECASE)
expresion_regular_3 = re.compile(r'^C(?=.*u)(?=.*a)(?=.*y)(?!.*(.).*\1)[uay]+$', re.IGNORECASE)

# Generar gráficos para cada expresión
draw_graph(expresion_regular_1, "Grafo para la Primera Expresion")
draw_graph(expresion_regular_2, "Grafo para la Segunda Expresion")
draw_graph(expresion_regular_3, "Grafo para la Tercera Expresion")
