import json
import random

# Списък с рандом думи за имена
random_names = [
    "Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta",
    "Iota", "Kappa", "Lambda", "Mu", "Nu", "Xi", "Omicron", "Pi",
    "Rho", "Sigma", "Tau", "Upsilon", "Phi", "Chi", "Psi", "Omega",
    "Phoenix", "Dragon", "Tiger", "Eagle", "Wolf", "Lion", "Shark", "Falcon",
    "Thunder", "Lightning", "Storm", "Blaze", "Frost", "Shadow", "Ghost", "Viper",
    "Rocket", "Bullet", "Arrow", "Sword", "Shield", "Armor", "Crown", "Diamond",
    "Gold", "Silver", "Bronze", "Iron", "Steel", "Crystal", "Ruby", "Emerald",
    "Nova", "Star", "Moon", "Sun", "Earth", "Mars", "Venus", "Jupiter",
    "Ace", "King", "Queen", "Jack", "Knight", "Warrior", "Hero", "Champion",
    "Master", "Expert", "Pro", "Elite", "Prime", "Max", "Ultra", "Mega"
]

# Списък с emoji
emojis = [
    "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇",
    "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗", "😙", "😚",
    "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐", "🤓", "😎", "🤩",
    "🥳", "😏", "😒", "😞", "😔", "😟", "😕", "🙁", "☹️", "😣",
    "😖", "😫", "😩", "🥺", "😢", "😭", "😤", "😠", "😡", "🤬",
    "🤯", "😳", "🥵", "🥶", "😱", "😨", "😰", "😥", "😓", "🤗",
    "🤔", "🤭", "🤫", "🤥", "😶", "😐", "😑", "😬", "🙄", "😯",
    "😦", "😧", "😮", "😲", "🥱", "😴", "🤤", "😪", "😵", "🤐",
    "🥴", "🤢", "🤮", "🤧", "😷", "🤒", "🤕", "🤑", "🤠", "😈",
    "👿", "👹", "👺", "🤡", "💩", "👻", "💀", "☠️", "👽", "👾",
    "🤖", "🎃", "😺", "😸", "😹", "😻", "😼", "😽", "🙀", "😿",
    "🔥", "💯", "💢", "💥", "💫", "💦", "💨", "🕳️", "💣", "💤",
    "🚀", "🛸", "⭐", "🌟", "✨", "⚡", "☄️", "💥", "🔥", "🌈",
    "🎯", "🎪", "🎨", "🎭", "🎪", "🎡", "🎢", "🎠", "🎳", "🎲",
    "🎮", "🕹️", "🎰", "🎱", "🏆", "🥇", "🥈", "🥉", "🏅", "🎖️",
    "🤛", "🤜", "👊", "✊", "👍", "👎", "👌", "🤏", "✌️", "🤞",
    "🤟", "🤘", "🤙", "👈", "👉", "👆", "🖕", "👇", "☝️", "👋",
    "🤚", "🖐️", "✋", "🖖", "👏", "🙌", "👐", "🤲", "🔫", "🗡️"
]


def generate_wallet_entry(wallet_address):
    """Генерира един wallet entry с рандом име и emoji"""
    return {
        "trackedWalletAddress": wallet_address,
        "name": random.choice(random_names),
        "emoji": random.choice(emojis),
        "alertsOn": False
    }


def generate_multiple_wallets():
    """Генерира множество wallet entries"""
    wallets = []

    print("Въведете wallet адреси (празен ред за край):")
    while True:
        address = input("Wallet адрес: ").strip()
        if not address:
            break
        wallets.append(generate_wallet_entry(address))

    return wallets


def main():
    # Генериране на wallet entries
    wallets = generate_multiple_wallets()

    if not wallets:
        print("Няма въведени wallet адреси.")
        return

    # Конвертиране в JSON
    json_output = json.dumps(wallets, indent=2, ensure_ascii=False)

    print("\nГенериран JSON:")
    print(json_output)

    # Запазване във файл (опционално)
    save_to_file = input("\nИскате ли да запазите във файл? (y/n): ").lower()
    if save_to_file == 'y':
        filename = input("Име на файла (без разширение): ").strip()
        if not filename:
            filename = "wallets"

        with open(f"{filename}.json", 'w', encoding='utf-8') as f:
            f.write(json_output)
        print(f"Файлът е запазен като {filename}.json")


if __name__ == "__main__":
    main()
