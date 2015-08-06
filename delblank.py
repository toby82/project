__author__ = 'Administrator'
def delblank(infile,outfile):
    """
    :param infile: "
    :param outfile:
    :return:
    """
    infp = open(infile,'r')
    outfp = open(outfile,'w')
    lines = infp.readlines()
    for line in  lines:
        if line.split():
            outfp.writelines(line)
    infp.close()
    outfp.close()
"""
#µ÷ÓÃÊ¾Àý
if __name__ == "__main__":
    delblank("1.txt","2.txt")

"""