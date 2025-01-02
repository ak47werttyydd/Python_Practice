'''
题目：寻找两个有序数组的中位数，空间复杂度为 O(1)
给定两个大小分别为m和n的正序（从小到大）数组nums1和nums2。
请你找出并返回这两个正序数组的中位数。

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
'''

#merge two sorted arrays

# #heap
# #max_heap, min_heap
# #size of a heap= len(nums1)+len(nums2)/2
#
# def find_mid(num1,num2):
#     max_heap=[]
#     min_heap=[]

#merge two sorted arrays, derive the mid index, then find the mid value

#min heap and max heap

#binary search

i=0
j=0
num1=[1,3]
num2=[2,4,7,8,9,10]
count=0
size=len(num1)+len(num2)
odd_even=True if size%2 else False  # True: odd, False: even
cur_val=0

if odd_even: #odd
    mid=size//2
    while i < len(num1) and j < len(num2):
        if num1[i]<num2[j]:
            i+=1
            count+=1
            if mid == count - 1:
                print("Middle value is: ",num1[i-1])
                break
        else:
            j+=1
            count+=1
            if mid == count - 1:
                print("Middle value is: ",num2[i-1])
                break
    #has finished one array
    #finish num1
    while j < len(num2):
        j+=1
        count+=1
        if mid == count - 1:
            print("Middle value is: ",num2[j-1])
            break
    #finish num2
    while i < len(num1):
        i+=1
        count+=1
        if mid == count - 1:
            print("Middle value is: ",num1[i-1])
            break


else: #even
    cur_val=0
    pre_val=0
    mid=size//2  # ( *(mid-1) + *(mid) ) / 2
    while i < len(num1) and j < len(num2):
        if num1[i]<num2[j]:
            cur_val=num1[i]
            i+=1
            count+=1
        else:
            cur_val=num2[j]
            j+=1
            count+=1

        if mid-1 == count-1:
            pre_val=cur_val
        elif mid == count-1:
            print("middle value is: ",(pre_val+cur_val)/2)
            break
    #has finished one array
    while j < len(num2):
        cur_val=num2[j]
        j+=1
        count+=1
        if mid-1 == count-1:
            pre_val=cur_val
        elif mid == count-1:
            print("middle value is: ",(pre_val+cur_val)/2)
            break

    while i < len(num1):
        cur_val=num1[i]
        i+=1
        count+=1
        if mid-1 == count-1:
            pre_val=cur_val
        elif mid == count-1:
            print("middle value is: ",(pre_val+cur_val)/2)
            break







