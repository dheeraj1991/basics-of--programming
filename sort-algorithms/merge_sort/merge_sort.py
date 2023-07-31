# Merge sort is a recursive sort which splits the list by 2 and when merging them backs sorts the two halfs

def merge_sort(l):
    # l is a list of elements
    if len(l) > 1:
        split_index = len(l) // 2
        left = l[:split_index]
        right = l[split_index:]
        left = merge_sort(left)
        right = merge_sort(right)
        
        l_index = len(left) - 1
        r_index = len(right) - 1
        combined_list = []
        while l_index >= 0 and r_index >= 0:
            if left[l_index] > right[r_index]:
                combined_list.insert(0, left[l_index])
                l_index -= 1
            else:
                combined_list.insert(0, right[r_index])
                r_index -= 1
        
        while l_index >= 0:
            combined_list.insert(0, left[l_index])
            l_index -= 1
        
        while r_index >= 0:
            combined_list.insert(0, right[r_index])
            r_index -= 1
        return combined_list
    return l

# Python execution starts from main
if __name__ == "__main__":
    print(merge_sort(['s','g','q','t','s','h','a','n','j']))