class Solution:    
    def longestdistance(self, checkpoints):
            # Sort checkpoints from least to greatest
            #type num: list of int
            #return type: int
            
            #TODO: Write code below to returnn an int with the solution to the prompt.
            sorted=[]
            past=0
            for ind in range(len(checkpoints)):
                min_index = ind
    
                for j in range(ind + 1, len(checkpoints)):
                    # select the minimum element in every iteration
                    if checkpoints[j] < checkpoints[min_index]:
                        min_index = j
                # swapping the elements to sort the array
                (checkpoints[ind], checkpoints[min_index]) = (checkpoints[min_index], checkpoints[ind])

            print(checkpoints)

            maxdiff=0
            for i in range(0,len(checkpoints)-1):
                diff= checkpoints[i+1]-checkpoints[i]
                if(diff>maxdiff):
                    maxdiff=diff
            return maxdiff

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.longestdistance(array)
    print(ans)

if __name__ and "__main__":
    main()