class azencode:

    def encode(self, text, loops=10):
        output_str = ""
        strs = ""
        strslist = list(text)

        strings = {
            'a':'V', 'b':'^', 'c':'M', 'd':'=', 'e':'a', 'f':'-', 'g':'p', 
            'h':'%', 'i':',', 'j':')', 'k':'w', 'l':'H', 'm':'c', 'n':'5', 
            'o':'m', 'p':'X', 'q':"'", 'r':'Z', 's':'r', 't':'&', 'u':'Y', 
            'v':'G', 'w':'l', 'x':'i', 'z':'s', 'y':'[', 'A':'L', 'B':'6', 
            'C':'T', 'D':'"', 'E':'I', 'F':'/', 'G':'U', 'H':'h', 'I':'J', 
            'J':'P', 'K':'j', 'L':'n', 'M':'t', 'N':']', 'O':'E', 'P':'7', 
            'Q':'D', 'R':'.', 'S':' ', 'T':'u', 'U':'O', 'V':'A', 'W':'g', 
            'X':'@', 'Z':'d', 'Y':'W', '/':'0', '\\':'*', '.':'K', ';':'_', 
            '"':'e', "'":'\\', ']':'!', '[':'B', '+':'$', '1':'b', '2':'3', 
            '3':'2', '4':'|', '5':'~', '6':'Q', '7':'9', '8':'o', '9':'R', 
            '0':'(', ':':':', '|':'x', ',':'C', '=':';', '-':'q', '_':'y', 
            '!':'N', '@':'8', '#':'4', '$':'1', '%':'f', '^':'F', '&':'k', 
            '*':'#', '(':'+', ')':'S', '~':'z', ' ':'v', '`':'`'}
        
        for i in strslist:
            strs += strings[i]

        strslists = list(strs)
        
        for x in range(0, loops):
            count = 0
            for e in strslists:
                strslists[count] = strings[e]
                count += 1
        

        for output in strslists:
            output_str += output
        

        return output_str[::-1]
    


    def decode(self, text, loops=10):
        output_str = ""
        strs = ""
        strslist = list(text)

        strings = {
            'V':'a', '^':'b', 'M':'c', '=':'d', 'a':'e', '-':'f', 'p':'g', 
            '%':'h', ',':'i', ')':'j', 'w':'k', 'H':'l', 'c':'m', '5':'n', 
            'm':'o', 'X':'p', "'":'q', 'Z':'r', 'r':'s', '&':'t', 'Y':'u', 
            'G':'v', 'l':'w', 'i':'x', 's':'z', '[':'y', 'L':'A', '6':'B', 
            'T':'C', '"':'D', 'I':'E', '/':'F', 'U':'G', 'h':'H', 'J':'I', 
            'P':'J', 'j':'K', 'n':'L', 't':'M', ']':'N', 'E':'O', '7':'P', 
            'D':'Q', '.':'R', ' ':'S', 'u':'T', 'O':'U', 'A':'V', 'g':'W', 
            '@':'X', 'd':'Z', 'W':'Y', '0':'/','*':'\\', 'K':'.', '_':';', 
            'e':'"','\\':"'", '!':']', 'B':'[', '$':'+', 'b':'1', '3':'2', 
            '2':'3', '|':'4', '~':'5', 'Q':'6', '9':'7', 'o':'8', 'R':'9', 
            '(':'0', ':':':', 'x':'|', 'C':',', ';':'=', 'q':'-', 'y':'_', 
            'N':'!', '8':'@', '4':'#', '1':'$', 'f':'%', 'F':'^', 'k':'&', 
            '#':'*', '+':'(', 'S':')', 'z':'~', 'v':' ', '`':'`'}
        
        for i in strslist:
            strs += strings[i]
        
        strslists = list(strs)

        for x in range(0, loops):
            count = 0
            for e in strslists:
                strslists[count] = strings[e]
                count += 1 

        
        for output in strslists:
            output_str += output
        
        return output_str[::-1]
    

    
    def chrencncode(self, text):#Don't Use This
        output_str = ""
        strs = ""
        strslist = list(text)

        for i in strslist:
            strs += chr((ord(i) + 12))

        strslists = list(strs)
        
        for output in strslists:
            output_str += output
        

        return output_str[::-1]
    

    
    def chrdecode(self, text):#Don't use this
        output_str = ""
        strs = ""
        strslist = list(text)

        for i in strslist:
            strs += chr((ord(i) - 12))

        strslists = list(strs)
        
        for output in strslists:
            output_str += output
        

        return output_str[::-1]

