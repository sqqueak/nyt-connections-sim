import random
import pprint

game = []
answer = []
for _ in range(4):
    game += (list(map(str, input().split(" "))))
input()
for _ in range(4):
    answer.append(set(map(str, input().split(" "))))
 
avg = 0
rounds = 100
for __ in range(rounds):
    guesses = 0
    while True:
        leave = False
        guess_index = set()
        guess_word = []
        for _ in range(4):
            x = random.randint(0,15)
            while x in guess_index:
                x = random.randint(0,15)
            guess_index.add(x)
            guess_word.append(game[x])

        for i in range(len(answer)):
            correct = True
            for w in guess_word:
                if w not in answer[i]:
                    correct = False
            if correct:
                # print(guesses)
                # print(guess_word)
                # answer.pop(i)
                # if len(answer) == 0:
                #     leave = True
                leave = True
        guesses += 1
        if leave:
            break
    avg += guesses
print(avg / rounds)
