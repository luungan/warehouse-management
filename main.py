items = []

# ===== FUNCTIONS =====

def add_item():
    name = input("Nhập tên hàng: ")
    items.append(name)
    print("Đã thêm!")

def display_items():
    if not items:
        print("Kho trống!")
    else:
        print("Danh sách hàng:")
        for i, item in enumerate(items, 1):
            print(f"{i}. {item}")

def search_item():
    keyword = input("Nhập tên cần tìm: ")
    found = [item for item in items if keyword.lower() in item.lower()]
    
    if found:
        print("Kết quả tìm kiếm:")
        for item in found:
            print(item)
    else:
        print("Không tìm thấy!")

def sort_items():
    items.sort()
    print("Đã sắp xếp!")

def statistics():
    print(f"Tổng số mặt hàng: {len(items)}")

def save_to_file():
    with open("data.txt", "w", encoding="utf-8") as f:
        for item in items:
            f.write(item + "\n")
    print("Đã lưu vào file!")

def load_from_file():
    try:
        with open("data.txt", "r", encoding="utf-8") as f:
            global items
            items = [line.strip() for line in f]
        print("Đã tải dữ liệu!")
    except FileNotFoundError:
        print("Chưa có file dữ liệu!")

# ===== MENU =====

def menu():
    while True:
        print("\n===== WAREHOUSE MANAGEMENT =====")
        print("1. Add item")
        print("2. Display items")
        print("3. Search item")
        print("4. Sort items")
        print("5. Statistics")
        print("6. Save to file")
        print("7. Load from file")
        print("0. Exit")

        choice = input("Chọn: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            display_items()
        elif choice == "3":
            search_item()
        elif choice == "4":
            sort_items()
        elif choice == "5":
            statistics()
        elif choice == "6":
            save_to_file()
        elif choice == "7":
            load_from_file()
        elif choice == "0":
            print("Thoát chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ!")

# ===== RUN =====

menu()


# ================= ADD =================
def add_item():
    id = input("Enter ID: ")

    for i in items:
        if i["id"] == id:
            print("ID already exists!")
            return

    name = input("Enter name: ")

    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
    except:
        print("Invalid input!")
        return

    item = {
        "id": id,
        "name": name,
        "quantity": quantity,
        "price": price
    }

    items.append(item)
    print("Added successfully!")


# ================= DISPLAY =================
def display_items():
    if not items:
        print("No data!")
        return

    print("\nID | Name | Quantity | Price")
    for i in items:
        print(f"{i['id']} | {i['name']} | {i['quantity']} | {i['price']}")


# ================= SEARCH =================
def search_item():
    keyword = input("Enter ID or name: ").lower()

    found = False
    for i in items:
        if keyword in i["id"].lower() or keyword in i["name"].lower():
            print(i)
            found = True

    if not found:
        print("Not found!")


# ================= SORT =================
def sort_items():
    items.sort(key=lambda x: x["price"])
    print("Sorted by price!")


# ================= STATISTICS =================
def statistics():
    if not items:
        print("No data!")
        return

    total_value = sum(i["quantity"] * i["price"] for i in items)

    print(f"Total items: {len(items)}")
    print(f"Total warehouse value: {total_value}")


# ================= SAVE =================
def save_to_file():
    with open("items.txt", "w") as f:
        for i in items:
            f.write(f"{i['id']},{i['name']},{i['quantity']},{i['price']}\n")

    print("Saved to file!")


# ================= LOAD =================
def load_from_file():
    global items
    try:
        with open("items.txt", "r") as f:
            items = []
            for line in f:
                data = line.strip().split(",")
                items.append({
                    "id": data[0],
                    "name": data[1],
                    "quantity": int(data[2]),
                    "price": float(data[3])
                })
        print("Loaded from file!")
    except:
        print("No file found!")


# ================= MAIN =================
def main():
    load_from_file()
    while True:
        menu()


main()