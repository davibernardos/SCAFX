# MACHINE LEARNING TECHNIQUES
# -----------------------------------------------
import math
import matplotlib.pyplot as plt
import numpy as np
import pydotplus
import scipy
from pylab import rcParams
from scipy.cluster.hierarchy import cophenet, dendrogram, linkage, set_link_color_palette
from scipy.spatial.distance import pdist
from sklearn import metrics
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.metrics import pairwise_distances
#from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import sklearn
#%matplotlib inline

np.set_printoptions(precision=4, suppress=True)

plt.figure(figsize=(10, 3))
plt.style.use('seaborn-whitegrid')

# HIERARCHICAL CLUSTERING
# ------------------------------------------------------------
## OUTPUT: DF acrescenta uma coluna com os Cluster (GA, GB, GC...)
## ------------------------------------------------------------
def agrupador(df, features_cols, start_stud, output_cluster, num_clusters, thisMetric, thisMethod, ls_groups):
    dfx = df[df.iloc[:].sum(axis=1) == 0] 
    df = df[df.iloc[:].sum(axis=1) > 0]
    
    df.index = df.index + start_stud
    dfx.index = dfx.index + start_stud
    df.index.name = 'stud.'
    
    #define dendrogram cut line
    cutting_height = len(df) - num_clusters
    
    ## Agglomerative Hierarchical
    #------------------------------------------------------------
    #create the cluster.labels_
    cluster = AgglomerativeClustering(n_clusters=num_clusters, affinity=thisMetric, linkage=thisMethod, compute_distances=True)
    cluster.fit_predict(df) 
    
    Z = linkage(df, method=thisMethod, metric=thisMetric) 
    #labelList = range(start_stud, len(df)+start_stud) 
    labelList = df.index.tolist()
    
    c, coph_dists = cophenet(Z, pdist(df))
    cut = Z[cutting_height][2]
    
    ## Dendrogram
    #------------------------------------------------------------ 
    plt.figure(figsize=(10, 7)) #6.5, 2.5 
    plt.grid(False)
    plt.ylabel('Euclidean Distance')
    plt.xlabel('Student clustering')
    
    set_link_color_palette(["blue", "orange", "green"])    
    dendrogram(Z, orientation='top', labels=list(labelList), distance_sort='descending', 
               show_leaf_counts=True, color_threshold=cut, above_threshold_color='yellow',
               leaf_font_size=12, leaf_rotation=90)
    plt.axhline(y=cut, linestyle='--', color='r')
    plt.savefig(output_cluster, bbox_inches='tight') 
    
    print("\n>>> AGGLOMERATIVE HIERARCHICAL ({}, {})".format(thisMetric, thisMethod))
    print("Cophenetic Correlation Coefficient: {} \n{}".format(round(c,2), cluster.labels_))
    
    
    #------------------------------------------------------------
    if not 'Cluster' in df:
        df.insert(len(features_cols), 'Cluster', cluster.labels_)        
        
    #------------------------------------------------------------    
    # Está sendo utilizada a média do grupo para não prejudicar os grupos menores
    dffdp = (df.groupby(['Cluster']).mean().sum(axis=1)).sort_values(ascending=False) 

    #a,b,c,d = dffdp.index.tolist()
    
    # Um novo data frame foi criado para não ocorrer warning devido a indexação encadeada
    new_df = df.copy()
    
    for (group, ordem) in zip(ls_groups, dffdp.index.tolist()):
        new_df.loc[new_df['Cluster'] == ordem, "Cluster"] = group

    #------------------------------------------------------------
    return (new_df, dfx, round(c,2))



# DECISION TREE
# ------------------------------------------------------------
def classificador(df, features_cols, output_tree, printador, ls_groups):
    clf = DecisionTreeClassifier(max_depth=None, random_state=0, criterion='entropy')
    clf.fit(df[features_cols], df['Cluster'])
    
    dot_data = tree.export_graphviz(clf, feature_names = features_cols, class_names = ls_groups, out_file=None,
                                    filled = True, rounded = False, special_characters=True)
    
    graph = pydotplus.graph_from_dot_data(dot_data)
    nodes = graph.get_node_list()
    colors =  ('yellow', 'orange', 'green', 'lightblue', 'pink')
    
    for node in nodes:
        if node.get_name() not in ('node', 'edge'):
            values = clf.tree_.value[int(node.get_name())][0]
            #color only nodes where only one class is present
            if max(values) == sum(values):    
                node.set_fillcolor(colors[np.argmax(values)])
            #mixed nodes get the default color
            else:
                #node.set_fillcolor(colors[np.argmax(values)])
                node.set_fillcolor("white")
                
    graph.write_png(output_tree)
    
    #?print("Accuracy: {}".format(round(score, 3)))