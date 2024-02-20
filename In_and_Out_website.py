def max_visitors_online(n, t_in, t_out):
    events = []
    for i in range(n):
        events.append(t_in[i], -1)
        events.append(t_out[i], 1)
    events.sort()
    online = 0
    max_online = 0
    for event in events:
        if event[1] == -1:
            online += 1
        else:
            online -= 1
        max_online = max(online, max_online)
    return max_online

def time_visitors_online(n, t_in, t_out):
    events = []
    for i in range(n):
        events.append(t_in[i], -1)
        events.append(t_out[i], 1)
    events.sort()
    online = 0
    not_empty_time = 0
    for i in range(len(events)):
        if online > 0:
            not_empty_time += events[i][0] - events[i - 1][0]
        if events[1] == -1:
            online += 1
        else:
            online -= 1
    return not_empty_time