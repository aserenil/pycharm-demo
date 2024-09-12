def output_crops(crops_data):
    for crop, count in crops_data.items():
        print(f'crop={crop}\n\tcount={count}')


def get_minimum_count(crops_data):
    # Find the minimum value in the dictionary
    min_value = min(crops_data.values())

    # Find all crops that have the minimum value
    crops_with_min_value = [crop for crop, value in crops_data.items() if value == min_value]
    return crops_with_min_value
