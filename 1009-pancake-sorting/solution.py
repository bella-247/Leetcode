class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def rev(arr, k):
            for i in range(k//2):
                arr[i], arr[k - i - 1] = arr[k - i - 1], arr[i]

        n = len(arr)
        result = []

        for i in range(1, n + 1):
            for j in range(n - i + 1):
                # we find the number we want to place in the current iteration
                if arr[j] == i:
                    # check if it is in the right position
                    if j != n - i:
                        # if it is already at the front then we don't need to reverse it
                        if j != 0:
                            k = j + 1
                            result.append(k)
                            rev(arr, k)

                        # now we made the necessary number at the front so we can reverse it upto its position so that it becomes at its position
                        k = n - i + 1
                        result.append(k)
                        rev(arr, k)
                        break

        result.append(n)
        return result
