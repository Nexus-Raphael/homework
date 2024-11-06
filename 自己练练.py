def maxArea(height):
    """
    该函数用于在给定的一组表示不同高度柱子的数组height中，
    通过移动两根指针（分别从数组的两端开始），不断尝试找到能容纳最多水的两根柱子组合，
    从而计算并返回由这些柱子围成的容器所能容纳的最大水量。
    """
    # 初始化左右指针
    left, right = 0, len(height) - 1
    # 初始化最大水量
    MaxArea = 0

    # 当左右指针没有交叉时继续循环
    while left < right:
        # 计算当前水量
        current = (right - left) * min(height[left], height[right])
        # 更新最大水量
        MaxArea = max(current, MaxArea)

        # 移动较短的柱子指针，尝试找到更高的柱子
        if height[left] < height[right]:
            # 向右移动左指针，因为当前左边柱子较矮，
            # 希望通过向右移动左指针找到更高的左边柱子来增大可能的水量
            left += 1
        else:
            # 向左移动右指针，因为当前右边柱子较矮或者与左边柱子等高，
            # 希望通过向左移动右指针找到更高的右边柱子来增大可能的水量
            right -= 1

    return MaxArea  # 返回找到的最大水量


height=[999999999999999999,1,8,6,2,5,4,8,3,7]
print(maxArea(height))