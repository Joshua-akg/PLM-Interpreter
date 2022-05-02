from os import listdir
import os

PATH = './'
FILENAME = 'Assignment.jj'
TESTPATH = './tests'
OUTPATH = 'output.txt'
ERRORPATH = 'err.txt'

def main():
    cmd = f'javacc {FILENAME} && javac *.java'
    os.system(cmd)

    tests = os.listdir(TESTPATH)
    print(f'Detected {len(tests)} tests in {TESTPATH}')
    for count, test in enumerate(tests, 1):
        print(
            f'------------------------------------\nRUN TEST: {test} [{count}/{len(tests)}]')
        cmd = f'(java {FILENAME[:-3]} < {TESTPATH}/{test})'
        os.system(cmd)
        print('------------------------------------')


if __name__ == '__main__':
    main()