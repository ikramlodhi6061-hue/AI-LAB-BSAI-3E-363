# Tasks:
# 1. BFS and DFS
# 2. DLS and IDDFS
# 3. Weighted Graph and UCS
# ===========================================================
# ===========================================================
# ORIGINAL A-G GRAPH
# ============================================================
# IMPORTANT:
# Replace the connections below with the EXACT successor order
# from the original A-G graph in Section 3.2.

GRAPH = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": ["G"],
    "F": ["G"],
    "G": []
}
START = "A"
GOAL = "G"
# ============================================================
# TASK 1 - BFS
# ============================================================
def bfs(graph, start, goal):
    queue = [(start, [start])]
    visited = set()
    visit_order = []
    while queue:
        node, path = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        visit_order.append(node)
        # Stop when goal is processed
        if node == goal:
            return path, visit_order
        # Add successors in the supplied order
        for successor in graph.get(node, []):
            if successor not in visited:
                queue.append(
                    (successor, path + [successor])
                )
    return None, visit_order

# ============================================================
# TASK 1 - DFS
# ============================================================\
def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    visit_order = []
    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        visit_order.append(node)
        # Stop when goal is processed
        if node == goal:
            return path, visit_order
        # Reverse push so original successor order
        # is processed first by the stack
        successors = graph.get(node, [])
        for successor in reversed(successors):
            if successor not in visited:
                stack.append(
                    (successor, path + [successor])
                )
    return None, visit_order
# ============================================================
# TASK 2 - DEPTH-LIMITED SEARCH (DLS)
# ============================================================
FOUND = "FOUND"
CUTOFF = "CUTOFF"
FAILURE = "FAILURE"
def dls(graph, node, goal, limit, path=None):
    if path is None:
        path = [node]
    # Goal test
    if node == goal:
        return FOUND, path
    # Depth limit reached
    if limit == 0:
        return CUTOFF, path
    cutoff_occurred = False
    # Process successors in supplied order
    for successor in graph.get(node, []):
        # Path-local cycle check
        if successor in path:
            continue
        status, result_path = dls(
            graph,
            successor,
            goal,
            limit - 1,
            path + [successor]
        )
        if status == FOUND:
            return FOUND, result_path
        if status == CUTOFF:
            cutoff_occurred = True
    if cutoff_occurred:
        return CUTOFF, path
    return FAILURE, path
# ============================================================
# RUN DLS FOR LIMITS 1, 2, 3 AND 4
# ============================================================
def run_dls(graph, start, goal):
    print("\n" + "=" * 60)
    print("TASK 2: DEPTH-LIMITED SEARCH (DLS)")
    print("=" * 60)
    for limit in range(1, 5):
        status, path = dls(
            graph,
            start,
            goal,
            limit
        )
        print("\nDepth Limit:", limit)
        print("Status:", status)
        print("Path:", " -> ".join(path))
# ============================================================
# TASK 2 - ITERATIVE DEEPENING DEPTH-FIRST SEARCH
# ============================================================
def iddfs(graph, start, goal, max_depth=4):
    print("\n" + "=" * 60)
    print("TASK 2: ITERATIVE DEEPENING DFS (IDDFS)")
    print("=" * 60)
    for depth in range(1, max_depth + 1):
        status, path = dls(
            graph,
            start,
            goal,
            depth
        )
        print(
            f"Depth {depth}: "
            f"{status} | "
            f"Path: {' -> '.join(path)}"
        )
        if status == FOUND:
            print("\nIDDFS RESULT")
            print("Goal found at depth:", depth)
            print("Final path:", " -> ".join(path))
            return path
    print("\nGoal was not found within the given depth limits.")
    return None
# ============================================================
# TASK 3 - WEIGHTED GRAPH
# ============================================================
# IMPORTANT:
# Replace these weights with the EXACT edge weights
# given in the weighted version of the original graph.

WEIGHTS = {
    ("A", "B"): 2,
    ("A", "C"): 5,
    ("B", "D"): 2,
    ("B", "E"): 6,
    ("C", "F"): 1,
    ("D", "G"): 5,
    ("E", "G"): 1,
    ("F", "G"): 5
}
# ============================================================
# UCS - UNIFORM COST SEARCH
# ============================================================
def get_edge_cost(weights, current, successor):
    return weights.get(
        (current, successor),
        float("inf")
    )

def ucs(graph, weights, start, goal):
    # Each item:
    # (total_cost, node, path)
    frontier = [
        (0, start, [start])
    ]
    best_cost = {
        start: 0
    }
    processing_order = []
    while frontier:
        # Select lowest-cost node
        frontier.sort(
            key=lambda item: item[0]
        )
        cost, node, path = frontier.pop(0)
        # Ignore outdated entries
        if cost > best_cost.get(
            node,
            float("inf")
        ):
            continue
        processing_order.append(
            (node, cost)
        )
        # Goal test
        if node == goal:
            return (
                path,
                cost,
                processing_order
            )
        for successor in graph.get(node, []):

            # Path-local protection
            if successor in path:
                continue
            edge_cost = get_edge_cost(
                weights,
                node,
                successor
            )
            new_cost = cost + edge_cost
            if new_cost < best_cost.get(
                successor,
                float("inf")
            ):
                best_cost[successor] = new_cost
                frontier.append(
                    (
                        new_cost,
                        successor,
                        path + [successor]
                    )
                )
    return None, float("inf"), processing_order
