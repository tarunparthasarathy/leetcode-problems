#  Homework 16 - Graph Traversal

import collections

# Helper Data Structures and Algorithms

class Graph:
    def __init__(self):
        self.storage = {}

    def add_vertex(self, id):
        if id not in self.storage:
            self.storage[id] = []
            return True
        else:
            return False

    def remove_vertex(self, id):
        if id not in self.storage:
            return False

        for vertex in self.storage:
            edges = self.storage[vertex]
            if id in edges:
                edges.remove(id)

        del self.storage[id]
        return True

    def add_edge(self, id1, id2):
        if id1 not in self.storage or id2 not in self.storage:
            return False
        if id2 in self.storage[id1]:
            return False
        self.storage[id1].append(id2)
        return True

    def remove_edge(self, id1, id2):
        if id1 in self.storage:
            if id2 in self.storage[id1]:
                self.storage[id1].remove(id2)
                return True
        return False

    def is_vertex(self, id):
        return id in self.storage

    def neighbors(self, id):
        if id in self.storage:
            return self.storage[id]
        return None

    def vertices(self):
        return [key for (key,value) in self.storage.items()]

def generate_adjacency_list(edges):
    """
    Helper method to generate an adjacency list from a list of edges.
    """
    graph = Graph()
    for edge in edges:
        start = edge[0]
        end = edge[1]
        graph.add_vertex(start)
        graph.add_vertex(end)
        graph.add_edge(start, end)
    return graph


def topological_sort(graph):
    """
    Helper method to perform topological sort on graph.
    """
    visited = set()
    results = []

    def dfs(current):
        if current in visited:
            return
        visited.add(current)
        neighbors = graph.neighbors(current)
        for neighbor in neighbors:
            dfs(neighbor)
        results.append(current)

    for node in graph.vertices():
        dfs(node)

    return list(reversed(results))



# Predict Order


# Practice visualizing the order of traversal for each of the following
# graphs. Write a valid ordering if
#     1) BFS
#     2) DFS (pre-order)
#     3) topological sort are performed.
# The starting vertex for BFS and DFS is vertex 0

# Graph A:
#      1) BFS: [0, 1, 2, 3, 4, 5]
#      2) DFS: [0, 2, 3, 4, 5, 1]
#      3) Topological Sort: [0, 1, 3, 2, 4, 5]
#
#
# Graph B:
#      1) BFS: [0, 1, 2, 3, 4]
#      2) DFS: [0, 1, 3, 4]
#      3) Topological Sort: [5, 0, 2, 1, 4, 3]
#
#
# Graph C:
#      1) BFS: [1, 3, 2, 4, 5, 6, 7]
#      2) DFS: [1, 3, 2, 4, 7, 6, 5]
#      3) Topological Sort: [0, 1, 3, 4, 5, 7, 6, 2]


#
#  Predict Order
#
#  Practice visualizing the order of traversal for each of the following
#  graphs. Write a valid ordering if 1) BFS, 2) DFS (pre-order), and
#  3) topological sort is performed. The starting vertex for BFS and DFS
#  is vertex 0
#
#  There are no tests for this particular problem. Additionally, for some of
#  these graphs, there are multiple possible solutions
#
#
#
#  Graph A: https://res.cloudinary.com/outco/image/upload/v1519855558/graph-traversal/Paper.Graph_Traversal.10.png
#
#  1) BFS: {0,1,2,3,4,5}
#  2) DFS: {0,1,3,4,5,2}
#  3) Topological sort: {0,2,1,3,4,5}
#
#  Graph B: https://res.cloudinary.com/outco/image/upload/v1519855554/graph-traversal/Paper.Graph_Traversal.11.png
#
#  1) BFS: {0,1,2,4,3}
#  2) DFS: {0,1,3,4,2}
#  3) Topological sort: {0,2,1,3,5,4}
#
#  Graph C: https://res.cloudinary.com/outco/image/upload/v1519855557/graph-traversal/Paper.Graph_Traversal.12.png
#
#  1) BFS: {0,1,2,3,4,5,6,7}
#  2) DFS: {0,2,4,5,7,6,1,3}
#  3) Topological sort: {0,1,3,2,4,6,5,7}
#


