def getInputs():
    newInput = []
    x, y = input().split(',') # num of snakes and num of ladders
    newInput.append((x, y))
    
    ladders = input().split(' ')
    ladderPoints = {}
    for z in ladders:
        x, y = z.split(',')
        ladderPoints[int(x)] = int(y)
    
    snakes = input().split(' ')
    snakePoints = {}
    for z in snakes:
        x, y = z.split(',')
        snakePoints[int(x)] = int(y)
        
    newInput.append(ladderPoints)
    newInput.append(snakePoints)
    return newInput

def traverseSquare(ladders, snakes, currentSquare):
    # Base case if at the finishline return 0 
    if currentSquare >= 100:
        return 0
    
    ladderDistance = 0
    furthestPoint = 0
    snakeDistance = []
    #Check if there is ladder within a dice rolle of 1-6
    for i in range(1, 7):
        if i + currentSquare in ladders:
            if ladders[i+currentSquare] > furthestPoint:
                furthestPoint = ladders[i + currentSquare]
                ladderDistance = i
    
    #Check if there is snake within a dice rolle of 1-6 
    for i in range(1, 7):
        if i + currentSquare in snakes:
            snakeDistance.append(i)
    #find max distance without a snake
    maxDistance = 0
    for x in range(1,7):
        if x not in snakeDistance:
            maxDistance = x
    
    #computes how many steps if we skip the ladder
    skipladder = traverseSquare(ladders, snakes, currentSquare + maxDistance) + 1
    if ladderDistance != 0:
        # if there is a ladder check the distance a ladder will give us and if it's better than
        # skipping the ladder, use it
        laddersteps = traverseSquare(ladders, snakes, ladders[ladderDistance + currentSquare]) + 1
        if laddersteps < skipladder:
            return laddersteps
        else:
            return skipladder
    #if there is no ladder the steps taken if we skip a ladder
    return skipladder
    

if __name__ == '__main__':
    numOfInputs = int(input())
    for i in range(numOfInputs):    
        inputs = getInputs()
        print(traverseSquare(inputs[1], inputs[2], 1))