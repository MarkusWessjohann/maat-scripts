import re

######################################################################
## Complexity calcualations
######################################################################

leading_tabs_expr = re.compile(r'^(\t+)')
leading_spaces_expr = re.compile(r'^( +)')
empty_line_expr = re.compile(r'^\s*$|^\s*\\\*\s*|^\*\s*$')
empty_lines = 0

def n_log_tabs(line):
    pattern = re.compile(r' +')
    wo_spaces = re.sub(pattern, '', line)
    m = leading_tabs_expr.search(wo_spaces)
    if m:
        tabs = m.group()
        return len(tabs)
    return 0

def n_log_spaces(line):
    pattern = re.compile(r'\t+')
    wo_tabs = re.sub(pattern, '', line)
    m = leading_spaces_expr.search(wo_tabs)
    if m:
        spaces = m.group()
        return len(spaces)
    return 0

def contains_code(line):
    if  empty_line_expr.match(line):
        empty_lines=empty_lines + 1
        return false
    return true


def complexity_of(line):
    return n_log_tabs(line) + (n_log_spaces(line) / 2) # hardcoded indentation

######################################################################
## Statistics from complexity
######################################################################
def empty_lines():		
    return empty_lines

def calculate_complexity_in(source):
    empty_lines = 0
    return [complexity_of(line) for line in source.split("\n") if contains_code(line)]
