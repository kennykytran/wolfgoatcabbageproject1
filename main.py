from search import *

//test
class WolfGoatCabbage(Problem):

    def __init__(self, initial={'F', 'G', 'W', 'C'}, goal=set()):
        super().__init__(initial, goal)

    def result(self, state, action):
        return [{'F', 'G'}]

    def actions(self, state):
        if state == {'F', 'W', 'G', 'C'}:
            return [{'F', 'G'}]

    def goal_test(self, state):
        return state == self.goal


def main():
    puzzler = EightPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 0))
    print("Question 5")
    print(puzzler.actions(state=(0, 1, 2, 3, 4, 5, 6, 7, 8)))
    print("Question 6")
    print(puzzler.result(state=(0, 1, 2, 3, 4, 5, 6, 7, 8), action='DOWN'))
    print("Question 7")
    puzzle = EightPuzzle((1, 2, 3, 5, 7, 4, 8, 6, 0))
    print(breadth_first_graph_search(puzzle).solution())
    print(len((breadth_first_graph_search(puzzle).solution())))

    wgc = WolfGoatCabbage()
    print(wgc.initial)
    print(wgc.actions({'F', 'W', 'G', 'C'}))
    # solution = depth_first_graph_search(wgc).solution()
    # print(solution)
    # solution = breadth_first_graph_search(wgc).solution()
    # print(solution)

    return


if __name__ == '__main__':
    main()
