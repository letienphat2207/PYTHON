# from tkinter import *
# from tkinter import ttk

# class todo:
#     def __init__(self, root):
#         pass
# def main():
#     root = Tk()
#     ui= todo(root)
#     root.mainloop()   
# if __name__ == "__main__":
#     main()

def main():
   

 from rembg import remove    
 from PIL import Image
 input_path = 'My.jpg'
 output_path='My.png'
 inp = Image.open(input_path)
 output = remove(inp)
 output.save = (output_path)

 from IPython.display import Image,display

 for path in output_path:
    final_img = Image(filename = output_path)
    final_img
    display(final_img)
main()
