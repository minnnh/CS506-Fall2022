from collections import defaultdict
from math import inf
from sim import euclidean_dist, manhattan_dist, jaccard_dist, cosine_sim
from read import read_csv
import random
import csv


def get_centroid(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    [p1,p2,p3]
    #p = len(points)
    #d = len(p)
    
    x,y=zip(*points)
    center=(max(x)+min(x))/2., (max(y)+min(y))/2.
    """
    p = len(points) # the number of the points
    d = len(points[0]) # the dimensions of the points
    
    center = [0] * (d)

    for i in range(p):
        for j in range(d):
            center[j] += points[i][j]
    
    for n in range(len(center)):
        center[n] = center[n] / 2
    
    return tuple(center)

    #raise NotImplementedError()


    
    

def get_centroids(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the centroid for each of the assigned groups.
    Return `k` centroids in a list
    """

    centroid = points.sample(1)
    return centroid

    #raise NotImplementedError()


def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    raise NotImplementedError()


def distance_squared(a, b):
    raise NotImplementedError()


def cost_function(clustering):
    raise NotImplementedError()


def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    raise NotImplementedError()


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    raise NotImplementedError()


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = get_centroids(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