# ============================================================
# INDEPENDENT PATH COST CALCULATION
# ============================================================
def calculate_path_cost(path, weights):
    if path is None or len(path) < 2:
        return 0
    total = 0
    for i in range(len(path) - 1):
        current = path[i]
        successor = path[i + 1]
        edge_cost = weights.get(
            (current, successor)
        )
        if edge_cost is None:
            return None
        total += edge_cost
    return total
# ============================================================
# DISPLAY TASK 1 RESULTS
# ============================================================
def run_task_1():
    print("\n" + "=" * 60)
    print("TASK 1: BFS AND DFS")
    print("=" * 60)
    # ---------------- BFS ----------------

    bfs_path, bfs_order = bfs(
        GRAPH,
        START,
        GOAL
    )
    print("\n--- BFS ---")
    print("Start:", START)
    print("Goal:", GOAL)
    print(
        "Visit / Processing Order:",
        " -> ".join(bfs_order)
    )
    if bfs_path:
        print(
            "Final Path:",
            " -> ".join(bfs_path)
        )
    else:
        print("Final Path: Goal not found")
    # ---------------- DFS ----------------
    dfs_path, dfs_order = dfs(
        GRAPH,
        START,
        GOAL
    )
    print("\n--- DFS ---")
    print("Start:", START)
    print("Goal:", GOAL)
    print(
        "Visit / Processing Order:",
        " -> ".join(dfs_order)
    )
    if dfs_path:
        print(
            "Final Path:",
            " -> ".join(dfs_path)
        )
    else:
        print("Final Path: Goal not found")
# ============================================================
# DISPLAY TASK 3 RESULTS
# ============================================================
def run_task_3():
    print("\n" + "=" * 60)
    print("TASK 3: WEIGHTED GRAPH AND UCS")
    print("=" * 60)
    # Run UCS
    path, cost, processing_order = ucs(
        GRAPH,
        WEIGHTS,
        START,
        GOAL
    )
    print("\n--- UCS RESULT ---")
    if path:
        print(
            "Minimum-Cost Path:",
            " -> ".join(path)
        )
        print(
            "UCS Returned Cost:",
            cost
        )
        # Independently calculate cost
        verified_cost = calculate_path_cost(
            path,
            WEIGHTS
        )
        print(
            "Independently Verified Cost:",
            verified_cost
        )
        if verified_cost == cost:
            print(
                "Cost Verification: PASS"
            )
        else:
            print(
                "Cost Verification: FAIL"
            )
    else:
        print(
            "No path to the goal was found."
        )
    # ---------------- Processing Order ----------------

    print("\nUCS Processing Order:")
    for node, node_cost in processing_order:
        print(
            f"{node}  -> cumulative cost = {node_cost}"
        )
# ===========================================================
# COMPARE HOPS AND COST
# ============================================================
def compare_routes():
    print("\n" + "=" * 60)
    print("ROUTE COST ANALYSIS")
    print("=" * 60)
    path, ucs_cost, _ = ucs(
        GRAPH,
        WEIGHTS,
        START,
        GOAL
    )
    if path:
        hops = len(path) - 1
        print(
            "UCS Path:",
            " -> ".join(path)
        )
        print(
            "Number of Hops:",
            hops
        )
        print(
            "Total Cost:",
            ucs_cost
        )
        print(
            "\nExplanation:"
        )
        print(
            "UCS minimizes TOTAL EDGE COST, "
            "not the number of edges."
        )
        print(
            "Therefore, a route with fewer hops "
            "can still cost more if its edge weights "
            "are higher."
        )
# ============================================================
# PRINT WEIGHTED EDGES
# ============================================================
def display_weighted_graph():
    print("\n" + "=" * 60)
    print("WEIGHTED GRAPH EDGES")
    print("=" * 60)
    for (source, destination), weight in WEIGHTS.items():
        print(
            f"{source} -> {destination} : weight = {weight}"
        )
# ============================================================
# MAIN PROGRAM
# ============================================================
def main():
    print("=" * 60)
    print("SUPERIOR UNIVERSITY")
    print("ARTIFICIAL INTELLIGENCE - LAB 3")
    print("SEARCH ALGORITHMS")
    print("=" * 60)
    print("\nStart Node:", START)
    print("Goal Node:", GOAL)
    # Task 1
    run_task_1()
    # Task 2
    run_dls(
        GRAPH,
        START,
        GOAL
    )
    iddfs(
        GRAPH,
        START,
        GOAL,
        max_depth=4
    )
    # Task 3
    display_weighted_graph()
    run_task_3()
    compare_routes()
    print("\n" + "=" * 60)
    print("ALL LAB TASKS COMPLETED")
    print("=" * 60)
# ============================================================
# PROGRAM START
# ============================================================
if __name__ == "__main__":
    main()
