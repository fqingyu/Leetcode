def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float

    partition_x + partition_y = (x + y + 1) / 2

    while
    max_left_x <= min_right_y
    max_left_y <= min_right_x

    if max_left_x > min_right_y
        move partition_x to left by 1
    else
        move partition_x to right by 1
    """
    if len(nums1) < len(nums2):
        return findMedianSortedArrays(nums2, nums1)
    else:
        start = 0
        end = len(nums1)
        partition_x = int((start + end) / 2)
        partition_y = int((len(nums1) + len(nums2) + 1) / 2 - partition_x)
        print("Initial: x:{}, y:{}".format(partition_x, partition_y))
        print(nums2)
        if partition_x - 1 < 0:
            x_left = -float('inf')
        else:
            x_left = nums1[partition_x-1]
        if partition_y - 1 < 0:
            y_left = -float('inf')
        else:
            y_left = nums2[partition_y-1]
        if partition_x >= len(nums1):
            x_right = float('inf')
        else:
            x_right = nums1[partition_x]
        if partition_y >= len(nums2):
            y_right = float('inf')
        else:
            y_right = nums2[partition_y]


        while x_left > y_right or y_left > x_right:
            if y_left > x_right:
                start = partition_x + 1
            else:
                end = partition_x - 1
            partition_x = int((start + end) / 2)
            partition_y = int((len(nums1) + len(nums2) + 1) / 2 - partition_x)
            print(partition_x)
            if partition_x - 1 < 0:
                x_left = -float('inf')
            else:
                x_left = nums1[partition_x-1]
            if partition_y - 1 < 0:
                y_left = -float('inf')
            else:
                y_left = nums2[partition_y-1]
            if partition_x >= len(nums1):
                x_right = float('inf')
            else:
                x_right = nums1[partition_x]
            if partition_y >= len(nums2):
                y_right = float('inf')
            else:
                y_right = nums2[partition_y]
        if (len(nums1) + len(nums2)) % 2 == 0:
            print("x")
            ans = (max(x_left, y_left) + min(x_right, y_right)) / 2
        else:
            ans = max(x_left, y_left)

        return ans

print(findMedianSortedArrays([], [1]))
