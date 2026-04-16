import os;

os.chmod("C:\\temp\\", 0o755);

def main():
    file: str = "C:\\temp\\ex37.txt";
    
    if (os.path.exists(file) and os.path.isfile(file)):
        lerArquivo(file);
    else:
        print("Arquivo não encontrado!");

def lerArquivo(arq):
    valor: int = 0;
    
    with open(arq) as arquivo:
        for line in arquivo:            
            valor = int(line.strip());
            if checaImpar(valor) != -1:
                print(valor, end="\n");

def checaImpar(v):
    if v % 2 == 0:
        return -1;
    else:
        return v;

if __name__ == "__main__":
    main();
