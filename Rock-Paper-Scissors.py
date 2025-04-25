i = 1
computer_score = 0
user_score = 0

choice = input("\n🎮 Ready to play Rock, Paper, Scissors?\n👉 Press 1 to start the game\n❌ Press 2 to exit\nEnter your choice: ")

while(i != 0):
    if(choice == '1'):
        print("\n🙌 Awesome! The game has started!\n")

        user_pick = int(input("🤔 Make your move:\n 1 - 🗿 Rock\n 2 - 📄 Paper\n 3 - ✂️  Scissors\nYour choice: "))
        if(user_pick == 1):
            print("\n🧑 You chose Rock 🗿.")
        elif(user_pick == 2):
            print("\n🧑 You chose Paper 📄.")
        elif(user_pick == 3):
            print("\n🧑 You chose Scissors ✂️.")
        else:
            print("\n⚠️ Invalid choice. Please select a valid option.")

        import random
        comp_pick = random.randint(1, 3)
        if(comp_pick == 1):
            print("🤖 Computer chose Rock 🗿.")
        elif(comp_pick == 2):
            print("🤖 Computer chose Paper 📄.")
        else:
            print("🤖 Computer chose Scissors ✂️.")

        if(user_pick == comp_pick):
            print("\n😐 It's a tie! You both chose the same.")
        elif(user_pick == 1 and comp_pick == 2):
            computer_score += 1
            print("\n💥 You lost this round. Computer wins! 🖥️")
        elif(user_pick == 1 and comp_pick == 3):
            user_score += 1
            print("\n🎉 You won this round! Computer loses. 🥳")
        elif(user_pick == 2 and comp_pick == 1):
            user_score += 1
            print("\n🎉 You won this round! Computer loses. 🥳")
        elif(user_pick == 2 and comp_pick == 3):
            computer_score += 1
            print("\n💥 You lost this round. Computer wins! 🖥️")
        elif(user_pick == 3 and comp_pick == 1):
            computer_score += 1
            print("\n💥 You lost this round. Computer wins! 🖥️")
        elif(user_pick == 3 and comp_pick == 2):
            user_score += 1
            print("\n🎉 You won this round! Computer loses. 🥳")
        else:
            print("\n⚠️ You didn't make a valid selection.")

    elif(choice == '2'):
        print("\n👋 Game over. Thanks for playing! 🙏")
        break
    elif (choice == ""):
        print("⚠️ You didn't enter anything! Please enter a choice.")
    else:
        print("\n⚠️ Invalid option. Please choose 1 or 2.\n")

    print(f"\n📊 Current Scores:\n🙋 You: {user_score}\n🤖 Computer: {computer_score}")

    choice = input("\n🔁 Would you like to play another round?\n👉 Press 1 to play again\n❌ Press 2 to exit\nEnter your choice: ")

i += 1

print("\n🏁 Final Results:")
if(user_score > computer_score):
    print(f"🏆 Congratulations! You beat the computer by {user_score - computer_score} point! 🎉")
elif(computer_score > user_score):
    print(f"💻 The computer wins! It beat you by {computer_score - user_score} point(s). Better luck next time! 😅")
else:
    print("🤝 It's a draw! Both you and the computer have the same score.")