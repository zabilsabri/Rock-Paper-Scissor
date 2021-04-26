__foundby__ = "zabilsabri"

while True:
    print("Kertas  = 1 \nBatu    = 2 \nGunting = 3 \n\n")

    player1 = int(input("\n\nPlayer1 \nMASUKKAN ANGKA: "))
    player2 = int(input("\n\nPlayer2 \nMASUKKAN ANGKA: "))

    proses = player1 + player2

    if proses == 5:
        if player1 == 2:
            print("\n\nPlayer1 Win!")
        else:
            print("\n\nPlayer2 Win!")

    if proses == 4:
        if player1 == 3:
            print("\n\nPlayer1 Win!")
        elif player1 == player2:
            print("DRAW!")
        else:
            print("\n\nPlayer2 Win!")

    if proses == 3:
        if player1 == 1:
            print("\n\nPlayer1 Win!")
        else:
            print("\n\nPlayer2 Win!")

    print("\n\nSTART A NEW GAME?")
    usr_command = input("Yes or NO: ")
    if usr_command.lower() == "no":
        break
    else:
        print("---------------------------------------------------------")
        continue

print("GOOD BYE!")