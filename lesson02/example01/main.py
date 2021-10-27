import argparse

class CesarS():
    shift = 0

    def __init__(self, shift = '5'):
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

class Crypt():
    cesar_s = CesarS(7)
    input_file = ''
    input_file_content = []
    mode = ''
    output_file = ''
    output_file_content = []

    def __init__(self, input_file, mode, output_file):
        self.input_file = input_file
        self.mode = mode
        self.output_file = output_file

    def read_input_file_content(self):
        with open(self.input_file, encoding='utf8') as f:
            while (byte := f.read(1)):
                self.input_file_content.append(ord(byte))

    def run(self):
        print('Mode =', self.mode)
        self.read_input_file_content()
        print(self.input_file_content)
        if (self.mode == 'decrypt'):
            self.output_file_content = self.cesar_s.decrypt(self.input_file_content)
        elif (self.mode == 'encrypt'):
            self.output_file_content = self.cesar_s.encrypt(self.input_file_content)
        print(self.output_file_content)
        self.write_output_file_content()

    def write_output_file_content(self):
        f = open(self.output_file, 'w', encoding='utf8')
        for i in self.output_file_content:
            f.write(chr(i))
        f.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['decrypt', 'encrypt'], help='mode')
    parser.add_argument('--input', help='input file', required=True)
    parser.add_argument('--output', help='output file', required=True)
    args = parser.parse_args()

    crypt = Crypt(args.input, args.mode, args.output)
    crypt.run()
