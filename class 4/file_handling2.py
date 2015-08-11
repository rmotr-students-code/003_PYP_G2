"""
Write a function, that receives the path to a text file and sorts all the
lines in the file ascending or descending, depending on the 'sorting'
parameter.

Example:
  sort_lines('file1.txt', sorting='asc')  
  sort_lines('file1.txt', sorting='desc')  
  

"""


def sort_lines(filepath, sorting='asc'):
    
    with open(filepath,"r+") as f:
        line_list = f.readlines() 
    
        if sorting == 'asc':
            line_list.sort()
        elif sorting == 'desc':
            line_list.sort(reverse=True)
            
        f.seek(0)
        f.writelines(line_list)
      

sort_lines('test.txt', sorting='desc')
print("Done")