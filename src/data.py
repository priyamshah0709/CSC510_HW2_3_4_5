from tokenize import String


class data:
    def __init__(self, src):
        self.cols = None #summaries of data
        self.rows = {} #kept data
        if type(src == String):
            pass


someStringCHANGE = ""

# Call `fun` on each row. Row cells are divided in `the.seperator`.
def csv(fname, fun):
    sep = "([^" + someStringCHANGE + "]+)"
    try:
        f = open(fname, 'r')
    except:
        import os
        f = open(str(os.path.dirname(__file__)) + "/../data/" +str(fname))
    
    
    text = f.read()
    print((text))


csv("auto93.csv", None)



# -- Call `fun` on each row. Row cells are divided in `the.seperator`.
# function csv(fname,fun,      sep,src,s,t)
#   sep = "([^" .. the.seperator .. "]+)"
#   src = io.input(fname)
#   while true do
#     s = io.read()
#     if not s then return io.close(src) else 
#       t={}
#       for s1 in s:gmatch(sep) do t[1+#t] = coerce(s1) end
#       fun(t) end end end