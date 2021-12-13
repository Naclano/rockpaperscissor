import random
allofthem = ["rock","paper","scissor"]
trallofthem = ["tas","kagit","makas"]
score = 0
while True:

    player = input("pick one: ")
    pc = random.choice(allofthem)
    pctr = random.choice(trallofthem)
    if player == "score":
        print(f"your score: {score} ")
    elif player == pc or player == pctr:
        score += 1
        print("draw")
    elif player == "rock" or player == "tas" and pc == "scissor" or pctr == "makas":
        score += 1
        print("won")
    elif player == "rock" or player == "tas" and pc == "paper" or pctr == "kagit":
        score -= 1
        print("you lose")
    elif player == "paper" or player == "kagit" and pc == "rock" or pctr == "tas":
        score += 1
        print("won")
    elif player == "paper" or player == "kagit" and pc == "scissor" or pctr == "makas":
        score -= 1
        print("you lose")
    elif player == "scissor" or player == "makas" and pc == "paper" or pctr == "kagit":
        score += 1
        print("won")
    elif player == "scissor" or player == "makas" and pc == "rock" or pctr == "tas":
        score -= 1
        print("you lose")
