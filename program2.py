def longest_substring(s: str) -> int:
    n = len(str)
    result = 0
    for i in range(n):
        visited = [0] * 256

        for j in range(i, n):

        
            if (visited[ord(str[j])] == True):
                break      
            else:
                result = max(result, j - i + 1)
                visited[ord(str[j])] = True

        visited[ord(str[i])] = False
    return result



