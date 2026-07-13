def show_title():
    print("DynastyIQ Blueprint Allocator")
    print("Plan how your program will spend its resources.")


def ask_for_points(prompt):
    while True:
        try:
            points = int(input(prompt))

            if points < 0:
                print("Please enter zero or a positive whole number.")
            else:
                return points
        except ValueError:
            print("Please enter a whole number.")

def calculate_percentage(category_points, available_points):
    if available_points == 0:
        return 0.0

    return category_points / available_points * 100

show_title()
available_points = ask_for_points("Enter available Dynasty Points: ")
coaching_staff_points = ask_for_points("Allocate to Coaching Staff: ")
facilities_points = ask_for_points("Allocate to Facilities: ")
recruiting_nil_points = ask_for_points("Allocate to Recruiting NIL: ")
roster_nil_points = ask_for_points("Allocate to Roster NIL: ")
allocations = {
    "Coaching Staff": coaching_staff_points,
    "Facilities": facilities_points,
    "Recruiting NIL": recruiting_nil_points,
    "Roster NIL": roster_nil_points,
}

total_allocated = (
    coaching_staff_points
    + facilities_points
    + recruiting_nil_points
    + roster_nil_points
)
remaining_points = available_points - total_allocated

print(f"Total allocated: {total_allocated} Dynasty Points")
if total_allocated > available_points:
    points_over = total_allocated - available_points
    print(f"Warning: You allocated {points_over} too many Dynasty Points.")
elif total_allocated == available_points:
    print(f"Your Dynasty Points are fully allocated.")
else:
    print(f"You have {remaining_points} Dynasty Points remaining.")

print("\nAllocation percentages:")
for category_name, category_points in allocations.items():
    percentage = calculate_percentage(category_points, available_points)
    print(f"{category_name}: {percentage:.1f}%")