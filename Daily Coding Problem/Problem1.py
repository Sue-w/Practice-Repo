"""This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?"""

def sum_of_two_nums_is_k(a_list, k):

    for i in a_list:
        if k - i in a_list:
            print(f"True because {i} + {k-i} = {k}")
            break


    # -- ALternate Solution --
    # for i in range(len(a_list)):
    #     for j in range(i+1, len(a_list)):
    #         sum_up = a_list[i] + a_list[j]
    #         if sum_up == k:
    #             print(f"True because {a_list[i]} + {a_list[j]} = {k}")

    # -- Alternate Solution --
    #
    # for counter, i in enumerate(a_list):
    #     for sub_counter, j in enumerate(a_list):
    #         if counter >= sub_counter:
    #             continue
    #         elif i + j == k:
    #             print(f"True because {i} + {j} = {k}")



random_list = [1,2,3,4,6,11]

sum_of_two_nums_is_k(random_list, 10)


