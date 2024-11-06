#暂时不太会输入，请见谅

def maxArea(height):
    left, right = 0, len(height) - 1

    maxmum= 0

    while left < right:

        current = (right - left) * min(height[left], height[right])

        maxmum = max(current, maxmum)


        if height[left] < height[right]:

            left += 1
        else:

            right -= 1

    return maxmum


height=[999999999999999999,1,8,6,2,5,4,8,3,7]
print(maxArea(height))