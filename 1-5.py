"""
1.5 Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become
a2blc5a3. If the "compressed" string would not become smaller than the original
string, your method should return the original string.
"""      
def stringcomp(a):
  previous = None
  result = ''
  repeated = 1
  for current in a:
    print current, repeated
    if current == previous:
      repeated +=1
    else:
      if repeated > 1:
        result += str(repeated)
      result += current
      repeated = 1
    previous = current 

  if repeated > 1:
    print result + str(repeated)
  else:
    print result


#  Sanity checks
stringcomp('aabcccccaaa')
