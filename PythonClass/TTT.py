import random
EMPTY = 0

state = [[1,2,0], [0,0,0], [0,0,0]]

    def random_func(state):
        available = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == EMPTY:
                    available.append((i ,j)) #[(0,2), (1,0), (1,1), (1,2), (2,0), (2,1)]
        return random.choice(available)

print(random_func(state)) #랜덤으로 수가 출력됨