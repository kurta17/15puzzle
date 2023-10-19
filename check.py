# tiles = [2,1,3,4,8,7,6,5,9,10,11,12,15,14,13]
# def n_inversion(arr):
#     count = 0
    
#     for i in range(len(arr)):
#         for x in range(i + 1, len(arr)) :
#             if arr[i] > arr[x]:
#                 count += 1
#     return count

# print(n_inversion(tiles))
# def random_tiles():
    
#     if n_inversion(tiles) % 2 == 0 :
#         tiles[0], tiles[1] = tiles[1], tiles[0]

#     return tiles


# print(random_tiles())