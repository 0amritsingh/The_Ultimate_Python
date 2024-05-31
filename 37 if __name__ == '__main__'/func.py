def greet():
    print(f'Namaste!')

print(f'__name__ == {__name__}\nThis is excecuted from the file where the funcation is WRITTEN')
greet()
if __name__=='__main__':
    print(f'__name__ == {__name__}\nThis is excecuted from the file where the funcation is WRITTEN')
    greet()