import ftplib


ftp = ftplib.FTP('www.google.com')
ftp.login(user='raunit_x', passwd='medepressed')
ftp.cwd('/Users/raunit_x/Desktop/Development')


def grab_file():
    file_name = '/Users/raunit_x/Desktop/random.txt'
    local_file = open(file_name, 'wb')
    ftp.retrbinary('RETR ' + file_name[len(file_name) - file_name[::-1].find('/'):], local_file.write, 1024)
    ftp.quit()
    local_file.close()


def place_file():
    file_name = '/Users/raunit_x/Desktop/random.txt'
    ftp.storbinary('STOR ' + file_name[len(file_name) - file_name[::-1].find('/'):], open(file_name, 'rb'))
    ftp.quit()


place_file()
