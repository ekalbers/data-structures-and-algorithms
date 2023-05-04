def left_join(hashtable_a, hashtable_b):
    keys = hashtable_a.keys()
    left_joined = []
    for key in keys:
        left_joined.append([key, hashtable_a.get(key), hashtable_b.get(key)])

    return left_joined

