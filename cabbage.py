start_node = 'wwww'
goal_node = 'eeee'

test = {
    'wwww': ['ewew', 'eeww', 'ewwe', 'ewww'],
    'ewww': ['wwww'],
    'ewwe': ['wwww'],
    'ewew': ['wwww'],
    'eewe': ['wwwe', 'weww', 'weww'],
    'wwwe': ['eewe', 'ewee', 'eewe'],
    'eeww': ['weww', 'wwww'],
    'weww': ['eeew', 'eewe', 'eeww'],
    'ewee': ['wwew', 'wwee', 'wwwe'],
    'wwee': ['ewee', 'eeee']
}
def depth_first_search(test, start, goal):
    stack = [(start, [])]
    visited = set()

    while stack:
        current, path = stack.pop()
        visited.add(current)

        if current == goal:
            return path + [current]

        for neighbor in test[current]:
            if neighbor not in visited:
                stack.append((neighbor, path + [current]))

    return None

path_to_goal = depth_first_search(test, start_node, goal_node)

if path_to_goal:
    print("The destination path:\n", ' --> '.join(path_to_goal))
else:
    print("Sorry! No goal found")
