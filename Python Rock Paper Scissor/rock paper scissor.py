#rock paper scissor
# r>s, s>p, p>r

import random
i=0
while i<5:
    def play():
        human = input(f'Input "r" for rock, "p" for paper and "s" for scissor: ').lower()
        computer = random.choice(['r', 'p', 's'])

        if human==computer:
            return 'tie'
        elif win(human, computer):
            return 'Human wins'
        else:
            return('Human loses')

    def win(human, computer):
        if (human=='r' and computer=='s') or (human=='s' and computer=='p') or (human=='p' and computer=='r'):
            return True
    
    print(play())
    i+=1
