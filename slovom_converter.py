
one = ["", "един ", "два ", "три ", "четири ",
       "пет ", "шест ", "седем ", "осем ",
       "девет ", "десет ", "единадесет ", "дванадесет ",
       "тринадесет ", "четиринадесет ", "петнадесет ",
       "шестнадесет ", "седемнадесет ", "осемнадесет ",
       "деветнадесет "]

ten = ["", "", "двадесет ", "тридесет ", "четиридесет ",
       "петдесет ", "шестдесет ", "седемдесет ", "осемдесет ",
       "деветдесет "]

hundred = ["", "сто", "двеста", "триста", "четиристотин",
           "петстотин", "шестстотин", "седемстотин", "осемстотин",
           "деветстотин"]


# n is 1- or 2-digit number
def num_to_words(n, s):
    str = ""

    # if n is more than 19, divide it
    if n > 19:
        str += ten[n // 10] + one[n % 10]
        if n > 100:
            str += hundred[n // 10] + ten[n // 10] + one[n % 10]
    else:
        str += one[n]

    if n:
        str += s

    return str


def conv_single_thousand(n):
    # stores word representation of given
    # number n
    out = ""
    # handles digits at ten millions and
    # hundred millions places (if any)
    out += num_to_words((n // 1000000),
                        "милион ")

    # handles digits at hundred thousands
    # and one millions places (if any)
    out += num_to_words(((n // 100000) % 100),
                        "сто хиляди ")

    # handles digits at thousands and tens
    # thousands places (if any)
    out += num_to_words(((n // 1000) % 100),
                        "хиляда ")

    # handles digit at hundreds places (if any)
    out += num_to_words(((n // 100) % 10),
                        "сто ")

    if n > 100 and n % 100:
        out += "и "

    # handles digits at ones and tens
    # places (if any)
    out += num_to_words((n % 100), "")


    n_str = str(n)
    n_len = len(n_str)
    out_list = str.split(out)

    if n_len < 3:
        if n > 20 and n_str[-1] != "0":
            out_list.insert(1, "и")
        out = " ".join(out_list)

    if n_len == 3:
        index = int(n_str[-3])
        hundreds_str = hundred[index]
        out_list[1] = hundreds_str

        if n_str[-2] == "0" and n_str[-1] == "0":
            index = int(n_str[-3])
            hundreds_str = hundred[index]
            out_list.pop(0)
            out = hundreds_str
        elif n_str[-1] != "0" or n_str[-2] != "0":
            out_list.pop(0)
            ten_digits = int(n_str[-2] + n_str[-1])
            out = " ".join(out_list)
            if 20 < ten_digits < 100:
                out_list.pop(1)
                out_list.insert(2, "и")
                if n_str[-1] == "0":
                    out_list.pop(-1)
                    out_list.insert(1, "и")
            out = " ".join(out_list)

    if 3 < n_len <= 6:
        if n_len == 4 and n_str[-4] == "1":

            ten_digits = int(n_str[-2] + n_str[-1])
            hundred_digits = int(n_str[-3] + n_str[-2] + n_str[-1])

            # correcting thousand /plural/ single 1000
            if n_str[-4] == "1" and n_str[-3] == "0" and n_str[-2] == "0" and n_str[-1] == "0":
                out_list.pop(0)
                out = " ".join(out_list)

            else:
                if n_str[-4] == "1":
                    out_list.pop(0)
                    out = " ".join(out_list)
                if 20 < ten_digits < 100:
                    out_list.pop(1)
                    out_list.insert(2, "и")
                    out = " ".join(out_list)

                if n_str[-1] == "0":
                    if n_str[-2] != "0":
                        if n_str[-3] == "0" and n_str[-1] == "0" and n_str[-2] == "1":
                            out = " ".join(out_list)
                        elif n_str[-3] == "0" and n_str[-1] == "0" and n_str[-2] != "2":
                            out_list.pop(2)
                            out_list.insert(1, "и")
                            out = " ".join(out_list)
                        else:
                            if n_str[-2] != "1" and n_str[-2] != "2":
                                out_list.pop(2)
                                out = " ".join(out_list)
                            elif n_str[-3] != "0":
                                out_list.pop(1)
                                out = " ".join(out_list)
                    else:
                        out_list.pop(2)
                        out = " ".join(out_list)
                if n_str[-1] == "0" and n_str[-2] == "0":
                    index = int(n_str[-3])
                    hundreds_str = hundred[index]
                    out_list.pop(-1)
                    out_list.append(hundreds_str)
                    out_list.insert(1, "и")
                    out = " ".join(out_list)
                # correcting whole hundreds
                if n_str[-3] != "0" and n_str[-2] == "0" and n_str[-1] == "0":
                    out_list.pop(1)
                    out_list.insert(1, "и")
                    index = int(n_str[-3])
                    thousands_str = hundred[index]
                    out_list.insert(1, thousands_str)
                    out_list.pop(-1)
                    out_list.pop(-1)
                    out_list.insert(1, "и")
                    out = " ".join(out_list)
                if n_str[-3] != "0":
                    index = int(n_str[-3])
                    thousands_str = hundred[index]
                    out_list.insert(1, thousands_str)
                    if n_str[-1] != "0" and n_str[-3] != "0":
                        out_list.pop(1)
                        out_list.pop(1)
                        out_list[1] = thousands_str
                        out = " ".join(out_list)
                if n_str[-1] != "0" and n_str[-3] != "0" and n_str[-2] != "1":
                    if n_str[-2] == "0":
                        pass
                    else:
                        out_list.pop(2)
                        out_list.insert(3, "и")
                        out = " ".join(out_list)
                if n_str[-3] != "0" and n_str[-1] == "0":
                    out_list.pop(2)
                    out = " ".join(out_list)
                    if n_str[-1] == "0" and n_str[-2] == "0":
                        out_list[1] = "и"
                        out = " ".join(out_list)

        if n_len == 4 and n_str[-4] != "1":
            if n_str[0] == "2":
                out_list[0] = "две"

            out_list[1] = "хиляди"
            out = " ".join(out_list)

            ten_digits = int(n_str[-2] + n_str[-1])

            # correcting thousand /plural/ single 1000
            if n_str[-3] == "0" and n_str[-2] == "0" and n_str[-1] == "0":
                out = " ".join(out_list)

            else:
                if 20 < ten_digits < 100:
                    out_list.pop(1)
                    out_list.insert(2, "и")
                    out_list.insert(1, "хиляди")
                    out_list.pop(2)
                    out_list.pop(2)
                    out_list.insert(-2, "и")
                    if n_str[-3] == "0" and n_str[-1] == "0":
                        out_list.pop(1)
                        out_list.insert(2, "и")

                if n_str[-1] == "0":
                    if n_str[-2] != "0":
                        if n_str[-3] == "0" and n_str[-1] == "0" and n_str[-2] != "2":
                            out_list.pop(2)
                            out_list.insert(1, "и")
                        else:
                            hundred_digits = int(n_str[-3])
                            if n_str[-2] != "1" and n_str[-2] != "2":
                                out_list.pop(2)
                                out_list[2] = hundred[hundred_digits]
                                out = " ".join(out_list)
                            elif n_str[-3] != "0":
                                out_list.pop(1)
                                out_list[1] = "хиляди"
                                out_list[2] = hundred[hundred_digits]
                                out = " ".join(out_list)

                if n_str[-1] == "0" and n_str[-2] == "0":
                    index = int(n_str[-3])
                    hundreds_str = hundred[index]
                    out_list.pop(-1)
                    out_list.append(hundreds_str)
                    out_list.insert(2, "и")
                    out_list.pop(-2)
                    out = " ".join(out_list)

                if n_str[-1] != "0" and n_str[-3] != "0" and n_str[-2] != "1":
                    if n_str[-2] == "0":
                        pass
                    else:
                        out_list.pop(2)
                        out_list.pop(2)
                        out_list.pop(2)
                        out_list.insert(3, "и")
                        if n_str[2] != "0":
                            index = int(n_str[-3])
                            hundreds_str = hundred[index]
                            out_list.insert(2, hundreds_str)
                            out = " ".join(out_list)
                if n_str[-3] == "0":
                    ten_digits = int(n_str[-2] + n_str[-1])
                    if 20 < ten_digits < 100 and n_str[-1] != "0":
                        out_list.pop(2)
                        out_list.insert(-1, "и")
                        out = " ".join(out_list)

                if n_str[-3] != "0" and n_str[-2] != "0" and n_str[-1] != "0":
                    ten_digits = int(n_str[-2] + n_str[-1])
                    if 10 < ten_digits < 20:
                        index = int(n_str[-3])
                        hundreds_str = hundred[index]
                        out_list.insert(2, hundreds_str)
                        out_list.pop(3)
                        out_list.pop(3)
                        out = " ".join(out_list)
                if n_str[-3] != "0" and n_str[-2] == "0" and n_str[-1] != "0":
                    out_list.pop(2)
                    out_list.pop(2)
                    index = int(n_str[-3])
                    hundreds_str = hundred[index]
                    out_list.insert(2, hundreds_str)
                    out = " ".join(out_list)

    return out


def conv_hundred(n):
    # stores word representation of given
    # number n
    out = ""
    # handles digits at ten millions and
    # hundred millions places (if any)
    out += num_to_words((n // 1000000),
                        "милион ")

    # handles digits at hundred thousands
    # and one millions places (if any)
    out += num_to_words(((n // 100000) % 100),
                        "сто хиляди ")

    # handles digits at thousands and tens
    # thousands places (if any)
    out += num_to_words(((n // 1000) % 100),
                        "хиляда ")

    # handles digit at hundreds places (if any)
    out += num_to_words(((n // 100) % 10),
                        "сто ")

    if n > 100 and n % 100:
        out += "и "

    # handles digits at ones and tens
    # places (if any)
    out += num_to_words((n % 100), "")

    # format string lingua

    n_str = str(n)
    n_len = len(n_str)
    out_list = str.split(out)

    if n_len < 3:
        if n > 20 and n_str[-1] != "0":
            out_list.insert(1, "и")
        out = " ".join(out_list)

    if n_len == 3:
        index = int(n_str[-3])
        hundreds_str = hundred[index]
        out_list[1] = hundreds_str

        if n_str[-2] == "0" and n_str[-1] == "0":
            index = int(n_str[-3])
            hundreds_str = hundred[index]
            out_list.pop(0)
            out = hundreds_str
        elif n_str[-1] != "0" or n_str[-2] != "0":
            out_list.pop(0)
            ten_digits = int(n_str[-2] + n_str[-1])
            out = " ".join(out_list)
            if 20 < ten_digits < 100:
                out_list.pop(1)
                out_list.insert(2, "и")
                if n_str[-1] == "0":
                    out_list.pop(-1)
                    out_list.insert(1, "и")
            out = " ".join(out_list)

    return out


def conv_thousands(n):
    n_str = str(n)
    n_len = len(n_str)
    slovom_str = ""
    if n_len <= 4:
        return conv_single_thousand(n)
    if n_len == 5:
        n_list = [*n_str]
        hundreds_str = str(n_list[2] + n_list[3] + n_list[4])
        hundreds_num = int(hundreds_str)
        if hundreds_num == 0:
            hundreds_words_string = "000"
        else:
            hundreds_words_string = conv_single_thousand(hundreds_num)

        ten_thousands_str = str(n_list[0] + n_list[1])
        ten_thousands_num = int(ten_thousands_str)
        ten_thousands_words = conv_single_thousand(ten_thousands_num)
        slovom_list = (ten_thousands_words + " хиляди " + hundreds_words_string).split()
        if hundreds_words_string == "000":
            slovom_list.pop(-1)
        else:
            if n_str[-3] == "0" and n_str[-2] == "0":
                slovom_list.insert(-1, "и")

            if n_str[-1] == "0":
                slovom_list.insert(-1, "и")
                if n_str[-2] == "1":
                    slovom_list.pop(-2)
                if n_str[-3] != "0":
                    slovom_list.pop(-2)
            if n_str[-2] == "1" and n_str[-1] == "0":
                slovom_list.insert(-1, "и")
            ten_digits = int(n_str[-2] + n_str[-1])
            if 10 < ten_digits < 20:
                slovom_list.insert(-1, "и")
                if n_str[-3] != "0":
                    slovom_list.pop(-2)
            if n_str[-3] != "0" and n_str[-2] == "0" and n_str[-1] == "0":
                slovom_list.insert(-1, "и")

        slovom_str = " ".join(slovom_list)

        if n_str[-4] == "1" or n_str[-4] == "2":
            if n_str[-4] == "1":
                pass

            if n_str[-4] == "2":
                for i in range(len(slovom_list)):
                    if slovom_list[i] == 'два':
                        slovom_list[i] = 'две'

            slovom_str = " ".join(slovom_list)
        return slovom_str

    if n_len == 6:
        n_list = [*n_str]
        hundreds_str = str(n_list[3] + n_list[4] + n_list[5])
        hundreds_num = int(hundreds_str)
        if hundreds_num == 0:
            hundreds_words_string = "000"
        else:
            hundreds_words_string = conv_single_thousand(hundreds_num)
        hundred_thousands_str = str(n_list[0] + n_list[1] + n_list[2])
        hundred_thousands_num = int(hundred_thousands_str)
        hundred_thousands_words = conv_single_thousand(hundred_thousands_num)
        slovom_list = (hundred_thousands_words + " хиляди " + hundreds_words_string).split()
        slovom_str = " ".join(slovom_list)
        if hundreds_words_string == "000":
            slovom_list.pop(-1)
            slovom_str = " ".join(slovom_list)
        else:
            if n_str[-3] == "0" and n_str[-2] == "0":
                slovom_list.insert(-1, "и")
                slovom_str = " ".join(slovom_list)
            if n_str[-1] == "0":
                slovom_list.insert(-1, "и")
                slovom_str = " ".join(slovom_list)
                if n_str[-2] == "1":
                    slovom_list.pop(-2)

                if n_str[-3] != "0":
                    slovom_list.pop(-2)
                    if n_str[-1] == "0" and n_str[-2] != "0":
                        slovom_list.pop(-2)
                        slovom_list.insert(-1, "и")
                        slovom_str = " ".join(slovom_list)
            if n_str[-2] == "1" and n_str[-1] == "0":
                slovom_list.insert(-1, "и")
                if n_str[-3] != "0":
                    index = int(n_str[-3])
                    hundreds_str = hundred[index]
                    slovom_list.insert(-2, hundreds_str)
                    slovom_list.pop(-4)
                    slovom_str = " ".join(slovom_list)
            ten_digits = int(n_str[-2] + n_str[-1])
            if 10 < ten_digits < 20:
                slovom_list.insert(-1, "и")
                slovom_str = " ".join(slovom_list)
                if n_str[-3] != "0":
                    slovom_list.pop(-2)
                    slovom_str = " ".join(slovom_list)
            if n_str[-3] != "0" and n_str[-2] == "0" and n_str[-1] == "0":
                slovom_list.insert(-1, "и")
                slovom_str = " ".join(slovom_list)

        if n_str[-4] == "1" or n_str[-4] == "2":
            if n_str[-4] == "1":
                for i in range(len(slovom_list)):
                    if slovom_list[i] == 'един':
                        slovom_list[i] = 'една'

            if n_str[-1] == "1" and hundreds_str != 000:
                slovom_list[-1] = 'един'

            if n_str[-4] == "2":
                for i in range(len(slovom_list)):
                    if slovom_list[i] == 'два':
                        slovom_list[i] = 'две'

            if n_str[-1] == "2" and hundreds_str != 000:
                slovom_list[-1] = 'два'

            slovom_str = " ".join(slovom_list)

    return slovom_str


def conv_millions(n):
    n_str = str(n)
    nlen = len(n_str)
    n_list = [*n_str]
    millions_n = int(n_str[0])
    hundreds_str = str(n_list[-3] + n_list[-2] + n_list[-1])
    hundred_thousands_str = str(n_list[-6] + n_list[-5] + n_list[-4])
    slovom_str = ""

    if nlen == 7:
        if n_str[-7] == "1":
            if hundreds_str == "000" and hundred_thousands_str == "000":
                slovom_str = one[millions_n] + "милион "
            elif hundreds_str != "000" and hundred_thousands_str == "000":
                if int(hundreds_str) < 101:
                    slovom_str = one[millions_n] + "милион и " + conv_thousands(int(hundreds_str))
                if int(hundreds_str) > 100:
                    slovom_str = one[millions_n] + "милион " + conv_thousands(int(hundreds_str))
                if n_str[-1] == "0" and n_str[-2] == "0" and int(hundreds_str) > 100:
                    slovom_str = one[millions_n] + "милион и " + conv_thousands(int(hundreds_str))

            elif hundred_thousands_str != "000":
                slovom_str = one[millions_n] + "милион " + conv_thousands(int(hundred_thousands_str + hundreds_str))
                if hundreds_str == "000":
                    slovom_str = one[millions_n] + "милион и " + conv_thousands(
                        int(hundred_thousands_str + hundreds_str))
        else:
            if hundreds_str == "000" and hundred_thousands_str == "000":
                slovom_str = one[millions_n] + "милионa "
            elif hundreds_str != "000" and hundred_thousands_str == "000":
                if int(hundreds_str) < 101:
                    slovom_str = one[millions_n] + "милионa и " + conv_thousands(int(hundreds_str))
                if int(hundreds_str) > 100:
                    slovom_str = one[millions_n] + "милионa " + conv_thousands(int(hundreds_str))
                if n_str[-1] == "0" and n_str[-2] == "0" and int(hundreds_str) > 100:
                    slovom_str = one[millions_n] + "милионa и " + conv_thousands(int(hundreds_str))

            elif hundred_thousands_str != "000":
                slovom_str = one[millions_n] + "милионa " + conv_thousands(int(hundred_thousands_str + hundreds_str))
                if hundreds_str == "000":
                    slovom_str = one[millions_n] + "милионa и " + conv_thousands(
                        int(hundred_thousands_str + hundreds_str))


    if 7 < nlen < 10:
        milions_list = n_list[:-6]
        milions_digits_list = n_list[-6:]
        milions_str = "".join(milions_list)
        milions_digits_str = "".join(milions_digits_list)
        milions_words = conv_hundred(int(milions_str))
        milions_digits_words = conv_thousands(int(milions_digits_str))
        hundreds_str = milions_digits_str[3:]
        hundred_thousands_str = milions_digits_str[:3]

        slovom_str = milions_words + " милиона " + milions_digits_words

        if hundreds_str == "000" and hundred_thousands_str == "000":
            slovom_str = milions_words + " милиона " + milions_digits_words

        if int(hundreds_str) <= 20 and nlen > 7:
            slovom_str = milions_words + " милиона " + milions_digits_words
        if int(hundreds_str) % 10 == 0 and int(hundreds_str) != 10 and int(hundreds_str) != 20 and int(
                hundred_thousands_str) == 0:
            slovom_str = milions_words + " милиона  " + milions_digits_words
        if hundreds_str != "000" and hundred_thousands_str == "000":
            slovom_str = milions_words + " милиона " + milions_digits_words

        if int(hundreds_str) < 101 and hundreds_str[0] == "0" and hundred_thousands_str == "000":
            slovom_str = milions_words + " милиона и " + milions_digits_words

        if int(hundreds_str) % 100 == 0 and int(hundred_thousands_str) == 0:
            slovom_str = milions_words + " милиона и " + milions_digits_words
        if int(hundred_thousands_str) % 100 == 0 and int(hundreds_str) == 0:
            slovom_str = milions_words + " милиона и " + milions_digits_words
        if (int(milions_str) > 0 and hundred_thousands_str[0] == "0"
                and hundred_thousands_str[1] != "0" and hundreds_str == "000"):
            slovom_str = milions_words + " милиона и " + milions_digits_words
        if (int(milions_str) > 0 and hundred_thousands_str[0] == "0"
                and hundred_thousands_str[1] == "0" and hundred_thousands_str[2] != "0" and hundreds_str == "000"):
            slovom_str = milions_words + " милиона и " + milions_digits_words
        if (int(milions_str)) > 0 and hundred_thousands_str == "000" and hundreds_str == "000":
            slovom_str = milions_words + " милиона " + milions_digits_words
    return slovom_str


def converter(n):
    n_str = str(n)

    if n < 1000000:
        return conv_thousands(n)
    else:
        return conv_millions(n)


def cents_convert(n):
    cents_words = conv_thousands(n)
    cents_list = cents_words.split()

    for i in range(len(cents_list)):
        if cents_list[i] == "един":
            cents_list[i] = "една"
        if cents_list[i] == "два":
            cents_list[i] = "две"

    cents_words = " ".join(cents_list)

    return cents_words


def input_split(n):

    if n.isdigit():
        integers = int(n)
        if integers > 1000000000:
            return "Числото e твърде голямо"

        whole_numbers = converter(integers)

        if integers < 2:

            if integers == 0:
               return "Нула"           
            if integers == 1:
                return whole_numbers + " лев"
        else:
            return whole_numbers + " лева"
    else:
        n_list = [*n]
        for symbol in n_list:
            digit_list = []
            dot_list = []
            if symbol.isdigit():
                digit_list.append(symbol)
            if symbol == "," or symbol == ".":
                dot_list.append(symbol)
                if len(dot_list) > 1:
                    return "Ползвайте една точка или запетая"
                if "." in n_list:
                    for i in n:
                        if i == ".":
                            n_list = n.split(".")
                    if len(n_list) < 2:
                        integers = int(n.replace(".", ""))
                        decimals = 0
                    else:
                        integers_trunkated = "0" + n_list[0]
                        integers = int(integers_trunkated)
                        if integers > 1000000000:
                            return "Числото е твърде голямо"
                        decimal_truncated = str(n_list[1])
                        if len(decimal_truncated) > 2:
                            return "Ползвайте до две цифри след точка или запетая"
                        if len(decimal_truncated) == 1:
                            decimal_truncated = decimal_truncated + "0"
                        if len(decimal_truncated) == 0:
                            return "Ползвайте до две цифри след точка или запетая"
                        decimal_trunk = decimal_truncated[:2]
                        decimals = int(decimal_trunk)
                        whole_numbers = converter(integers)
                        decimal_numbers = cents_convert(decimals)
                        if decimals == 0:
                            if integers < 2:
                                return whole_numbers + " лев"
                            else:
                                return whole_numbers + " лева"
                        else:
                            if integers < 2 and decimals > 1:
                                if integers == 0:
                                    return decimal_numbers + " стотинки "
                                else:
                                    return whole_numbers + " лев и " + decimal_numbers + " стотинки "
                            elif decimals < 2 and integers > 1:
                                if integers == 0:
                                    return decimal_numbers + " стотинка "
                                else:
                                    return whole_numbers + " лева и " + decimal_numbers + " стотинка "
                            elif integers < 2 and decimals < 2:
                                if integers == 0:
                                    return decimal_numbers + " стотинка "
                                else:
                                    return whole_numbers + " лев и " + decimal_numbers + " стотинка "
                            elif integers >= 2 and decimals >= 2:
                                return whole_numbers + " лева и " + decimal_numbers + " стотинки "

                if "," in n_list:
                    for i in n:
                        if i == ",":
                            n_list = n.split(",")
                    if len(n_list) < 2:
                        integers = int(n.replace(",", ""))
                        decimals = 0
                    else:
                        integers_trunkated = "0" + n_list[0]
                        integers = int(integers_trunkated)
                        decimal_truncated = str(n_list[1])
                        if len(decimal_truncated) > 2:
                            return "Ползвайте до две цифри след точка или запетая"
                        if len(decimal_truncated) == 1:
                            decimal_truncated = decimal_truncated + "0"
                        decimal_trunk = decimal_truncated[:2]
                        decimals = int(decimal_trunk)
                        whole_numbers = converter(integers)
                        decimal_numbers = cents_convert(decimals)
                        if decimals == 0:
                            if integers < 2:
                                return whole_numbers + " лев"
                            else:
                                return whole_numbers + " лева"
                        else:
                            if integers < 2 and decimals > 1:
                                if integers == 0:
                                    return decimal_numbers + " стотинки "
                                else:
                                    return whole_numbers + " лев и " + decimal_numbers + " стотинки "
                            elif decimals < 2 and integers > 1:
                                if integers == 0:
                                    return decimal_numbers + " стотинка "
                                else:
                                    return whole_numbers + " лева и " + decimal_numbers + " стотинка "
                            elif integers < 2 and decimals < 2:
                                if integers == 0:
                                    return decimal_numbers + " стотинка "
                                else:
                                    return whole_numbers + " лев и " + decimal_numbers + " стотинка "
                            elif integers >= 2 and decimals >= 2:
                                return whole_numbers + " лева и " + decimal_numbers + " стотинки "
            elif not symbol.isdigit():
                return "Попълнете цяло число или дробно число до две цифри след точката или запетаята"

