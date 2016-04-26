import sys

"""
Constructs a solution to traverse an array of integers in the shortest number of
steps starting at index 0. The integer contained in the current index indicates
the amount of steps available to be taken. At any point, the algorithm can step
forward an amount of indices that is no greater than the integer value contained
in the current index. During each step, the algorithm will print how many steps
it has taken. The algorithm is considered done/succesful when you can legally
step beyond the last array element. Once completed, the algorithm should print
the term 'out'.
"""

def read(filename):
    """
    Read file with an int on each line and return a list of integers
    """
    nums = []
    try:
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                nums.append(int(line))
        return nums
    except IOError:
        print("IOError")
        sys.exit()

def calculate_hops_to(nums):
    """
    Given an array of integers where each integer n in an index indicates that
    the program may traverse 0 to n indices forward, calculate how many steps
    are required to get to the ith index. Return an array of the same size with
    the said calculated values.
    EXAMPLE:
        nums          =   [2 ,1 ,1 ,4 ,5 ,1 ,0 ,0 ,3 ,1]
        hops_needed   =   [0 ,1 ,1 ,2 ,3 ,3 ,3 ,3 ,4 ,4]
    """
    hops_needed = [0] # init to 0 since first index is 0 hops
    hop_level = 0
    for i in range(0,len(nums)):
        hops = nums[i]
        if i+hops >= len(hops_needed) and len(nums) != len(hops_needed):
            hop_level = hop_level+1
            for j in range(0,(i+hops - len(hops_needed)+1)):
                hops_needed.append(hop_level)
    return hops_needed

def construct_solution(nums):
    """
    Constructs a solution to traverse an array of integers in the shortest
    number of steps starting at index 0.
    """
    hops_calculated = calculate_hops_to(nums)
    solution = [len(hops_calculated)-1]
    current_hops = hops_calculated[len(hops_calculated)-1]
    for i in range(len(hops_calculated)-1,-1,-1):
        if hops_calculated[i] < current_hops and i + nums[i] >= solution[0]:
            current_hops = hops_calculated[i]
            solution.insert(0,i)
    return solution

def print_solution(solution):
    s = ""
    for i in range(0,len(solution)):
        s = s + str(solution[i]) + ", "
    print(s+"out.")


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        nums = read(filename)
        solution = construct_solution(nums)
        print_solution(solution)
    except IndexError:
        print("Error: a file should be passed in as an argument.")
        sys.exit()
