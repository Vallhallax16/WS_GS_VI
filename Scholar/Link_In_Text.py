class Link_In_Text:

    @staticmethod
    def Extract_Text(a):
        text = ""
        start_copy = False

        for char in a:
        #
            if(char == ">"):
            #
                start_copy = True
            #

            if(char == "<" and start_copy == True):
            #
                return text
            #

            if(start_copy == True and char != ">"):
                text.__add__(char)
        #