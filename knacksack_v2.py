class knap:
    def dp():
        weight_limit = 20 # our max weight limit
        weights = [8,7,6,5,4] # set of our weights 
        values = [1500,1600,1700,1800,3000] # sets of our profits (value)
        tabulation_chart = [[0 for _ in range(weight_limit + 1)] for _ in range(len(weights))] # chart that we will use for the tabulation method

        avaliable_items = [0] * len(weights) # available items we can have in this bag

        row = 0
        for item in range(len(weights)):
            weight = weights[item] # current weight
            value = values[item] # current profit (value)
            for index in range(weight_limit, weight-1, -1):
                column = tabulation_chart[row]
                # we will be getting the possible max weight from the current row we are on depending how many items we have in the set
                tabulation_chart[row][index] = max(value+column[index-weight], column[index]) 
            row += 1

        # for row in tabulation_chart:
        #     print(row)

        # algorithm to detect what items we can put in our bag
        i = len(tabulation_chart) - 1
        j = len(tabulation_chart[0]) - 1

        while j > 0 and i > 0:
            # case 1, if the current value is not the same as the value one row up, then we will add the current value to our bag
            if tabulation_chart[i][j] != tabulation_chart[i-1][j]:
                avaliable_items[i] = 1
                j -= weights[i] # subtract j to the current weight we have
                i -= 1 
            else: # Case 2, the current value is the same as the one above, dont add the current value to the bag
                avaliable_items[i] = 0
                i -= 1

        # print(avaliable_items)

        print("Avaliable items you can put in the bag:")
        total_weight = 0
        total_profit = 0
        for i in range(len(avaliable_items)):
            if avaliable_items[i] == 1:
                print(f"Item {i+1} Weight: {weights[i]} Profit: {values[i]}" )
                total_weight += weights[i]
                total_profit += values[i]

        print(f"Total Weight: {total_weight} Total Profit {total_profit} (Weight Capacity: {weight_limit})")

        return avaliable_items 


if __name__ == "__main__":
    knap.dp()
