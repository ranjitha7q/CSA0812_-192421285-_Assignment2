"""Q5: Mutable default argument bug and safe function design."""

def add_item_buggy(item, order=[]):
    order.append(item)
    return order

def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order

def calculate_total_and_gst(items, gst_rate=0.05):
    total = sum(items)
    gst = total * gst_rate
    return total, gst

def make_order_adder():
    order = []
    def add(item):
        order.append(item)
        return order.copy()
    return add

if __name__ == "__main__":
    print("Buggy shared default:")
    print(add_item_buggy("Tea"))
    print(add_item_buggy("Vada"))
    print("Stored defaults:", add_item_buggy.__defaults__)

    print("\\nCorrect independent customer orders:")
    print("Customer 1:", add_item("Tea"))
    print("Customer 2:", add_item("Vada"))
    print("Customer 3:", add_item("Coffee"))

    total, gst = calculate_total_and_gst([10, 20, 15])
    print(f"Total: Rs. {total:.2f}; GST: Rs. {gst:.2f}; Grand total: Rs. {total + gst:.2f}")

    print("\\nClosure example:")
    customer_order = make_order_adder()
    print(customer_order("Tea"))
    print(customer_order("Vada"))
