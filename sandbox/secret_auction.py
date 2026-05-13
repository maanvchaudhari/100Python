import subprocess


def take_bid():
    name = input("\nEnter your name\n→ ").strip().lower()
    while True:
        try:
            amount = float(input("What amount would you like to bid\n₹ "))
            if amount <= 0:
                print("\n⚠️ Bidding amount should be atleast ₹1 ⚠️")
                continue
            break
        except ValueError:
            print("\n⚠️ Type in a valid numerical value ⚠️")
    return {name: amount}


def main():
    bid_dict = {}
    while True:
        subprocess.call(["clear"])
        print("* WELCOME TO SECRET AUCTION *")
        bid_dict.update(take_bid())
        do_continue = (
            input("Are there any more bidders? [Yes / No]\n→ ").strip().lower()
        )
        while do_continue not in ("yes", "no"):
            print("\n⚠️ Type in either 'yes' or 'no'")
            do_continue = (
                input("Are there any more bidders? [Yes / No]\n→ ").strip().lower()
            )
        if do_continue == "no":
            break
    winner = max(bid_dict, key=bid_dict.get)
    print(f"\nThe winner is {winner}, with bid amount of ₹{bid_dict[winner]}")


if __name__ == "__main__":
    main()
