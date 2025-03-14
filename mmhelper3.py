import itertools
import time
import math
from multiprocessing import Pool

#numbers = input('Enter your numbers:')
numbers = '3741990774'
objects = list(numbers)


#length = int(input('How long is the answer:'))
length = 10
permutations = set(itertools.permutations(objects, length))  
unique_permutations_list = [list(perm) for perm in permutations]


#guesslst = list()
#scorelst = list()
#score = [0,0]
#turns = int(input('how many turns have you played?'))


#for i in range(turns):
#    guess = input(f'Turn {i + 1}: ')
#    guess = list(guess)
#    score[0] = int(input(f'Turn {i + 1}: '))
#    score[1] = int(input(f'Turn {i + 1}: '))
#    guesslst += [guess]
#    scorelst += [score[:]]
#
#print(guesslst)
#print(scorelst)
guesslst = [['1', '1', '2', '2', '3', '3', '4', '4', '5', '5'], ['6', '6', '7', '7', '8', '8', '9', '9', '0', '0'], ['2', '4', '6', '8', '0', '1', '3', '5', '7', '9'], ['7', '7', '1', '1', '2', '2', '0', '0', '4', '4'], ['8', '8', '9', '9', '4', '4', '1', '1', '2', '2'], ['4', '4', '2', '6', '6', '0', '2', '7', '1', '1'], ['0', '0', '3', '4', '4', '2', '8', '8', '4', '7'], ['9', '9', '0', '0', '7', '3', '2', '4', '1', '6'], ['3', '7', '4', '1', '9', '9', '0', '7', '7', '4']]
scorelst = [[4, 2], [5, 2], [6, 1], [6, 2], [5, 0], [5, 2], [5, 0], [7, 0], [10, 3]]

x = dict()
for i in range(10):
    x[str(i)] = 0
    
y = dict()
for i in range(20):
    y[str(i)] = 0

def check(num,guesslst,scorelst):
    for guess, target_score in zip(guesslst,scorelst):
        answer = num
        p = 0
        n = 0
        ncount = x.copy()
        acount = x.copy()
        
        for g, ans in zip(guess,answer):
            ncount[g] = ncount.get(g,0) + 1
            acount[ans] = acount.get(ans,0) + 1
            g = int(g)
            ans = int(ans)
            if g == ans:
                p += 1
                
        for value1, value2 in zip(ncount.values(), acount.values()):
            if value1 > 0 and value2 > 0:
                if value2 >= value1:
                    n += value1
                elif value1 > value2:
                    n += value2
            else:
                continue
                
        score = [n,p]
        
        if score != target_score:
            return False
    
    return True

# Function to process a batch of numbers
def process_batch(batch):
    valid_numbers = []

    for num in batch:
        if check(num, guesslst, scorelst):
            valid_numbers.append(num)

    return valid_numbers

def main():
    # Generate a list of 1 million random 10-digit numbers for demonstration
    numbers = unique_permutations_list
    
    print(len(numbers))
    
    start_time = time.time()

    # Split the numbers into batches
    batch_size = 10000
    batches = [numbers[i:i + batch_size] for i in range(0, len(numbers), batch_size)]

    # Use multiprocessing to process each batch in parallel
    with Pool() as pool:
        results = pool.map(process_batch, batches)
 
    # Flatten the list of results
    valid_numbers = [num for batch in results for num in batch]
    
    t =time.time() - start_time
    
    print(f"Valid numbers count: {len(valid_numbers)}")
    p = input('print or not:(1) print\n(2) print & continue\n(3) continue')
    if p == '1':
        print(valid_numbers)
        print('t=',t                 )

if __name__ == "__main__":
    main()
