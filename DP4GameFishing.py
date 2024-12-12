from collections import defaultdict
H=100 #fish's health
E=100 #initial stamina
D=5 #inital damage per swing
F=10 #initial stamina cost per swing
N=5 #number of events
events=[  #events: [perminently increase stamina, perminently increase damage]
    [5,5], #event 1 is events[0]
    [5,5],
    [5,5],
    [5,5],
    [5,5]
]
events[0:0]=[[0,0]] #add a dummy event 0。注意，新插入的的元素需要多加一层括号以使维度等于events的维度
print(events)

def can_fish(H, E, D, F, N, events):
    rows = N + 1  # 事件数 + 1（包括初始状态）
    max_stamina = E + sum(event[0] for event in events)  # 计算可能的最大体力
    max_damage = D + sum(event[1] for event in events)   # 计算可能的最大伤害
    cols = max_stamina + 1

    # dp[i][j][dmg] = max_cumulative_damage
    dp = [ [defaultdict(int) for _ in range(cols)] for _ in range(rows)]

    # 初始状态：考虑在没有任何事件的情况下进行挥杆
    for j in range(E, -1, -F):
        swings = (E - j) // F  # 已经挥杆次数
        cumulative_damage = swings * D
        dp[0][j][D] = cumulative_damage

    for i in range(1, rows):
        stamina_up, damage_up = events[i]

        for j in range(cols):
            for dmg in dp[i-1][j]:
                cumulative_damage = dp[i-1][j][dmg]

                # 选择1：增加体力
                new_max_stamina = min(j + stamina_up, max_stamina)
                new_stamina = min(j + stamina_up, new_max_stamina)
                dp[i][new_stamina][dmg] = max(dp[i][new_stamina][dmg], cumulative_damage)

                # 计算增加体力后可以额外挥杆的次数和新的累积伤害
                swings = new_stamina // F
                remaining_stamina = new_stamina - swings * F
                total_damage = cumulative_damage + swings * dmg
                dp[i][remaining_stamina][dmg] = max(dp[i][remaining_stamina][dmg], total_damage)

                # 选择2：增加伤害
                new_dmg = dmg + damage_up
                dp[i][j][new_dmg] = max(dp[i][j][new_dmg], cumulative_damage)

                # 计算增加伤害后可以挥杆的次数和新的累积伤害
                swings = j // F
                remaining_stamina = j - swings * F
                total_damage = cumulative_damage + swings * new_dmg
                dp[i][remaining_stamina][new_dmg] = max(dp[i][remaining_stamina][new_dmg], total_damage)

    # 检查是否有可能在任意状态下达到或超过鱼的血量
    for j in range(cols):
        for dmg in dp[N][j]:
            if dp[N][j][dmg] >= H:
                return "YES"
    return "NO"

print(can_fish(H,E,D,F,N,events))