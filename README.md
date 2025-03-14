![image](https://github.com/user-attachments/assets/8843dfdf-ef03-4d5c-ac98-bd89563254ff)

1. Introduction

This is a game origin from "master mind" aka "Bulls and cows", where I would play with my friends during highschool.

2. Game Rules

The game is simple, one person came out with a code that act as the answer (eg. 14155), another person will need to guess the answer via trial & Error. Each round, the guesser will make a guess, and will recieve 2 hint based on the guess, number & position.
For example:
Answer : 3456
Guess : 9953
Number (N) = 2, 3 and 5 are correct 
Position (P) = 1, only 5 is correct 
My usual target is to guess the answer by (number of digit of answer + 2) rounds, So 10 digit answer would take 12 rounds.

3. Current model

As I was learning python, I decided to create a program where it will guess the answer according to your progress as my first project.
Currently, performance is still not as I imagine. You will need to first guess all the numbers, before using the program to guess the answer, which means it can only help to guess the position. 
So, if the answer is 7163, you will first need to guess that 2367 is the number, and use the program to find that 7163 is the correct arrangement.

4. Challenges

One of the challenges I faced is the large amount of possibilities, due to the increase difficulty of the game (where me and my friends will guess 10 numbers or more). 10^10 will result in a number too huge, which is inefficient to process.

5. Optimization

To optimize my current program, I try to introduce an algorithm, where it can use information from lesser guess to come out with a workable set of posibilities. 
Lets compare now vs new algorithm:
Now:![image](https://github.com/user-attachments/assets/a23482a5-d155-467e-a8dc-c74ac3aba674)

You will need to play 8-9 rounds, get the numbers to use the program
1. First list out all the posibilities of already guessed number (eg. 3741990774), which has 151200 posible combination.
2. Then, each combination (act as the answer) vs each guess = get N & P values
3. Check the N & P value with the actual N & P value (from guess and real answer), if not match, remove the single combination from the list and proceed to the next one.
4. I check all the combinations for each guess to know how each guess affect the possible combination.

New algorithm:

You will need to play only 5-6 round, get the numbers to use the program
1. First, enter the possible number and come out with a set of possibilities (eg. 013479) <- stucked
2. Follow above step 2,3,4

My idea is, just guess the type of number, dont need to know each of them individually, (eg. know the answer have 1,2,3,4 , dont need to know the answer have 1111,222,33,4)

6. Mathematical problem

I can't really find the solution to the part where I am stucked, which is the list out all the possibilities of 10 digits combinations, given 6 type of digits. eg ( 1222223456 is one of the combination, type is 123456 )
![image](https://github.com/user-attachments/assets/8836815d-6cf6-4705-8d29-61949436fca9)

I tried asking ChatGPT for solution, but the answer doesn't even make sense. The result is 12,697,896,960, which is even larger than 10^10. 
Without this solution, I cannot proceed to the next step



