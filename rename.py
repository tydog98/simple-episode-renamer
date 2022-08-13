import os

print('This script assumes all episodes are already in proper order!')

season = input("Enter season number: ")

if season == '':
    season = '1'

offset = input("Enter episode number to start from: ")

if offset == '':
    offset = '1'

directoryName = input('Enter name of output directory: ')

if directoryName == '':
    directoryName = 'renamed'


def rename():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    count = 0
    for file in files:
        episode = count + int(offset)
        if file == os.path.basename(__file__):
            pass
        else:
            count += 1
            file_extension = os.path.splitext(file)[-1]
            os.rename(file, f'./{directoryName}/s{season.zfill(2)}e{str(episode).zfill(2)}{file_extension}')


if os.path.isdir(directoryName):
    rename()
else:
    os.mkdir(f'./{directoryName}')
    rename()
