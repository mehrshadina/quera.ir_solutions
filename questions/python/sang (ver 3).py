m = list(map(int, input().split()))
m_list = []
i = 1
s = 1

while i < len(m) :
    if (not m[i-1] > 0) or (not m[i] < 0):
        i += 1

    else:
        rem = m[i-1] + m[i]

        if m[i-1] == -m[i]:
            text = f'step {s}: meteorite with index {i-1} and {i} with size {m[i-1]} exploded'
            print(text)
            m = m[:i-1] + m[i+1:]
            i -= 1

        else:
            if m[i-1] + m[i] > 0:
                text = f'step {s}: meteorite with index {i} with size {m[i]} exploded'
                print(text)
                m = m[:i-1] + [rem] + m[i+1:]
        
            else:
                text = f'step {s}: meteorite with index {i-1} with size {m[i-1]} exploded' 
                print(text)
                i -= 1
                m = m[:i] + [rem] + m[i+2:]

        print('new orbit:', m)
        s += 1

    


print('final orbit:', m)