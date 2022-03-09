from search import *


class WolfGoatCabbage(Problem):

    def __init__(self, initial={'F', 'G', 'W', 'C'}, goal=set()):
        super().__init__(initial, goal)

    def goal_test(self, state):
        return state == self.goal
    
    def result(self, state, action):
        return [{'F', 'G'}]

    def actions(self, state):
        #1st level
        if state == {'F', 'W', 'G', 'C'}:
            return [{'F', 'G'}]
        #2nd level
        elif  state == {'F', 'G'}:
            return [{'G'}]
        #3rd level
        elif  state == {'G'}:
            return [{'F', 'W', 'G'}]
        elif  state == {'G'}:
            return [{'F', 'G', 'C'}]
        #4th level
        elif  state == {'F', 'W', 'G'}:
            return [{'W'}]
        elif  state == {'F', 'G', 'C'}:
            return [{'C'}]
        #5th level
        elif  state == {'W'}:
            return [{'F', 'W', 'C'}]
        elif  state == {'C'}:
            return [{'F', 'W', 'C'}]
        #6th level
        elif  state == {'F', 'W', 'C'}:
            return [{'W', 'C'}]
        #7th level
        elif  state == {'W', 'C'}:
            return [{'F', 'W', 'G', 'C'}]



def main():
    wgc = WolfGoatCabbage()
    print("Initial state")
    print(wgc.initial)

    # print("Actions")
    # print(wgc.actions({'F', 'W', 'G', 'C'}))
    
    print("Goal Test")
    # print(wgc.goal_test({'F', 'G', 'W', 'C'}))
    
    # solution = depth_first_graph_search(wgc).solution()
    # print(solution)
    # solution = breadth_first_graph_search(wgc).solution()
    # print(solution)

    return


if __name__ == '__main__':
    main()
