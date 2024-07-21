   from operator import itemgetter

   tuples = [(3, 'c'), (1, 'a'), (2, 'b')]
   sorted_tuples = sorted(tuples, key=itemgetter(1))  # Sort by the second element of each tuple
   