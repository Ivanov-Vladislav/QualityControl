import sys

def CorrectTriangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        if a > 0 and b > 0 and c > 0:
            return True
    else:
        return False


def TypeTriangle(a, b, c):
    res = ""
    if CorrectTriangle(a,b,c):
        if (a == b) and (a == c):
            res = "Равносторонний"
        else:
            if (a == b) or (b == c) or (a == c):
                res = "Равнобедренный"
            else:
                res = "Обычный"
    else:
        res = "Нетреугольник"
    return res

def main(list=''):
    side = []
    result = "Неизвестнаяошибка"
    if len(sys.argv) == 4:
        try:
            for count in range(3):
                str = ''
                temp = sys.argv[count+1]
                for c in temp:
                    if c == ',':
                        str += '.'
                    else:
                        str += c
                side.append(float(str))
            if side[0] != 'None' and side[0] != 'None' and side[0] != 'None':
                result = TypeTriangle(side[0], side[1], side[2])
        except:
            result = "Неизвестнаяошибка"
    else:
        if list != '':
            list_temp =''
            for c in list:
                if c == ',':
                    list_temp += '.'
                else:
                    list_temp += c
            if (len(list_temp.split(' ')) == 3):
                try:
                    for count in range(3):
                        side.append(float(list_temp.split(" ")[count]))
                    if side[0] != 'None' and side[0] != 'None' and side[0] != 'None':
                        result = TypeTriangle(side[0], side[1], side[2])
                except ValueError:
                    result = "Неизвестнаяошибка"
            else:
                result = "Неизвестнаяошибка"
    return result

if __name__ == "__main__":
    print(main())