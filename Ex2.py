import os;

os.chmod("C:\\temp\\", 0o755);

def main():
    n: int = 0;
    a: int = 0;
    b: int = 1;
    c: int = 0;

    n = int(input("Insira um valor: "));

    if n >= 1:
        gravaValor(a);
        print(a);
    if n >= 2:
        gravaValor(b);
        print(b);
    
    for i in range(2, n):
        c = a + b;
        a = b;
        b = c;
        gravaValor(c);
        print(c);

def gravaValor(num):
    dir: str = "C:\\temp\\";
    arq: str = "ex37.txt";
    file: str = "";
    
    enc: str = "utf-8";
    tipo: str = "a";
    existe: boolean = False;
    
    if (os.path.exists(dir) and os.path.isdir(dir)):
        file = dir + arq;
                
        if num == 0:
            tipo = "w";
            
        with open(file, tipo, encoding=enc) as arquivo:
            arquivo.write(str(num) + "\n");
            
if __name__ == "__main__":
    main();
