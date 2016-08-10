#!/usr/bin/env python

import ptc

# Pokemon Trainer Club Account Creator
# By Gee19

acc_prefix = "pick_your_own"
password = "pick_your_own"
num_of_acc = 1
last_acc_suffix = 8

if __name__ == '__main__':
    for x in xrange(num_of_acc):
        curr_acc_suffix = x + last_acc_suffix
        curr_acc_name = acc_prefix + str(curr_acc_suffix)

        print "Current user: " + curr_acc_name

        ptc.init()

        #step 1 ------------------
        try:
            ptc.wait_for_verify_age()
            ptc.click_dob()
            try:
                ptc.wait_for_date_picker()
                ptc.set_month()
                ptc.set_day()   
            except TimeoutException:
                print "Verify Age: Timed out waiting for datepicker to load"
        except TimeoutException:
            print "Verify Age: Timed out waiting for page to load"
        finally:
            ptc.confirm_dob()
            ptc.wait_for_verify_age()
            ptc.set_country()
            ptc.continue_to_create()
            print "done step 1"

        #step 2 -----------------
        try:
            ptc.wait_for_create_acc()
            ptc.set_username(curr_acc_name)
            ptc.set_passwords(password)
            #gm.gen_temp_email()
            #ptc.set_emails(temp_email)
            ptc.opt_out()
            ptc.accept_terms()

        except TimeoutException:
            print "Create Account: Timed out waiting for page to load"
        finally:
            #ptc.check_user_availability()
            #ptc.continue_to_verify_email()
            #gm.click_verify_link()
            print "done step 2"