both = input("Enter the plays: ").split("@")

player_a = both[0].split(" ")

player_b = both[1].split(" ")

player_a_score = 0
player_b_score = 0

for x in range(0,len(player_a)):
    if(player_a[x] == "rock" and player_b[x] == "scissors"):
        #print("player_a won! Rock beats scissors!")
        player_a_score+=1
    elif player_a[x] == "scissors" and player_b[x] == "paper":
        player_a_score+=1
    elif player_a[x] == "paper" and player_b[x] == "rock":
        player_a_score+=1
    elif player_b[x] == "rock" and player_a[x] == "scissors":
        player_b_score+=1
    elif player_b[x] == "scissors" and player_a[x] == "paper":
        player_b_score+=1
    elif player_b[x] == "paper" and player_a[x] == "rock":
        player_b_score+=1

print("Score of player a: " + str(player_a_score) + "  Score of player b: " + str(player_b_score))
# print("Score of player b: " + str(player_b_score))

if player_a_score > player_b_score:
    print("Player A won!")
elif player_b_score > player_a_score:
    print("Player B won!")
else:
    print("Tie!")