#
#  Redundant Connection
#
#  Given a directed graph (list of edges), where if one of the edges is
#  removed, the graph will become a tree.  Return that edge.
#
#  Parameters:
#
#  Input: edges: [[Integer]]
#  Output: [Integer]
#
#  Examples:
#
# `{{1, 2}, {1, 3}, {2, 3}} --> {2, 3}`
# `{{1, 2}, {2, 3}, {2, 4}, {4, 5}, {5, 2}} --> {5, 2}`
#
#  Note:
#  - For some inputs, there coule be multiple
#    correct solutions
#
#  Resources:
#  - https://leetcode.com/problems/redundant-connection-ii/description/
#


def redundant_connection(edges):
    N = len(edges)
    parent = {}
    candidates = []
    for u, v in edges:
        if v in parent:
            candidates.append([parent[v], v])
            candidates.append([u, v])
        else:
            parent[v] = u

    def orbit(node):
        seen = set()
        while node in parent and node not in seen:
            seen.add(node)
            node = parent[node]
        return node, seen

    root = orbit(1)[0]

    if not candidates:
        cycle = orbit(root)[1]
        for u, v in edges:
            if u in cycle and v in cycle:
                ans = [u, v]
        return ans

    children = collections.defaultdict(list)
    for v in parent:
        children[parent[v]].append(v)

    seen = [True] + [False] * N
    stack = [root]
    while stack:
        node = stack.pop()
        if not seen[node]:
            seen[node] = True
            stack.extend(children[node])

    return candidates[all(seen)]


# Third Degree Neighbors
#
# Given an undirected graph represented by a list of edges and a start vertex, return an array of the 3rd degree neighbors.
# Parameters:
#
# Input: edges: [[Integer]]
# Input: start: Integer
# Output: [Integer]
#
# Examples:
#
# The following example with start vertex `1`:
# input:
#              9
#            /
# 1 -- 2   8
# |    | /   \
# 3 -- 4      7
#        \  /  \
#          5 -- 6
#
# output: [5, 8]

def third_degree_neighbors(edges, start):

    graph = generate_adjacency_list(edges)

    result = []
    queue = collections.deque()
    seen = set()

    seen.add(start)
    queue.append([start, 0])

    while len(queue) > 0:
        current, degree = queue.popleft()
        if degree == 3:
            result.append(current)
            continue
        neighbors = graph.neighbors(current)
        for neighbor in neighbors:
            if neighbor not in seen:
                queue.append([neighbor, degree + 1])
                seen.add(neighbor)

    return result

# Detect Cycle in Graph (Undirected)
# Given edges that represent an undirected graph, determine if the graph has a cycle.
# A cycle has a minimum of 3 vertices.

# Parameters:
# Input: edges: [[Integer]]
# Output: Boolean

# Example:

# Input: [[1, 2], [2, 1], [2, 3], [3, 2], [3, 1], [1, 3],
#         [3, 4], [4, 3], [5, 4], [5, 6], [6, 5], [5, 7],
#         [7, 5], [6, 7], [7, 6], [8, 7], [8, 9], [9, 8]]

#                 9
#               /
    graph = generate_adjacency_list(edges)
    seen = set()
    queue = collections.deque()

    vertices = graph.vertices()
    for vertex in vertices:
        if vertex not in seen:
            seen.add(vertex)
            queue.append(vertex)

    while(len(queue) > 0):
        current = queue.popleft()
        neighbors = graph.neighbors(current)
        neighbors_visited = 0
        flag = False
        for neighbor in neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
            else:
                neighbors_visited += 1
            if neighbors_visited > 1:
                flag = True
            if flag is True:
                return flag

    return False

#
#  Friend Circles
#
#  A friend circle is a group of people who are direct or indirect friends.
#  Given a NxN bitset matrix, where a 1 in the i,j coordinate signifies a
#  friendship between person i and person j, determine how many circles of
#  friends there are.
#
#  Parameters:
#
#  Input: Graph: [[Integer]] (adjacency matrix)
#  Output: Integer
#
#  Example:
#
#  Input: `[[1,1,0], [1,1,0], [0,0,1]]`
#  Output: 2
#
#  Input: `[[1,1,0], [1,1,1], [0,1,1]]`
#  Output: 1
#
#  Resources:
#  - https://leetcode.com/problems/friend-circles/description/
#
#

def friend_circles(matrix):
    seen = set()
    circles = 0
    queue = collections.deque()

    for row in range(len(matrix)):
        person = row

        if person not in seen:
            queue.append(person)
            seen.add(person)
            circles += 1
        while queue:
            current = queue.popleft()
            for friend in range(len(matrix[row])):
                if matrix[current][friend] == 1 and friend not in seen:
                    seen.add(friend)
                    queue.append(friend)

    return circles


