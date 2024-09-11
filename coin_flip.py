from random import randint

# tails = 1
# heads = 2

tails_counter = 0
heads_counter = 0


def coin_flip(tails, heads):
    result = randint(1, 2)
    return result


play_times = int(input("How many times would you like to flip a coin? "))

for i in range(play_times):
    result = coin_flip(tails_counter, heads_counter)
    if result == 1:
        tails_counter += 1
        print("Tails has won!")
    elif result == 2:
        heads_counter += 1
        print("Heads has won!")

print("\nGame Over")
print(f"Tails has won {tails_counter} times while heads has won {heads_counter} times.")
