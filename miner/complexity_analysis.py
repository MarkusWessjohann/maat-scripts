######################################################################
## This program calulcates the whitespace complexity of a file.
######################################################################

#!/bin/env python
import argparse
import desc_stats
import complexity_calculations
 
######################################################################
## Statistics from complexity
######################################################################

def as_stats(revision, complexity_by_line):
 return desc_stats.DescriptiveStats(revision, complexity_by_line)
    
######################################################################
## Output
######################################################################

def as_csv(stats):
# print('n,total,mean,sd,max,lineIndentComplex')
 fields_of_interest = [args.file, stats.n_revs, stats.total, round(stats.mean(),2), round(stats.sd(),2), stats.max_value(), stats.lineIndentComplexity()]
 printable = [str(field) for field in fields_of_interest]
 print(';'.join(printable))

######################################################################
## Main
######################################################################

def run(args):
 with open (args.file, "r") as file_to_calc:
  complexity_by_line = complexity_calculations.calculate_complexity_in(file_to_calc.read())
  stats = desc_stats.DescriptiveStats(args.file, complexity_by_line)
  as_csv(stats)

if __name__ == "__main__":
 parser = argparse.ArgumentParser(description='Calculates whitespace complexity of the given file.')
 parser.add_argument('file', type=str, help='The file to calculate complexity on')
 args = parser.parse_args()
 run(args)
