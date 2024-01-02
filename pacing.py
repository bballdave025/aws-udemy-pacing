#!/usr/bin/env python3
#
##############################################################################
# @file pacing.py
# @since 2023-07-12
# @author David BLACK  gh: @bballdave025
#
#######################################################################

import string # is it needed for "<str>".{split(), replace()} ?
import sys

print("Starting")

do_debug_process = True
only_check_first_lines = False
n_lines_to_check = 3
do_skip_0th_entry = True

if do_debug_process:
  print()
  print("We're debugging the process, y'all.")
  print()
##endof:  if do_debug_process

title = "Pacing for ZtoM Google TF Appendixes"
n_title_lines = 6

delim_char = ','

#in_csv_fname = "in_pacing_aws_cp.csv"
#in_csv_fname = "in_pacing_aws_mls.csv"
#in_csv_fname = "in_pacing_ztm_ggl_tf_usableVer_0-07.csv"
in_csv_fname = "in_pacing_jose_tf_therest_usableVer_0.01.csv"

#out_csv_fname = "out_pacing_aws_cp.csv"
#out_csv_fname = "out_pacing_aws_mls.csv"
#out_csv_fname = "out_pacing_ztm_ggl_tf_usableVer_0-07.csv"
out_csv_fname = "out_pacing_jose_tf_therest_usableVer_0.01.csv"

count_nums = 15 # zero-indexed
curr_column = 0

