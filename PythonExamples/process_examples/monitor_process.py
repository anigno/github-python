import subprocess
import time
from typing import Optional, Tuple

class ProcessMonitoring:
    def __init__(self):
        self.process: Optional[subprocess.Popen] = None

    def run_command_line(self, command_line):
        self.process = subprocess.Popen(command_line, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        # self.process = subprocess.Popen(command_line, shell=True)

    def run_and_wait(self, command_line) -> int:
        self.run_command_line(command_line)
        return self.process.wait()

    def get_process_state(self):
        return self.process.poll()

    def get_process_outputs(self) -> Tuple[bytes, bytes]:
        return self.process.communicate()

    def display_output(self):
        # Read and print the output of the process in real-time
        for line in iter(self.process.stdout.readline, b''):
            print(line.decode('utf-8').rstrip())

if __name__ == '__main__':
    pm = ProcessMonitoring()
    print('run1', time.time())
    pm.run_command_line(['dir', 'C:\\Users\\503392062', ''])
    print('run2', time.time())
    while True:
        q = pm.get_process_state()
        if q is not None:
            break
        time.sleep(0.1)
    print('finished', time.time())

    bStd, bErr = pm.get_process_outputs()
    print('all', time.time())
    oStd = str(bStd).split('\\r\\n')
    oErr = str(bErr).split('\\r\\n')
    for i, l in enumerate(oStd):
        print(i, l)
    print(oErr)
