items = []

# ===== ADD ITEM =====

def add_item(items):
    item_id = input("Nhập ID: ")
    name = input("Nhập tên hàng: ")

    while True:
        try:
            quantity = int(input("Nhập số lượng: "))
            if quantity >= 0:
                break
            else:
                print("Số lượng không được âm!")
        except ValueError:
            print("Vui lòng nhập số nguyên!")

    while True:
        try:
            price = float(input("Nhập giá: "))
            if price >= 0:
                break
            else:
                print("Giá không được âm!")
        except ValueError:
            print("Vui lòng nhập số!")

    item = {
        "id": item_id,
        "name": name,
        "quantity": quantity,
        "price": price
    }

    items.append(item)
    print("Đã thêm mặt hàng!")


# ===== DISPLAY ITEMS =====

def display_items(items):
    if not items:
        print("Kho trống!")
        return

    print("\nDanh sách hàng:")
    print("{:<10} {:<20} {:<10} {:<10}".format("ID", "Tên hàng", "Số lượng", "Giá"))

    for item in items:
        print("{:<10} {:<20} {:<10} {:<10}".format(
            item["id"],
            item["name"],
            item["quantity"],
            item["price"]
        ))


# ===== SEARCH ITEM =====

def search_item(items):
    keyword = input("Nhập ID hoặc tên hàng cần tìm: ").lower()

    found = []

    for item in items:
        if keyword in item["id"].lower() or keyword in item["name"].lower():
            found.append(item)

    if not found:
        print("Không tìm thấy!")
        return

    print("\nKết quả tìm kiếm:")
    print("{:<10} {:<20} {:<10} {:<10}".format("ID", "Tên hàng", "Số lượng", "Giá"))

    for item in found:
        print("{:<10} {:<20} {:<10} {:<10}".format(
            item["id"],
            item["name"],
            item["quantity"],
            item["price"]
        ))


# ===== SORT ITEMS =====

def sort_items(items):
    if not items:
        print("Không có dữ liệu để sắp xếp!")
        return

    items.sort(key=lambda item: item["quantity"])
    print("Đã sắp xếp theo số lượng!")


# ===== STATISTICS =====

def statistics(items):
    if not items:
        print("Kho trống!")
        return

    total_quantity = 0
    total_value = 0

    for item in items:
        total_quantity += item["quantity"]
        total_value += item["quantity"] * item["price"]

    print("\nThống kê kho:")
    print("Tổng số mặt hàng:", len(items))
    print("Tổng số lượng hàng:", total_quantity)
    print("Tổng giá trị hàng tồn kho:", total_value)


# ===== SAVE TO FILE =====

def save_to_file(items):
    with open("data.txt", "w", encoding="utf-8") as f:
        for item in items:
            f.write(f"{item['id']},{item['name']},{item['quantity']},{item['price']}\n")

    print("Đã lưu dữ liệu vào file!")


# ===== LOAD FROM FILE =====

def load_from_file(items):
    try:
        with open("data.txt", "r", encoding="utf-8") as f:
            items.clear()

            for line in f:
                item_id, name, quantity, price = line.strip().split(",")

                item = {
                    "id": item_id,
                    "name": name,
                    "quantity": int(quantity),
                    "price": float(price)
                }

                items.append(item)

        print("Đã tải dữ liệu từ file!")

    except FileNotFoundError:
        print("Chưa có file dữ liệu!")

    except ValueError:
        print("File dữ liệu bị sai định dạng!")


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
            add_item(items)
        elif choice == "2":
            display_items(items)
        elif choice == "3":
            search_item(items)
        elif choice == "4":
            sort_items(items)
        elif choice == "5":
            statistics(items)
        elif choice == "6":
            save_to_file(items)
        elif choice == "7":
            load_from_file(items)
        elif choice == "0":
            print("Thoát chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ!")


# ===== RUN =====

if __name__ == "__main__":
    menu()