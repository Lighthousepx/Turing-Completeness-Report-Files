#to create a Tuing Machine that decides A={0^2^n|n>=0} or the lanuage of strings of 0s whose length is a power of 2

class tmachine:
    def __init__(self,tape,delta,q0,qa,qr): # delta = transitions, q0 = start state, qa/qr = accept or reject
        self.tape = dict(enumerate(tape))
        self.head = 0
        self.qn = q0 #current state
        self.delta = delta
        self.qa = qa
        self.qr = qr
        self.blank = '_' # blank symbol 
    
    def step(self):
        bit = self.tape.get(self.head, self.blank) # symbol tape currently reading
        if (self.qn, bit) not in self.delta: # check valid symbol
            self.qn = self.qr
            return False

        state, write, move = self.delta[(self.qn, bit)]
        
        self.tape[self.head] = write
        self.qn = state
        
        if move == 'R':
            self.head += 1
        elif move == 'L':
            self.head -= 1
        elif move == 'S':
            pass
        # moving the tape head Right or Left or keeping Stationary according to delta
        
        return True
    
    def show(self):
        if not self.tape:
            print('_')
            return
        
        min_bit = min(self.tape.keys())
        max_bit = max(self.tape.keys())
        
        tape_contents = ''
        for a in range(min_bit,max_bit + 1):
            if a == self.head:
                tape_contents += f'[{self.tape.get(a,self.blank)}]'
            else:
                tape_contents += f'[{self.tape.get(a,self.blank)}]'
        
        print(tape_contents, 'state:', self.qn)
    
    def prt_tape(self): 
        min_bit = min(self.tape.keys())
        max_bit = max(self.tape.keys())
        return ''.join(self.tape.get(a,self.blank) for a in range(min_bit,max_bit)) # removes blank at end
    
    
    def run(self, max_moves = 10000): # can be infinite but for testing purposes do not allow to run infinitely
        moves = 0 
        while self.qn not in (self.qa, self.qr) and moves < max_moves:
            self.step()
            moves += 1
        return self.qn == self.qa
    


initial_tape = list('000000000') + ['_']

transitions = { # transition table with all delta functions 
    ('q1','_'): ('qr','_','R'),
    ('q1','x'): ('qr', 'x','R'),
    ('q1','0'): ('q2', '_','R'),
    ('q2','x'): ('q2','x','R'),
    ('q2','_'): ('qa','_','R'),
    ('q2', '0'): ('q3','x','R'),
    ('q3', 'x'): ('q3','x','R'),
    ('q3','0'): ('q4','0','R'),
    ('q3','_'): ('q5','_','L'),
    ('q4', '_'): ('qr','_','R'),
    ('q4', 'x'): ('q4', 'x','R'),
    ('q4','0'): ('q3', 'x', 'R'),
    ('q5','0'): ('q5','0', 'L'),
    ('q5','x'): ('q5', 'x', 'L'),
    ('q5', '_'): ('q2', '_', 'R')}

tm = tmachine(
    tape = initial_tape,
    delta = transitions,
    q0 = 'q1',
    qa = 'qa',
    qr = 'qr')

result = tm.run()

print('Accept' if result else 'Reject')
print(tm.tape)
print(tm.prt_tape())


intial_tape = list('10101011100010011011101') + ['_']

transitions = {
('q0','0'): ('q0','0','R'),
('q0','1'): ('q0','1','R'),
('q0','_'): ('q1','_','L'),

('q1','1'): ('q1','0','L'),
('q1','0'): ('qa','1','S'),
('q1','_'): ('qa','1','S')}


tm = tmachine(tape = intial_tape,
              delta = transitions,
              q0 = 'q0',
              qa = 'qa',
              qr = 'qr')

result = tm.run()
print('Accept' if result else 'Reject')
print(tm.tape)
print(tm.prt_tape())
print(int(tm.prt_tape(),2))



