
def scoreboard(who_ate_what):

    class Struct:
        def __init__(self, ** entries):
            self.__dict__.update(entries)
    li = []
    for p in who_ate_what:
        if 'chickenwings' not in p:
            p['chickenwings'] = 0
        if 'hamburgers' not in p:
            p['hamburgers'] = 0
        if 'hotdogs' not in p:
            p['hotdogs'] = 0
            # random cases (incomplete)

        args = p
        s = Struct(**args)
        score = s.chickenwings*5+s.hamburgers*3+s.hotdogs*2
        d = {'name': s.name, 'score': score}
        li.append(d)

    final = sorted(li, key=lambda d: (-d['score'], d['name']))
    return(final)


print(scoreboard([{'name': 'T800'}, {'name': 'T-X', 'hotdogs': 11, 'chickenwings': 2, 'hamburgers': 11}, {'name': 'Skynet', 'hamburgers': 15, 'chickenwings': 8, 'hotdogs': 6},
      {'name': 'T1000', 'chickenwings': 5}, {'name': 'Sarah Connor', 'hamburgers': 15, 'hotdogs': 3}, {'name': 'John Connor', 'chickenwings': 13}, {'name': 'Kyle Reese', 'hotdogs': 10}]))
