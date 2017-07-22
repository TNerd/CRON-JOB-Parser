#!/usr/bin/python
###############################################################################
import sys, re
###############################################################################
# error event
#
def error_instance(error, instruction, third):
    print ''
    print "Error:", error
    print third, instruction
    sys.exit(1)

###############################################################################
# exceptions / arg data validation
#
if __name__ == "__main__":
    try:
        current_time = sys.argv[1]
    except IndexError:
        error_instance("Missing Arguments", "./sunny 04:24 file", "Example:")

if ((re.compile("\d\d:\d\d")).search(current_time)) is None:
    error_instance("Incorrect time", "01:24, 23:59, 00:00", "Example:")
###############################################################################
# results
#
def result(when, hour, minute, path):
    m_fix = '{0:02d}'.format(int(minute))
    h_fix = '{0:02d}'.format(int(hour))
    print '{}:{} {} - {}'.format(h_fix, m_fix, when, path)
###############################################################################
# If this, if that... If I could sort it out better.
#
def if_this_if_that(content):
    s_l_c          = content.split() # config file data
    h_current_time = int(current_time[:2])
    m_current_time = int(current_time[-2:])
    o              = 00
    t              = 'Today'
    tt             = 'Tomorrow'

    # X hour, specific minute
    if re.match("\*", s_l_c[1]) and re.match("\d|\d\d", s_l_c[0]):
        if m_current_time <= int(s_l_c[0]):
            result(t,(h_current_time), (s_l_c[0]), s_l_c[2])
        else:
            if h_current_time == 23:
                result(tt,(o), (s_l_c[0]), s_l_c[2])
            else:
                result(t,(h_current_time+1), (s_l_c[0]), s_l_c[2])

    # every minute
    elif re.match("\*", s_l_c[1]) and re.match("\*", s_l_c[0]):
        result(t,(h_current_time), m_current_time, s_l_c[2])

    # specific hour, X minute
    elif re.match("\d|\d\d", s_l_c[1]) and re.match("\*", s_l_c[0]):
        if h_current_time <= int(s_l_c[1]):
            result(t,(s_l_c[1]), o, s_l_c[2])
        else:
            result(tt, (s_l_c[1]),o, s_l_c[2])

    # specific hour, specific minute
    else:
        if h_current_time <= int(s_l_c[1]) and m_current_time <= int(s_l_c[0]):
            result(t, (s_l_c[1]),(s_l_c[0]), s_l_c[2])
        else:
            result(tt, (s_l_c[1]),(s_l_c[0]), s_l_c[2])

###############################################################################
# load / pick regex match / pass to statements
#
for match_line in (sys.stdin.readlines()):
    if re.match("(\d\s|\d\d|\*)", match_line):
        if_this_if_that(match_line)
