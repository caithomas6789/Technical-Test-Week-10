"""Script which adds the second, minute and hour of the time"""
# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.


# [TODO]: fix the function
def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    total = 0
    list_of_nums = time_str.split(":")
    print(int(list_of_nums[0]))
    if 0 <= int(list_of_nums[0]) < 60 or 0 <= int(list_of_nums[1]) < 60 or 0 <= int(list_of_nums[2]) < 24:
        for num in list_of_nums:
            total += int(num)
        return total

    print("Invalid Time")
    return 0

# Unit tests in the test_3_testing.py file
