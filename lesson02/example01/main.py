import argparse, sys

class CesarS():
    shift = 0

    def __init__(self, shift = 5):
        self.shift = shift

    def decrypt(self, input):
        print('Decrypt with shift =', self.shift)
        result = []
        for i in input:
            result.append(i - self.shift)

        return result

    def encrypt(self, input):
        print('Encrypt with shift =', self.shift)
        result = []
        for i in input:
            result.append(i + self.shift)

        return result

class Substitution():
    dictionary = {
        'A': 'B',
        'B': 'A',
        'C': 'D',
        'D': 'C',
        'E': 'F',
        'F': 'E',
        'G': 'H',
        'H': 'G',
        'I': 'J',
        'J': 'I',
        'K': 'L',
        'L': 'K',
        'M': 'N',
        'N': 'M',
        'O': 'P',
        'P': 'O',
        'R': 'S',
        'S': 'R',
        'T': 'U',
        'U': 'T',
        'V': 'W',
        'W': 'V',
        'Y': 'Z',
        'Z': 'Y',
    }

    def decrypt(self, input):
        print('Decrypt')
        result = []
        for i in input:
            try:
                result.append(self.dictionary[i])
            except:
                result.append(i)

        return result

    def encrypt(self, input):
        print('Encrypt')
        result = []
        for i in input:
            try:
                result.append(self.dictionary[i])
            except:
                result.append(i)

        return result

class Crypt():
    cesar_s = CesarS(7)
    substitution = Substitution()
    input_file = ''
    input_file_content = []
    mode = ''
    output_file = ''
    output_file_content = []
    type = ''

    def __init__(self, input_file, mode, output_file, type):
        self.input_file = input_file
        self.mode = mode
        self.output_file = output_file
        self.type = type

    def read_input_file_content(self):
        try:
            with open(self.input_file, encoding='utf8') as f:
                while (byte := f.read(1)):
                    if self.type == 'cesar':
                        self.input_file_content.append(ord(byte))
                    elif self.type == 'substitution':
                        self.input_file_content.append(byte)
        except FileNotFoundError:
            print('Can not open file')
            sys.exit()

    def run(self):
        print('Mode =', self.mode, 'type =', self.type)
        self.read_input_file_content()
        print(self.input_file_content)

        if self.type == 'cesar':
            algorithm = self.cesar_s
        elif self.type == 'substitution':
            algorithm = self.substitution

        if (self.mode == 'decrypt'):
            self.output_file_content = algorithm.decrypt(self.input_file_content)
        elif (self.mode == 'encrypt'):
            self.output_file_content = algorithm.encrypt(self.input_file_content)
        print(self.output_file_content)
        self.write_output_file_content()

    def write_output_file_content(self):
        try:
            f = open(self.output_file, 'w', encoding='utf8')
            for i in self.output_file_content:
                if self.type == 'cesar':
                    f.write(chr(i))
                elif self.type == 'substitution':
                    f.write(i)
            f.close()
        except IsADirectoryError:
            print('Can not write to directory')
            sys.exit()
        except:
            print('Some other problem')
            sys.exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['decrypt', 'encrypt'], help='mode')
    parser.add_argument('--input', help='input file', required=True)
    parser.add_argument('--output', help='output file', required=True)
    parser.add_argument('type', choices=['cesar', 'substitution'], help='type')
    args = parser.parse_args()

    crypt = Crypt(args.input, args.mode, args.output, args.type)
    crypt.run()
