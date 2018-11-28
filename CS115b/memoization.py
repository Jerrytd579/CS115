
import time

# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n - 2)
#
# #start_time = time.time()
# #print(fib(40))
# #print('fib computation time without memoization: %.2f s' % (time.time() - start_time()))
#
# # Memoization
# # 1: If key is inside  the dictionary, return the value associated with the key
# # 2: Do work! In other words, recursively compute the answer and store the result in a local variable
# # 3: Store the result in the dictionary, and return the result.
#
def fib_memo(n):
    def fib_helper(n, memo):
        # If n is in memo, return memo[n]. Refer to step one in memoization.
        if n in memo:
            return memo[n]
        # Do work.
        # Recursively compute the next fibonacci number.
        # Save the result in a local variable
        if n <= 1:
            result = n
        else:
            result = fib_helper(n - 2, memo) + fib_helper(n - 1, memo)
        # Store the result in memo and return the result
        memo[n] = result
        return result
    return fib_helper(n, {})

print(fib_memo(28))
#
# start_time = time.time()
# print(fib_memo(40))
# print('fib computation time without memoization: %.2f s' % (time.time() - start_time))
#
# def fast_LCS(s1, s2):
#     #Returns the length of the longest common subsequence in strings s1 and s2
#
#     def fast_LCS_helper(s1, s2, memo):
#         if (s1, s2) in memo:
#             return memo[(s1, s2)]
#         if s1 == '' or s2 == '':
#             result = 0
#         elif s1[0] == s2[0]:
#             result = 1 + fast_LCS_helper(s1[1:], s2[1:], memo)
#         else:
#             result = max(fast_LCS_helper(s1, s2[1:], memo), fast_LCS_helper(s1[1:], s2, memo))
#         memo[(s1, s2)] = result
#         return result
#
# def fast_LCS_with_values(s1, s2):
#     def fast_LCS_helper(s1, s2, memo):
#         if (s1, s2) in memo:
#             return memo[(s1, s2)]
#
#         if s1 == "" or s2 == "":
#             result = [0, ""]
#         elif s1[0] == s2[0]:
#             lose_both = fast_LCS_helper(s1[1:], s2[1:], memo)
#             result = [1 + lose_both[0], s1[0] + lose_both[1]]
#         else:
#             useS1 = fast_LCS_helper(s1, s2[1:], memo)
#             useS2 = fast_LCS_helper(s1[1:], s2, memo)
#             if useS1[0] > useS2[0]:
#                 result = useS1
#             else:
#                 result = useS2
#
#         memo[(s1, s2)] = result
#         return result
#
#     return fast_LCS_helper(s1, s2, {})
#
# def subset_memo(target, lst):
#     '''Determines whether or not it is possible to create target sum using the values in the list.
#     Values in list can be positive, negative, or zero.'''
#     last = len(lst) - 1
#     def subset_helper(target, current, memo):
#         if (target, current) in memo:
#             return memo[(target, current)]
#         if target == 0:
#             result = True
#         elif current > last:
#             result = False
#         else:
#             result = subset_helper(target - lst[current], current + 1, memo) or `subset_helper(target, current + 1, memo)
#         memo[(target, current)] = result
#         return result
#
#     # return use_it or lose_it
#
#     return subset_helper(target, 0, {})
#
# print(subset_memo(5, [1, 2, 3, 4]))
