class Solution:    
    def longestdistance(self, checkpoints):
            # Sort checkpoints from least to greatest
            #type num: list of int
            #return type: int
            
            #TODO: Write code below to returnn an int with the solution to the prompt.
            sorted=[]
            past=0
            for i in checkpoints:
                if(i>past):
                    sorted.append(i)
            for i in range(len(checkpoints)):
                
                # Find the minimum element in remaining
                # unsorted array
                min_idx = i
                for j in range(i+1, len(checkpoints)):
                    if checkpoints[min_idx] > checkpoints[j]:
                        sorted.append(j)      
            print(sorted)
            maxdiff=0
            for i in range(0,len(sorted)-1):
                diff= sorted[i+1]-sorted[i]
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