with open(in_csv_fname, 'r', encoding='utf-8') as ifh:
  with open(out_csv_fname, 'w+', encoding='utf-8') as ofh:
    
    ##  Make space at the beginning of the csv (which will become
    ##+ an Excel spreadsheet) for a nice title
    
    big_title_str = (count_nums - 1) * ( title + ',' )
    big_title_str = big_title_str + title + '\n'
    
    if do_debug_process:
      print()
      print(f"big_title_str:\n{big_title_str}")
      print()
    ##endof:  if do_debug_process

    for idx in range(n_title_lines):
      ofh.write(big_title_str)
    ##endof:  for idx in range(n_title_lines)
    
    is_first_line = True
    this_line_number = 0

    ## Process the input file
    for line in ifh:
      if do_debug_process:
        print()
        print("----------------------------------")
        print()
      ##endof:  if do_debug_process

      if is_first_line:
        if do_debug_process:
          print()
          print("Inside the first-line code.")
          print()
        ##endof:  if do_debug_process

        # We don't need the column names
        is_first_line = False
        continue
        
      ##endof:  if is_first_line

      lesson_info_str = line.rstrip()
      lesson_info_list = lesson_info_str.split(',')
      
      if do_debug_process:
        print()
        print(f"lesson_info_str: '{lesson_info_str}'")
        print("lesson_info_list:")
        print(str(lesson_info_list))
      ##endof:  if do_debug_process
      
      this_lesson_number_pre = str(lesson_info_list[0])
      this_lesson_number = this_lesson_number_pre
      if int(this_lesson_number_pre) < 10:
        this_lesson_number = "00" + this_lesson_number_pre
      ##endof:  if int(this_lesson_number) < 10
      if ( int(this_lesson_number_pre) > 9 and 
             int(this_lesson_number_pre) < 100 ):
        this_lesson_number = "0"  + this_lesson_number_pre
      ##endof:  if <num_-gt_9_and_-lt_100>
      this_type_letter       = str(lesson_info_list[1])
      this_section_number    = str(lesson_info_list[2])
      this_subsec_number     = str(lesson_info_list[3])
      this_has_follow_str    = str(lesson_info_list[4])
      this_has_follow_str = this_has_follow_str.lower()
      extra_cell_goes_after = 'Unknown'
      if this_has_follow_str == 'true':
        extra_cell_goes_after = True
      elif this_has_follow_str == 'false':
        extra_cell_goes_after = False
      else:
        print("Detected neither 'True' nor 'False' for this_has_follow_str.",
              file=sys.stderr)
        print("Using the boolean, False.", file=sys.stderr)
        extra_cell_goes_after = False
      ##endof:  if/else if/else <this_has_follow_str>
      this_after_parts       = str(lesson_info_list[5])
      this_after_parts_list = []
      if this_after_parts == 'None' or this_after_parts == '':
        this_after_parts = None
      ##endof:  if this_after_parts == 'None' or this_after_parts = ''
      else:
        this_after_parts_list = this_after_parts.split(';')
      ##endof:  if/else this_after_parts == 'None' or this_after_parts = ''
      
      if do_debug_process:
        print()
        print(f"this_lesson_number:    {this_lesson_number}")
        print(f"this_type_letter:      {this_type_letter}")
        print(f"this_section_number:   {this_section_number}")
        print(f"this_subsec_number:    {this_subsec_number}")
        print(f"extra_cell_goes_after: {extra_cell_goes_after}")
        if this_after_parts is not None:
          print(f"this_after_parts:     {this_after_parts}")
        else:
          print("this_after_parts is None")
        ##endof:  if/else this_after_parts is not None
        print(f"this_after_parts_list:\n{this_after_parts_list}")
        print()
      ##endof:  if do_debug_process
      
      is_skip_0th_time = ( (this_line_number == 0 and curr_column == 0 and do_skip_0th_entry) )
      
      if not is_skip_0th_time:
        ofh.write('"' + this_lesson_number + \
                  this_type_letter + '"' + delim_char)
        curr_column += 1
      ##endof:  if not is_skip_0th_time
      else:
        if do_debug_process:
          print()
          print("Skipping the cell for the zeroth entry.")
          print()
      ##endof:  if/else not is_skip_0th_time
      
      if curr_column > count_nums:
        ofh.write('\n')
        curr_column = 0
      ##endof:  if curr_column > count_nums

      EXIT_INCONSISTENT_BOOL_AND_LIST = 1
      
      we_have_list_but_boolean_is_false = \
        (len(this_after_parts_list) > 0) and (not extra_cell_goes_after)
      if we_have_list_but_boolean_is_false:
        print(  ("You have extra_cell_goes_after = False,\n"
                 "but you have list elements given.\n"
                 "Line number is: " + str(this_line_number) + ".\nExiting."
                ), file=sys.stderr
             )
        ifh.close()
        ofh.close()
        sys.exit(EXIT_INCONSISTENT_BOOL_AND_LIST)
      ##endof:  if we_have_list_but_boolean_is_false

      if extra_cell_goes_after:
        if len(this_after_parts_list) == 0:
          print(  ("You have extra_cell_goes_after = True,\n"
                   "but your list is empty.\n"
                   "Line number is: " + str(this_line_number) + ".\nExiting."
                  ), file=sys.stderr
               )
          ifh.close()
          ofh.close()
          sys.exit(EXIT_INCONSISTENT_BOOL_AND_LIST)
        ##endof:  if len(this_after_parts_list) == 0

        for cell_str in this_after_parts_list:
          ofh.write('"' + cell_str + '"' + delim_char)
          curr_column += 1
          if curr_column > count_nums:
            ofh.write('\n')
            curr_column = 0
          ##endof:  if curr_column > count_nums
        ##endof:  for cell_str in this_after_parts_list:

      ##endof:  if extra_cell_goes_after

      if do_debug_process and only_check_first_lines:
        if this_line_number > n_lines_to_check:
          ##  I don't know if my counting logic is right, but it should
          ##+ let me debug
          break
        ##endof:  if this_line_number > n_lines_to_check
      ##endof:  if do_debug_process

      this_line_number += 1

    ##endof:  for line in ifh
  ##endof:  with open ... ofh
##endof:  with open ... ifh

print()
print("Because of muSoft 'Unicode', you'll have to do a search and replace:")
print("Search: 'Â'; Replace: ''")
print("This is only in Excel, by the way.")
print()

##  Maybe fix it by searching for Unicode bytes for \section and replacing
##+ them with the muSoft bytes for \section
