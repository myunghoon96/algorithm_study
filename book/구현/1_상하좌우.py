n = 5
plans = ['R', 'R', 'R', 'U', 'D', 'D']

x, y = 1, 1

for plan in plans:

    if plan == 'R':
        if y + 1 <= n:
            y += 1
        
    elif plan == 'L':
        if y - 1 >= 1:
            y -= 1
        
    elif plan == 'U':
        if x - 1 >= 1:
            x -= 1
        
    elif plan == 'D':
        if x + 1 <= n:
            x += 1

print(x,y)