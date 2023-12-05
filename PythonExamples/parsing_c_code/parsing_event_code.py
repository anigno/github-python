import os
import re

class ParsingEventCode:
    def parse(self, filepath: str):
        with open(file=filepath, mode='r') as file:
            text = file.read()
            pattern = re.compile(r'event_code=(\d+)')
            matches = pattern.findall(text)
            events = set()
            for match in matches:
                print(match)
                events.add(match)
            root, extension = os.path.splitext(filepath)
            out_filepath = f'{root}.out.{extension}'
            with open(file=out_filepath, mode='w+', newline='') as outfile:
                for event in events:
                    outfile.write(f'{event}{os.linesep}')

if __name__ == '__main__':
    parser = ParsingEventCode()
    parser.parse(r'C:\Users\503392062\Downloads\ScoutConfirmGdbLog_Processed-Olga.txt')
