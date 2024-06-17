import numpy as np
import pandas as pd
from scipy.spatial import Delaunay


def add_annotaion(adata):
    celltypes = pd.read_csv("annotation/W_cell_density.csv", index_col=0)
    gc_annotation = pd.read_csv("annotation/manual_GC_annot.csv", index_col=0).fillna(0).replace("GC", 1)
    obs_names = np.intersect1d(celltypes.index, adata.obs_names)
    
    adata = adata[obs_names]
    celltypes = celltypes.loc[obs_names]
    gc_annotation = gc_annotation.loc[obs_names]
    
    adata.obsm['celltype'] = celltypes
    adata.obsm['celltype'].columns = [x.replace('mean_spot_factors','') for x in adata.obsm['celltype'].columns]
    adata.obsm['celltype_raw'] = adata.obsm['celltype'].copy()
    adata.obsm['celltype'] = adata.obsm['celltype'].divide(adata.obsm['celltype'].sum(axis=1), axis=0)
    adata.obs['germinal_center'] = gc_annotation
    adata.obs['germinal_center'] = adata.obs['germinal_center'].map({0: "Other", 1: "GC"})
    return adata


def find_edges(adata, r=10, alpha=20, only_outer=True):
    points = np.asarray(adata[adata.obs['germinal_center']=='GC'].obsm['spatial'] * adata.uns['spatial']["V1_Human_Lymph_Node"]['scalefactors']['tissue_hires_scalef'])
    points = np.vstack((points+[-r,r], points+[-r,-r], points+[r,r], points+[r,-r]))
    assert points.shape[0] > 3, "Need at least four points"
    def add_edge(edges, i, j):
        """
        Add an edge between the i-th and j-th points,
        if not in the list already
        """
        if (i, j) in edges or (j, i) in edges:
            # already added
            assert (j, i) in edges, "Can't go twice over same directed edge right?"
            if only_outer:
                # if both neighboring triangles are in shape, it's not a boundary edge
                edges.remove((j, i))
            return
        edges.add((i, j))
    tri = Delaunay(points)
    edges = set()
    # Loop over triangles:
    # ia, ib, ic = indices of corner points of the triangle
    for ia, ib, ic in tri.simplices:
        pa = points[ia]
        pb = points[ib]
        pc = points[ic]
        # Computing radius of triangle circumcircle
        # www.mathalino.com/reviewer/derivation-of-formulas/derivation-of-formula-for-radius-of-circumcircle
        a = np.sqrt((pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2)
        b = np.sqrt((pb[0] - pc[0]) ** 2 + (pb[1] - pc[1]) ** 2)
        c = np.sqrt((pc[0] - pa[0]) ** 2 + (pc[1] - pa[1]) ** 2)
        s = (a + b + c) / 2.0
        area = np.sqrt(s * (s - a) * (s - b) * (s - c))
        circum_r = a * b * c / (4.0 * area)
        if circum_r < alpha:
            add_edge(edges, ia, ib)
            add_edge(edges, ib, ic)
            add_edge(edges, ic, ia)
    return points, edges