# Longest Path I
# Given a DAG (directed acyclic graph), find the longest path in the graph

# Parameters:

# Input: Graph: [[Integer]] (adjacency matrix)
# Output: Integer

# Example:

# Input: [[1, 2], [2, 3], [1, 3]]
# Output: [1, 2, 3]

# Input: [[6, 5], [6, 4], [5, 4], [4, 3], [2, 3], [1, 2], [4, 1]]
# Output: [6, 5, 4, 1, 2, 3]

def longest_path_1(edges):
    graph = generate_adjacency_list(edges)
    visited = set()
    longest_path_1.result = []

    def dfs(current, path):
        if current in visited:
            return
        if len(path) > len(longest_path_1.result):
            longest_path_1.result = path[:]

        visited.add(current)
        neighbors = graph.neighbors(current)
        for neighbor in neighbors:
            path.append(neighbor)
            dfs(neighbor, path)
            path.pop()

        visited.remove(current)

    vertices = graph.vertices()

    for vertex in vertices:
        dfs(vertex, [vertex])

    return longest_path_1.result



# Course Schedule

# A collection of courses at a University has prerequisite courses that must be taken first. Given an
# array of course pairs [a, B] where A is the prerequisite of B, determine a valid sequence of courses
# a student can take to complete all the courses

# Parameters
# Input: courses [[String]]
# Output: [String]

# Examples
# [[a, b], [a, c], [b, d], [c, d]] --> [a, b, c, d] || [a, c, b, d]
#
#  Course Schedule
#
#  A collection of courses at a University has prerequisite courses that must
#  be taken first.  Given an array of course pairs [A, B] where A is the
#  prerequisite of B, determine a valid sequence of courses a student can
#  take to complete all the courses.
#
#  Parameters:
#
#  Input: courses: [[String]]
#  Output: [String]
#
#  Example:
#
#  Input: [["a","b"],["a","c"],["b","d"],["c","d"]]
#  Output: ["a","b","c","d"] or ["a","c","b","d"]
#
#  Input: [["a","b"],["b","c"],["c","d"]]
#  Output: ["a","b","c","d"]




def course_schedule(course_list):
    graph = generate_adjacency_list(course_list)
    return topological_sort(graph)


#
#  Cryptic Dictionary
#
#  An array of strings in lexicographical (alphabetical) order has been put
#  through a [simple substitution cypher](https://en.wikipedia.org/wiki/Substitution_cipher)
#  where each letter is now substituted for another letter. Determine a valid
#  ordering of characters in the cypher.
#
#  Parameters:
#
#  Input: words: [String]
#  Output: [String]
#
#  Example:
#
#  Input: ["baa", "abcd", "abca", "cab", "cad"]
#  Output: ["b", "d", "a", "c"]
#
#  Input: ["caa", "aaa", "aab"]
#  Output: ["c", "a", "b"]
#
#

def cryptic_dictionary(words):
    def first_letter_difference(word1, word2):
        for letter in range(min(len(word1), len(word2))):
            if word1[letter] != word2[letter]:
                return [word1[letter], word2[letter]]

    edges = []
    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]
        if first_letter_difference(word, next_word) is not None:
            edges.append(first_letter_difference(word, next_word))
    graph = generate_adjacency_list(edges)
    return topological_sort(graph)




# ###########################################################
# ##############  DO NOT TOUCH TEST BELOW!!!  ###############
# ###########################################################

# custom expect function to handle tests
# List count : keeps track out how many tests pass and how many total
#   in the form of a two item array i.e., [0, 0]
# String name : describes the test
# Function test : performs a set of operations and returns a boolean
#   indicating if test passed
def expect(count, name, test):
  if(count == None or not isinstance(count, list) or len(count) != 2):
    count = [0, 0]
  else:
    count[1] += 1


  result = 'false'
  errMsg = None
  try:
    if test():
      result = ' true'
      count[0] += 1
  except Exception as err:
    errMsg = str(err)

  print('  ' + (str(count[1]) + ')   ') + result + ' : ' + name)
  if errMsg != None:
    print('       ' + errMsg + '\n')

# code for capturing print output
#
# directions: capture_print function returns a list of all elements that were
#             printed using print with the function that it is given. Note that
#             the function given to capture_print must be fed using lambda.
#             Example cis provided below

