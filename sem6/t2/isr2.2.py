from datetime import datetime

def uniqid():
    time_parts = ['%Y', '%m%d', '%H%M%S', '%f']
    while True:
        uniq_id = ''
        time_now = datetime.utcnow()
        for part in time_parts:
            if part == time_parts[0]:
                uniq_id += (str(hex(int(time_now.strftime(part))))[2::])
            else:
                uniq_id += ('-' + str(hex(int(time_now.strftime(part))))[2::])
        yield uniq_id

if __name__ == '__main__':
    uniqid = uniqid()
    n = 40
    for i in range(n):
        print(uniqid.__next__())
