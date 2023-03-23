## Importando os componentes necessários
import networkx as nx
from matplotlib import pyplot as plt
## Para textos em Latex
#plt.rcParams.update({
#    "text.usetex": True,
#    "font.family": "sans-serif",
#    "font.sans-serif": ["Helvetica"]})
# for Palatino and other serif fonts use:
#plt.rcParams.update({
#    "text.usetex": True,
#    "font.family": "serif",
#    "font.serif": ["Palatino"],
#})
## Fazendo o gráfico e os paths
g1 = nx.DiGraph()
g1.add_edges_from([("$P$", "$Q$"), ("$P$", "$D_{t_{1}}$"),("$P$", "$D_{t_{2}}$") , ("$D_{t_{2}}$", "$Q$"), ("$F$", "$P$"), ("$F$", "$Q$"), ("$F$", "$D_{t_{1}}$"),("$F$", "$D_{t_{2}}$"), ("$D_{t_{1}}$", "$Q$"), ("$D_{t_{2}}$", "$Q$"),("$D_{t_{1}}$", "$D_{t_{2}}$")])
plt.tight_layout()
#para layout
pos = nx.spring_layout(g1)
nx.draw_networkx_edges(g1, pos,arrows = True , width = 1.6, connectionstyle="arc3, rad=1.2", edgelist=[("$F$", "$D_{t_{2}}$")])
nx.draw_networkx(g1, pos, arrows = True, node_color = '#ff6700',  node_shape = 'o', node_size = 900, width = 1.6, edgelist=[("$P$", "$Q$"), ("$P$", "$D_{t_{1}}$"),("$P$", "$D_{t_{2}}$") , ("$D_{t_{2}}$", "$Q$"), ("$F$", "$P$"), ("$F$", "$Q$"), ("$F$", "$D_{t_{1}}$"), ("$D_{t_{1}}$", "$Q$"), ("$D_{t_{2}}$", "$Q$"),("$D_{t_{1}}$", "$D_{t_{2}}$")])
plt.savefig("dag1.svg", format="SVG")
# tell matplotlib you're done with the plot: https://stackoverflow.com/questions/741877/how-do-i-tell-matplotlib-that-i-am-done-with-a-plot
plt.clf()

## testando para ver se os paths formam um caso não cíclico
# para ver se ele é direto (deve retornar true)
nx.is_directed(g1)
# para ver se ele é acíclico (deve retornar true)
nx.is_directed_acyclic_graph(g1)
