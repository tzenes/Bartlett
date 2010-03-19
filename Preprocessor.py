
def main():
  file = open('FamiliarQuotations.txt',encoding = 'latin1', mode = 'r');
  lines = file.readlines();
  out = ()
  flag = bool(0)

  for line in lines:
    if line.startswith('FAMILIAR QUOTATIONS.'):
#start of quotes
      flag = bool(1)
      continue
    elif line.startswith('APPENDIX.'):
#end of quotes
      flag = bool(0)
      out = processQuotes(out)
      writeLines('quotesEdited.txt', out)
      out = ()
      continue
    elif line.startswith('INDEX.'):
#start of keywords
      flag = bool(1)
    elif line.startswith('Transcriber\'s Notes:'):
#end of keywords
      flag = bool(0)
      out = processIndex(out)
      writeLines('keywords.txt', out)

    if flag:
      temp = line,
      out = out + temp


def processQuotes(lines):

  state = bool(0)
  out = ()

  for line in lines:
    if line.startswith('_'):
      if not state:
        hold = line.rstrip('[]1234567890-\n') + '\n'
        temp = hold,
        out = out + temp
    elif line.startswith('['):
      state = bool(1)
    elif line.startswith('FOOTNOTE'):
      state = bool(1)
    elif line.startswith('\n'):
      continue
    else:
      state = bool(0)
      hold = line.rstrip('[]1234567890-\n') + '\n'
      temp = hold,
      out = out + temp

  return out

def processIndex(out):
  return out
#this is placeholder... obviously


def writeLines(filename, lines):
  
  file = open(filename, encoding='latin1', mode='w')

  for line in lines:
    file.write(line);


if __name__ == "__main__":
  main()

