from search import *


class WolfGoatCabbage(Problem):

    def __init__(self, initial=frozenset({'F', 'G', 'W', 'C'}), goal=set()):
        super().__init__(initial, goal)

    def result(self, state, action):
        if action[0] is not set():
            return frozenset(state ^ action[0])
        return set()
        # current_state = state
        # if state == {'F', 'W', 'G', 'C'}:
        #     current_state = {'W', 'C'}
        # elif state == {'W', 'C'}:
        #     current_state = {'F', 'W', 'C'}
        # elif state == {'F', 'W', 'C'}:
        #     current_state = {'F', 'G', 'C'}
        # elif state == {'F', 'G', 'C'}:
        #     current_state = 'F', 'G', 'C'
        # elif state == {'F', 'G', 'C'}:
        #     current_state = {'G'}
        # elif state == {'G'}:
        #     current_state = {'F', 'G'}
        # elif state == {'F', 'G'}:
        #     current_state = set()
        # return frozenset(current_state)

    def actions(self, state):
        if state == {'F', 'W', 'G', 'C'}:
            return [{'F', 'G'}]
        elif state == {'W', 'C'}:
            return [{'F'}]
        elif state == {'F', 'W', 'C'}:
            return [{'F', 'W'}]
        elif state == {'F', 'G', 'C'}:
            return [{'F', 'G'}]
        elif state == {'F', 'G', 'C'}:
            return [{'F', 'C'}]
        elif state == {'G'}:
            return [{'F'}]
        elif state == {'F', 'G'}:
            return [{'G', 'F'}]

    def goal_test(self, state):
        return state == self.goal


def main():
    # puzzler = EightPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 0))
    # print("Question 5")
    # print(puzzler.actions(state=(0, 1, 2, 3, 4, 5, 6, 7, 8)))
    # print("Question 6")
    # print(puzzler.result(state=(0, 1, 2, 3, 4, 5, 6, 7, 8), action='DOWN'))
    # print("Question 7")
    # puzzle = EightPuzzle((1, 2, 3, 5, 7, 4, 8, 6, 0))
    # print(breadth_first_graph_search(puzzle).solution())
    # print(len((breadth_first_graph_search(puzzle).solution())))

    print({'F', 'W', 'G', 'C'} == {'F', 'G', 'C', 'W'})

    wgc = WolfGoatCabbage()
    # print(wgc.initial)
    # print(wgc.actions({'F', 'W', 'G', 'C'}))
    # print(wgc.result({'F', 'W', 'G', 'C'}, [{'F', 'G'}]))
    # print(wgc.result({'W', 'C'}, [{'F'}]))
    # print(wgc.actions(wgc.result({'F', 'W', 'G', 'C'}, [{'F', 'G'}])))
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    # solution = breadth_first_graph_search(wgc).solution()
    # print(solution)

    return


if __name__ == '__main__':
    main()
