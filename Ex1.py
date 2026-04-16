import os;

os.chmod("C:\\temp\\", 0o755);

def main():
    valor: int = 0;
    texto: str = "";
    
    for i in range(10, 151):
        valor = i * i;
        texto += str(valor) + "\n";
        
    gravaArquivo(texto);
    print("Fiz lá com sucesso man");

def gravaArquivo(v):
    dir: str = "C:\\temp\\";
    arq: str = "ex31.txt";
    file: str = "";
    
    enc: str = "utf-8";
    tipo: str = "a";

    if (os.path.exists(dir) and os.path.isdir(dir)):
        file = dir + arq;

        if (os.path.exists(file)):
            tipo = "w";
        
        with open(file, tipo, encoding=enc) as arquivo:
            arquivo.write(v);

if __name__ == "__main__":
    main();

