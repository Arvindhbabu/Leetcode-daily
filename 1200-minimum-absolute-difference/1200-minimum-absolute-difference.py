class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()

        mini = float('inf')
        for i in range(1, n):
            mini = min(mini, arr[i]-arr[i-1])

        # l = list()
        l = []
        for i in range(1, n):
            if(mini == arr[i]-arr[i-1]):
                l.append([arr[i-1], arr[i]])

        return l;        