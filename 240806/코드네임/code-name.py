class Agent:
    def __init__(self, name="", score=0):
        self.name = name
        self.score = score

agents = [Agent() for _ in range(5)]

for i in range(5):
    name, score = tuple(input().split())
    agents[i].name = name
    agents[i].score = int(score)

min_agent = 0
for i in range(1, 5):
    if agents[min_agent].score > agents[i].score:
        min_agent = i

print(agents[min_agent].name, agents[min_agent].score)