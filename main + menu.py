<<<<<<< HEAD
items = []

# ===== FUNCTIONS =====

def add_item(items):
    name = input("Nhập tên hàng: ")
    items.append(name)
    print("Đã thêm!")

def display_items(items):
    if not items:
        print("Kho trống!")
    else:
        print("Danh sách hàng:")
        for i, item in enumerate(items, 1):
            print(f"{i}. {item}")

def search_item(items):
    keyword = input("Nhập tên cần tìm: ")
    found = [item for item in items if keyword.lower() in item.lower()]
    
    if found:
        print("Kết quả tìm kiếm:")
        for item in found:
            print(item)
    else:
        print("Không tìm thấy!")

def sort_items(items):
    items.sort()
    print("Đã sắp xếp!")

def statistics(items):
    print(f"Tổng số mặt hàng: {len(items)}")

def save_to_file(items):
    with open("data.txt", "w", encoding="utf-8") as f:
        for item in items:
            f.write(item + "\n")
    print("Đã lưu vào file!")

def load_from_file(items):
    items = []
    try:
        with open("data.txt", "r", encoding="utf-8") as f:
            items = [line.strip() for line in f]
        print("Đã tải dữ liệu!")
    except FileNotFoundError:
        print("Chưa có file dữ liệu!")

    return items

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


=======
items = []

# ===== FUNCTIONS =====

def add_item(items):
    name = input("Nhập tên hàng: ")
    items.append(name)
    print("Đã thêm!")

def display_items(items):
    if not items:
        print("Kho trống!")
    else:
        print("Danh sách hàng:")
        for i, item in enumerate(items, 1):
            print(f"{i}. {item}")

def search_item(items):
    keyword = input("Nhập tên cần tìm: ")
    found = [item for item in items if keyword.lower() in item.lower()]
    
    if found:
        print("Kết quả tìm kiếm:")
        for item in found:
            print(item)
    else:
        print("Không tìm thấy!")

def sort_items(items):
    items.sort()
    print("Đã sắp xếp!")

def statistics(items):
    print(f"Tổng số mặt hàng: {len(items)}")

def save_to_file(items):
    with open("data.txt", "w", encoding="utf-8") as f:
        for item in items:
            f.write(item + "\n")
    print("Đã lưu vào file!")

def load_from_file(items):
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

>>>>>>> ace27496b142fc2ef76e037bef1bb9e2b47f95ae
