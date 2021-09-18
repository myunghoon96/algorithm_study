players = [2,3,1,2,2]
ans = 0

players.sort()

temp_group = []
feer_level = 0
for player in players:

    temp_group.append(player)
    feer_level=player

    if len(temp_group)==feer_level:
        ans+=1
        temp_group=[]
        feer_level = 0

print(players)
print(ans)