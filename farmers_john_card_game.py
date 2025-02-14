def main():
    players, rounds = map(int, input().split())

    cows_cards = []
    for _ in range(players):
        cards = list(map(int, input().split()))
        cows_cards.append(sorted(cards))

    def can_complete_game(perm):
        for round in range(rounds):
            top = -1

            for cow_idx in perm:
                cow_card = cows_cards[cow_idx-1][round]

                if cow_card <= top:
                    return False

                top = cow_card

        return True

    cow_min_cards = []
    for i, cards, in enumerate(cows_cards):
        min_card = min(cards)
        cow_number = i + 1
        cow_min_cards.append((min_card, cow_number))

    print("For each cow:")
    for min_card, cow_number in cow_min_cards:
        print(f"Cow {cow_number} has minimum card {min_card}")


    cow_min_cards.sort()

    perm = []
    for x in cow_min_cards:
        cow_number = x[1]
        perm.append(cow_number)

    if can_complete_game(perm):
        return perm
    return [-1]

result = main()
print(*result)