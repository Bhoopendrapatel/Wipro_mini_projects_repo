def process_purchase_file(filename):
    try:
        with open(filename + ".txt", 'r') as file:
            lines = file.readlines()

        items_purchased = 0
        free_items = 0
        total_amount = 0
        discount = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue

            if line.lower().startswith("discount"):
                try:
                    discount = int(line.split()[1])
                except (IndexError, ValueError):
                    print("Invalid discount format.")
                continue

            parts = line.split()
            if len(parts) < 2:
                continue

            item_name = parts[0]
            item_price = parts[1]

            if item_price.lower() == 'free':
                free_items += 1
            else:
                try:
                    total_amount += int(item_price)
                    items_purchased += 1
                except ValueError:
                    print(f"Invalid price for item: {item_name}")

        final_amount = total_amount - discount

        print(f"Enter the file name: {filename}")
        print(f"No of items purchased: {items_purchased}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {total_amount}")
        print(f"Discount given: {discount}")
        print(f"Final amount paid: {final_amount}")

    except FileNotFoundError:
        print("File not found. Please check the file name.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = input("Enter file name (without .txt): ")
process_purchase_file(filename)