hmap = {}
        ans = []
        for  i in range(m):
            stack = []
            for j in range(n):
                stack.append(arr[i][j])
            stack = tuple(stack)
            if stack in hmap:
                ans.append(i)
            else:
                hmap[stack] = 1
        return ans
