import fileinput
from optparse import OptionParser

fields = []
values = {}



def usage():
    print <<<EOT
	topify - take any input stream and turn it into a top-like display.

	Usage: topify [format] 
EOT




def main():
    parser = OptionParser(usage="usage: %prog [format] filename \n" + \
			  "- take any input stream and turn it into a (io)top-like display",
                          version="%prog 1.0")
    parser.add_option("-f", "--format",
                      action="store",
                      dest="input_format",
                      default='line',
		      choices=['line','json']
                      help="Specify the basic format of the input (line, json)")
    parser.add_option("-d", "--descriptor",
                      action="store", # optional because action defaults to "store"
                      dest="descriptor",
                      default="",
                      help="Compound descriptor of the field/line formats",)
    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("wrong number of arguments")

    print options
    print args

    for line in fileinput.input():
	
        pass

if __name__ == "__main__":
	main()
