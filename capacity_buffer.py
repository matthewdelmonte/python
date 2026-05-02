def capacity_buffer(total_hours, buffer_ratio=0.2):
    return total_hours * (1 - buffer_ratio)

print(f"Available Capacity {capacity_buffer(40,0.15)} Hours")