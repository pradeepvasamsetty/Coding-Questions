# https://www.hackerrank.com/challenges/s10-weighted-mean/problem

# Python 3
def weighted_mean(numbers, weights):
    total = sum([num*weight for num,weight in zip(numbers,weights)])
    print(round(total / sum(weights),1))

if __name__=="__main__":

    numbers = int(input()) # Not needed; so overwrite var with next input
    numbers = list(map(float, input().split()))
    weights = list(map(float, input().split()))

    weighted_mean(numbers, weights)