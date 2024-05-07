#sample input is a = sdfghjkjhgfdfghjkjhgfddfgh
#sample input is b = int(4)

# sample output

# sd
# fg
# hj
# kj
# hg
# fd
# fg
# hj
# kj
# hg
# fd
# df
# gh





#method 1
import textwrap

def wrap(string,max_width):
    OUT =  textwrap.wrap(string,max_width,break_long_words=True)
    return "\n".join(OUT)
  


if __name__ == "__main__":
    string,max_width = input(), int(input())
    result = wrap(string,max_width)
    print(result)



