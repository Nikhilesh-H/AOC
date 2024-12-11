# path = r"AOC15\day-15\test.txt"
path = r"AOC15\day-15\input.txt"

with open(path) as f:
    ingrediants = f.read().split("\n")

ingrediants = [[int(j.split()[-1]) for j in i.split(",")] for i in ingrediants]

teaspoons = 100

scores = []

if "test" in path:
    for a in range(1, teaspoons+1):
        b = teaspoons - a
        score1 = [a*i for i in ingrediants[0]]
        score2 = [b*i for i in ingrediants[1]]
        if score1[-1] + score2[-1] == 500:
            score = 1
            for i in range(4):
                score *= (score1[i]+score2[i]) if (score1[i]+score2[i]) > 0 else 0
            scores.append(score)

else:
    for a in range(1, teaspoons+1):
        for b in range(teaspoons+1-a):
            for c in range(teaspoons+1-a-b):
                d = teaspoons - a - b - c

                score1 = [a*i for i in ingrediants[0]]
                score2 = [b*i for i in ingrediants[1]]
                score3 = [c*i for i in ingrediants[2]]
                score4 = [d*i for i in ingrediants[3]]

                if score1[-1] + score2[-1] + score3[-1] + score4[-1] == 500:
                    score = 1
                    for i in range(4):
                        score *= (score1[i]+score2[i]+score3[i]+score4[i]) if (score1[i]+score2[i]+score3[i]+score4[i]) > 0 else 0
                    scores.append(score)

print(max(scores))