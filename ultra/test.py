import math

imageList=["1.png","2.png","3.png","4.png","5.png"]

imageSet = [[] * 4 for i in range(int(math.ceil( len(imageList) / 4 )))]

print(imageSet)
# # imageSet = [[],[]]
# for i in range(0, math.ceil( len(imageList) / 4 )):
#     if (len(imageList) >= 4):
#         loops = 4
#     else:
#         loops = (len(imageList) % 4)
#     print("loops",loops)
#     for j in range(0,loops):
#         print("imageSet",imageSet)
#         print(i)
#         newImage = imageList.pop()
#         print(newImage)
#         imageSet[i].append(newImage)

# print(imageSet)