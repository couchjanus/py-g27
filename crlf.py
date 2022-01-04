WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

def to_lin(file_path):
  with open(file_path, 'rb') as open_file:
      content = open_file.read()
     
  content = content.replace(UNIX_LINE_ENDING, WINDOWS_LINE_ENDING)

  with open(file_path, 'wb') as open_file:
      open_file.write(content)

def to_win(file_path):
  with open(file_path, 'rb') as open_file:
      content = open_file.read()
     
  content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

  with open(file_path, 'wb') as open_file:
      open_file.write(content)
