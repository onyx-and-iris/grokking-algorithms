# BFS DFS on rooted tree (connected acyclic graph)

The BFS example uses a queue which results in a breadth first search. When a directory is found its contents are appended to the queue to be processed later

The DFS example uses the call stack which results in a depth first search. When a directory is found it is recursively passed to files_with_extension to be processed immediately.

Note. DFS cannot be used to find the shortest path. In the mango seller example, a DFS search may have found a second or third degree
seller before a first. However, DFS may be used to find the topological sort.
