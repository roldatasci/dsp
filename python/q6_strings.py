# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    return 'Number of donuts: {}'.format(count) if int(count) < 10 else 'Number of donuts: many'

if __name__ == '__main__':
    print(donuts(4)) # Number of donuts: 4
    print(donuts(9)) # Number of donuts: 9
    print(donuts(10)) # Number of donuts: many
    print(donuts(99)) # Number of donuts: many


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    return '' if len(s) < 2 else s[:2] + s[-2:]

if __name__ == '__main__':
    print(both_ends('spring')) # spng
    print(both_ends('Hello')) # Helo
    print(both_ends('a')) # (no output)
    print(both_ends('xyz')) # xyyz


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    # modif = s[1:]
    # for char in modif:
    #     if char == s[0]
    return s[0] + s[1:].replace(s[0],'*')

if __name__ == '__main__':
    print(fix_start('babble')) # ba**le
    print(fix_start('aardvark')) # a*rdv*rk
    print(fix_start('google')) # goo*le
    print(fix_start('donut')) # donut


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    if len(a) >= 2 and len(b) >= 2: return b[0:2] + a[2:] + ' ' + a[0:2] + b[2:]

if __name__ == '__main__':
    print(mix_up('mix','pod')) # pox mid
    print(mix_up('dog','dinner')) # dig donner
    print(mix_up('gnash','sport')) # spash gnort
    print(mix_up('pezzy','firm')) # fizzy perm


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if len(s) >= 3:
        if s[-3:] != 'ing':
            s += 'ing'
        else:
            s += 'ly'
    return s

if __name__ == '__main__':
    print(verbing('hail')) # hailing
    print(verbing('swiming')) # swimingly
    print(verbing('do')) # do


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    not_idx = s.find('not')
    bad_idx = s.find('bad')
    if bad_idx > not_idx:
        s = s.replace(s[not_idx:bad_idx+3], 'good')
    return s

if __name__ == '__main__':
    print(not_bad('This movie is not so bad')) # This movie is good
    print(not_bad('This dinner is not that bad!')) # This dinner is good!
    print(not_bad('This tea is not hot')) # This tea is not hot
    print(not_bad("It's bad yet not")) # It's bad yet not


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    if len(a) % 2 == 0:
        a_front = a[:int(len(a) / 2)]
        a_back = a[int(len(a) / 2):]
    else:
        a_front = a[:int(len(a) / 2) + 1]
        a_back = a[int(len(a) / 2) + 1:]
    if len(b) % 2 == 0:
        b_front = b[:int(len(b) / 2)]
        b_back = b[int(len(b) / 2):]
    else:
        b_front = b[:int(len(b) / 2) + 1]
        b_back = b[int(len(b) / 2) + 1:]
    return a_front + b_front + a_back + b_back

if __name__ == '__main__':
    print(front_back('abcd','xy')) # abxcdy
    print(front_back('abcde','xyz')) # abcxydez
    print(front_back('Kitten','Donut')) # KitDontenut