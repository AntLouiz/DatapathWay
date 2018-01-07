# DatapathWay
Um programa que auxilia no estudo de um datapath básico.

## Datapath
O projeto trabalha com o seguinte datapath:
![Datapath Básico](/images/basic_datapath.jpg)

## Começando

### Pré-requisitos
É necessário o [Python 3.x](https://www.python.org/downloads/) instalado no seu computador.

### Baixando o projeto
Utilize o [Git](https://git-scm.com/) para baixar o projeto em sua máquina.
Certifique-se que o **Git** está instalado executando no terminal ```git --version```.
Clone o repósitório em sua máquina executando:
```
        git clone https://github.com/AntLouiz/DatapathWay.git
```

### Executando
Utilize o arquivo **instructions_file.txt.example** como exemplo para a execução do programa.
Renomeie o arquivo **instructions_file.txt.example** para **instructions_file.txt**.
Apague todos os comentários dentro do arquivo.
Entre na pasta do projeto e execute o seguinte comando:

```
        python3 main.py
```

## Exemplo
#### Fazendo uma soma utilizando os comandos **lw**, **add** e **sw**.

Utilizando a linguagem assembly temos os seguintes comandos:

```
        lw $s2, 16($t0)
        lw $s3, 20($t0)
        add $t2, $s2, $s3
        sw $t2, 24($t0)
```

Transformando esses comandos em binário, fica:

```
        10001101000101000000000000010000
        10001101000101010000000000010100
        00000010101101000101000000100000
        10101101000010100000000000011000
```

Insiro esses comandos no **instructions_file.txt** e executo no terminal ```python3 main.py```.
A saída esperada será os caminhos percorridos pelos os principais dados das instruções
que foram inseridas no arquivo.

```
        --------------------------------------------------
        Instruction: 10001101000101000000000000010000
        Type: I
        Operation: lw
        --------------------------------------------------
        Read register 1: 01000
        Read data 1: 10000
        ALU-in-1: 10000
        ALU-in-2: 10000
        ALU-result: 100000
        Address: 100000
        Read data: 1101
        Write data: 1101
        Write register: 10100



        --------------------------------------------------
        Instruction: 10001101000101010000000000010100
        Type: I
        Operation: lw
        --------------------------------------------------
        Read register 1: 01000
        Read data 1: 10000
        ALU-in-1: 10000
        ALU-in-2: 10100
        ALU-result: 100100
        Address: 100100
        Read data: 1100
        Write data: 1100
        Write register: 10101



        --------------------------------------------------
        Instruction: 00000010101101000101000000100000
        Type: R
        Operation: add
        --------------------------------------------------
        Read the register 1: 10101
        Read the register 2: 10100
        Read data 1: 1100
        Read data 2: 1101
        ALU-in-1: 1100
        ALU-in-2: 1101
        ALU-result: 11001
        Write data: 11001
        Write register: 01010



        --------------------------------------------------
        Instruction: 10101101000010100000000000011000
        Type: I
        Operation: sw
        --------------------------------------------------
        Read the register 1
        Read the register 2
        Read data 1: 10000
        Read data 2: 11001
        ALU-in-1: 10000
        ALU-in-2: 11000
        ALU-result: 101000
        Address: 101000
        Write data: 11001
```

## Observações

### Registradores temporários e valores salvos:
* $t0-$t7 :: 8 - 15
* $s0-$s7 :: 16 - 23
* $t8-$t9 :: 24 - 25

### Memória:
* A memória contém apenas 256 endereços.
* A memória contém valores randômicos de 1 a 200.
* O registrador $t0 tem o valor 16.
* Operações que foram implementadas:

        - lw
        - sw
        - add
        - sub
        - and
        - or
