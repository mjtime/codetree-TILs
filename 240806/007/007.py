class Agent:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time
    def print_agent(self):
        print("secret code :", code)
        print("meeting point :", place)
        print("time :", time)

code, place, time = map(str, input().split())
agent1 = Agent(code, place, time)
agent1.print_agent()