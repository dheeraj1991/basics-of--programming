# Bubble sort is a very basic sort which compares adjacent elements and swaps it if they are in the wrong order
# Bubble sort time complexity is O(N*N)

def bubble_sort(l):
    # l is a list of elements
    for counter in range(len(l)):
        for index in range(len(l)-(counter+1)):
            if l[index] > l[index + 1]:
                temp = l[index]
                l[index] = l[index+1]
                l[index+1] = temp
    return l

# Python execution starts from main
if __name__ == "__main__":
    print(bubble_sort(['s','g','q','t','s','h','a','n','j']))