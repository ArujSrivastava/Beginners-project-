# Project 1: Making a mad libs game

def Mad_libs(n):
    if n == 1:
        a = input("Enter a plural noun: ")
        b = input('Enter a wacky state: ')
        c = input("Enter a verb: ")
        d = input("Enter a noun: ")
        e = input("Enter people's name: ")
        f = input("Enter a verb: ")
        g = input("Enter a noun: ")
        u = input("Enter a verb: ")
        v = input("Enter a noun: ")
        h = input("Enter a part of the body: ")
        i = input("Enter an adjective: ")
        j = input("Enter a relative: ")
        k = input("Enter a chain restaurant: ")
        l = input("Enter an adjective (past tense): ")
        m = input("Enter month: ")
        n = input("Enter a verb: ")
        o = input("Enter a noun: ")
        p = input("Enter a verb (past tense)")
        q = input("Enter an adjective: ")
        r = input("Enter a verb: ")
        s = input("Enter same body part as entered above: ")
        t = input("Enter a noun: ")
        print('''\n A''', a, '''in''', b, ''' was arrested this morning after he''', c, '''a
                  In front of''', d, '''.''', e, ''' had a history of''', f, ''', but  
                  no one not even his''', g, '''--ever imagined he'd with a''', u, '''
                  stuck in his''', v, '''

                  "1 always thought he was''', h, ''', but I never thought he'd do something 
                  like this. Even his''', i, '''was surprised 1
                  After a brief''', j, ''', cops followed him to a ''', k, ''', where he reportedly''', l, '''in the fry machine. 
                  In ''', m, ''', a women was charged with a similar crime. But rather than''',
              n, '''with a ''', o, ''', she ''', p, '''with a''', q, '''
                  dog. 

                  Either way, we imagine that after witnessing him''', r, '''with a ''', s, '''there
                  are probably a whole lot of''', t, '''that are going to need some therapy.''')

    elif n == 2:
        a = input("Enter a plural noun: ")
        b = input('Enter a adjective: ')
        c = input("Plural animal name: ")
        d = input("Enter plural noun: ")
        e = input("Enter an adjective: ")
        f = input("Enter a color: ")
        g = input("Enter a adjective: ")
        h = input("Enter a noun: ")
        i = input("Enter a plural noun: ")
        j = input("Enter an adjective: ")
        k = input("Enter a verb: ")
        l = input("Enter a plural noun: ")
        m = input("Enter verb-ed: ")
        n = input("Enter a verb: ")
        o = input("Enter a noun: ")
        p = input("Enter an adjective: ")

        print("Unicorns aren't like other", a + ";\nthey're", b +
              ". They look like", c + ",\nwith", d + " for feet")
        print("and a", e + " mane of hair. But unicorns\nare", f +
              " and have a", g, h + " on their heads. Some", i + " don't")
        print("believe unicorns are", j + " but I")
        print("believe in them. I would love to", k + " a\nunicorn to faraway",
              l + ". One thing\nI've always", m + " about is whether")
        print("unicorns", n + " rainbows, or is thier",
              o + p + " like any other animal's?")

    elif n == 3:
        a = input("Enter a Holiday: ")
        b = input("Enter a noun: ")
        c = input("Enter a place: ")
        d = input("Enter a name or thing: ")
        e = input("Enter an adjective: ")
        f = input("Enter a body part: ")
        g = input("Enter a verb: ")
        h = input("Enter a adjective: ")
        i = input("Enter a noun: ")
        j = input("Enter an food: ")
        k = input("Enter a plural noun: ")
        print('''I can't believe it's already''', a, '''! I can't wait to 
                  put on my''', b, '''and visit every''', c, ''' in my 
                  neighborhood. This year, I am going to dress up as''', d, ''' with''', e, f, '''. Before I''', g, '''
                  I make sure to grab my''', h, i, ''' to hold all of 
                  my ''', j, ''' . Finally, all of my''', k, ''' are ready to go!''')

    else:
        print("There are only 3 stories for Mad libs")
        exit()

    return


n = int(input('''Enter which game you want to play:
          1: Weird News
          2: Unicorn poop
          3: Halloween\n'''))  # Enter 3 single quotes to print in multiple lines using single print statement

Mad_libs(n)
