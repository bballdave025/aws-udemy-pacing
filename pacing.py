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
only_check_first_lines = True
n_lines_to_check = 1

if do_debug_process:
  print()
  print("We're debugging the process, y'all.")
  print()
##endof:  if do_debug_process

title = "Pacing for AWS Cloud Practitioner"
n_title_lines = 6

in_csv_fname = "in_pacing_aws_cp.csv"

out_csv_fname = "out_pacing_aws_cp.csv"

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
    this_line_number=0

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
      
      this_lesson_number   = str(lesson_info_list[0])
      this_section_number  = str(lesson_info_list[1])
      this_subsec_number   = str(lesson_info_list[2])
      this_has_follow_str  = str(lesson_info_list[3])
      if this_has_follow_str == 'True':
        this_has_follow_bool = True
      elif this_has_follow_str == 'False':
        this_has_follow_bool = False
      else:
        print("Detected neither 'True' nor 'False' for this_has_follow_str.",
              file=sys.stderr)
        print("Using the boolean, False.", file=sys.stderr)
        this_has_follow_bool = False
      ##endof:  if/else if/else <this_has_follow_str>
      this_after_parts     = str(lesson_info_list[4])
      this_after_parts_list = []
      if this_after_parts == 'None' or this_after_parts == '':
        this_after_parts = None
      ##endof:  if this_after_parts == 'None' or this_after_parts = ''
      else:
        this_after_parts_list = this_after_parts.split(';')
      ##endof:  if/else this_after_parts == 'None' or this_after_parts = ''
      
      if do_debug_process:
        print()
        print(f"this_lesson_number:   {this_lesson_number}")
        print(f"this_section_number:  {this_section_number}")
        print(f"this_subsec_number:   {this_subsec_number}")
        print(f"this_has_follow_bool: {this_has_follow_bool}")
        if this_after_parts is not None:
          print(f"this_after_parts:     {this_after_parts}")
        else:
          print("this_after_parts is None")
        ##endof:  if/else this_after_parts is not None
        print(f"this_after_parts_list:\n{this_after_parts_list}")
        print()
      ##endof:  if do_debug_process

      if do_debug_process and only_check_first_lines:
        if this_line_number > n_lines_to_check:
          ##  I don't know if my logic is right, but it should
          ##+ let me debug
          break
        ##endof:  if this_line_number > n_lines_to_check
      ##endof:  if do_debug_process

      this_line_number += 1

    ##endof:  for line in ifh
  ##endof:  with open ... ofh
##endof:  with open ... ifh