from io import StringIO
import sys
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout


def capture_print(toRun):
  with Capturing() as output:
    pass
  with Capturing(output) as output:  # note the constructor argument
    toRun()
  return output


print('Redundant Connection Tests')
test_count = [0, 0]

def test():
  example = redundant_connection([[1, 2], [1, 3], [2, 3]])
  return example is not None and example == [2, 3] or example == [1, 3]

expect(test_count, "should work when one node has two parents, but there is no cycle", test)


def test():
    example = redundant_connection([[1, 2], [2, 3], [2, 4], [4, 5], [5, 2]])
    return example is not None and example == [5, 2]

expect(test_count, "should work when one node has two parents, and there is a cycle", test)

def test():
    example = redundant_connection([[1,2],[2,3],[3,1]])
    return example is not None and example == [1, 2] or example == [2, 3] or example == [3, 1]

expect(test_count, "should work when there is a cycle, but no node has two parents", test)

def test():
    example = redundant_connection([[1,2],[2,3],[3,1],[3,6],[2,5],[1,4]])
    return example is not None and example == [1, 2] or example == [2, 3] or example == [3, 1]

expect(test_count, "should work when there is a cycle, and other nodes not in the cycle", test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

print("Third Degree Neighbors")
test_count = [0, 0]


def test():
    edges = [[1,2],[2,1],[1,3],[3,1],[2,4],[4,2],[3,4],[4,3],[4,8],[8,4],[4,5],[5,4],[5,6],[6,5],[5,7],[7,5],[6,7],[7,6],[8,7],[7,8],[8,9],[9,8]]
    example = third_degree_neighbors(edges, 1)
    return example is not None and example == [5, 8] or example == [8, 5]

expect(test_count, "should work on a linear example input", test)

def test():
    edges = [[1, 1]]
    example = third_degree_neighbors(edges, 1)
    return example is not None and example == []

expect(test_count, "should work on a graph with one vertex", test)


def test():
    edges = [[1,2],[2,1],[2,3],[3,2],[3,4],[4,3],[3,5],[5,3],[3,6],[6,3],[1,7],[7,1],[7,8],[8,7],[8,9],[9,8],
             [8,10],[10,8],[8,11],[11,8]]
    example = third_degree_neighbors(edges, 1)
    return example is not None and example == [4,5,6,9,10,11]

expect(test_count, "should work with multiple third degree neighbors", test)

def test():
    edges = [[1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3],[4, 5], [5, 4], [5, 6], [6, 5], [6, 1], [1, 6]]
    example = third_degree_neighbors(edges, 1)
    return example is not None and example == [4]

expect(test_count, "should work on a small cycle", test)

def test():
    edges = [[1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 1], [1, 8]]
    example = third_degree_neighbors(edges, 1)
    return example is not None and example == [4,6]

expect(test_count, "should work on a large cycle", test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

print("Detect Cycle Tests")
test_count = [0, 0]

def test():
    example = detect_cycle_in_graph([[1, 2], [2, 1], [2, 3], [3, 2], [3, 1], [1, 3]])
    return example is True

expect(test_count, "should work on a first example input", test)

def test():
    example = detect_cycle_in_graph([[1, 2], [2, 1], [2, 3], [3, 2], [3, 1], [1, 3],[3, 4], [4, 3],
                                   [5, 4], [4, 5], [5, 6], [6, 5],[4, 7], [7, 4]])
    return example is True

expect(test_count, "should work on second example input", test)

def test():
    example = detect_cycle_in_graph([[1, 2], [2, 1], [1, 3], [3, 1], [3, 4], [4, 3],
           [4, 5], [5, 4], [5, 6], [6, 5], [4, 7], [7, 4]])
    return example is True

expect(test_count, "should work on third example input", test)

def test():
    example = detect_cycle_in_graph([])
    return example is False

expect(test_count, "should work on empty input", test)

def test():
    example = detect_cycle_in_graph([[1, 2], [2, 1], [1, 3], [3, 1], [3, 5], [5, 3],
                                     [5, 6], [6, 5], [6, 4], [4, 6], [4, 2], [2, 4]])
    return example is True

expect(test_count, "should work on fifth example input", test)

def test():
    example = detect_cycle_in_graph([[1, 1]])
    return example is False

expect(test_count, "should work on a single vertex", test)

def test():
    example = detect_cycle_in_graph([[1, 2], [2, 1]])
    return example is False

expect(test_count, "should work on two vertices", test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print("Friend Circles")
test_count = [0, 0]

def test():
    matrix = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    example = friend_circles(matrix)
    return example is not None and example == 2

expect(test_count, "should work on first example case", test)

def test():
    matrix = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    example = friend_circles(matrix)
    return example is not None and example == 1

expect(test_count, "should work on second example case", test)

def test():
    matrix = []
    example = friend_circles(matrix)
    return example is not None and example == 0

expect(test_count, "should work on empty matrix", test)

def test():
    matrix = [[1]]
    example = friend_circles(matrix)
    return example is not None and example == 1

expect(test_count, "should work on a single person", test)

def test():
    matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    example = friend_circles(matrix)
    return example is not None and example == 4

expect(test_count, "should work when no one is friends with anyone else", test)

def test():
    matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    example = friend_circles(matrix)
    return example is not None and example == 1

expect(test_count, "should work when everyone is friends with everyone else", test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print("Longest Path I")
test_count = [0, 0]

def test():
    example = longest_path_1([[1, 2], [2, 3], [1, 3]])
    return example == [1, 2, 3]

expect(test_count, "should work for first example case", test)

def test():
    example = longest_path_1([[6, 5], [6, 4], [5, 4], [4, 3], [2, 3], [1, 2], [4, 1]])
    return example == [6, 5, 4, 1, 2, 3]

expect(test_count, "should work for second example case", test)

def test():
    example = longest_path_1([[2, 3], [3, 1]])
    return example == [2, 3, 1]

expect(test_count, "should work for three element linear graph", test)

def test():
    example = longest_path_1([[1, 2], [2, 4], [4, 6], [1, 3], [3, 5], [5, 7]])
    return example == [1, 2, 4, 6] or example == [1, 3, 5, 7]

expect(test_count, "should work for graph with two equivalent paths", test)

def test():
    example = longest_path_1([[1, 1]])
    return example == [1]

expect(test_count, "should work for single element graph", test)

def test():
    example = longest_path_1([[1, 2], [1, 3], [1, 4], [1, 5]])
    return example == [1, 2] or example == [1, 3] or example == [1, 4] or example == [1, 5]

expect(test_count, "should handle graph with multiple paths equivalent in length", test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

print("Course Schedule")
test_count = [0, 0]

def test():
    course_list = [['a', 'b'], ['a', 'c'], ['b', 'd'], ['c', 'd']]
    example = course_schedule(course_list)
    return example is not None and example == ['a', 'b', 'c', 'd'] or example == ['a', 'c', 'b', 'd']

expect(test_count, "should work on first example", test)

def test():
    course_list = [['a', 'b'], ['b', 'c'], ['c', 'd']]
    example = course_schedule(course_list)
    return example is not None and example == ['a', 'b', 'c', 'd']

expect(test_count, "should work on second example", test)

def test():
    course_list = [['a', 'c'], ['a', 'b']]
    example = course_schedule(course_list)
    return example is not None and example == ['a', 'c', 'b'] or example == ['a', 'b', 'c']

expect(test_count, "should work on third example", test)

def test():
    course_list = [["a","b"],["a","c"],["b","d"],["d","e"],["d","c"],["c","e"],["e","f"],["f","h"],["e","h"],["e","g"],["h","g"]]
    example = course_schedule(course_list)
    return example is not None and example == ['a', 'b', 'd', 'c', 'e', 'f', 'h', 'g']

expect(test_count, "should work on fourth example", test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print("Cryptic Dictionary")
test_count = [0, 0]

def test():
    sorted_words = ['baa', 'abcd', 'abca', 'cab', 'cad']
    example = cryptic_dictionary(sorted_words)
    return example is not None and example == ["b", "d", "a", "c"]

expect(test_count, "should work on first example", test)


def test():
    sorted_words = ["caa", "aaa", "aab"]
    example = cryptic_dictionary(sorted_words)
    return example is not None and example == ["c", "a", "b"]

expect(test_count, "should work on second example", test)

def test():
    sorted_words = ['bbb', 'bab']
    example = cryptic_dictionary(sorted_words)
    return example is not None and example == ["b", "a"]

expect(test_count, "should work on third exmaple", test)

def test():
    sorted_words = ['bm','bn','bo','mo']
    example = cryptic_dictionary(sorted_words)
    return example is not None and example == ['b','m','n','o']

expect(test_count, "should work on fourth example", test)


print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')
