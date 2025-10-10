def solution(S:str) -> int:
    # Implement your solution here
    s = S.lstrip('0')
    if not s:
        return 0

    return len(s) + s.count('1') - 1

print(solution("011100"))