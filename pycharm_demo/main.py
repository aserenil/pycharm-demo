import pprint

from sorting_techniques import pysort

from data.crops import crops
from output import output_crops
from output import get_minimum_count

import pydevd_pycharm

# pydevd_pycharm.settrace('localhost', port=5678, stdoutToServer=True, stderrToServer=True)
pydevd_pycharm.settrace('localhost', port=5678, stdoutToServer=True, stderrToServer=True, suspend=False)

sort_obj = pysort.Sorting()


def main():
    output_crops(crops_data=crops)
    pprint.pprint(get_minimum_count(crops_data=crops))

    sorted_crops = sort_obj.bubbleSort(list(crops.keys()))
    for crop in sorted_crops:
        count = crops[crop]
        print(crop, count)

    pprint.pprint(get_minimum_count(crops_data=crops))


if __name__ == '__main__':
    main()
