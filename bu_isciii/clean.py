#!/usr/bin/env python
'''
=============================================================
HEADER
=============================================================
INSTITUTION: BU-ISCIII
AUTHOR: Guillermo J. Gorines Cordero
MAIL: guillermo.gorines@urjc.es
VERSION: 1.0
CREATED: 21-2-2022
REVISED: 21-2-2022
REVISED BY:
DESCRIPTION: 
OPTIONS:

USAGE:

REQUIREMENTS:

TO DO: 
================================================================
END_OF_HEADER
================================================================
'''
# Generic imports
import sys
import os

# Local imports

class CleanUp(self):
    def __init__(self,):
        # access the api with the service name to obtain
        self.removes = 
        self.renames = 


    def show_removable_dirs(self, to_stdout = True):
        """
        Print or return the list of objects that must be deleted in this service
        
        Usage: 
            object.show_removable_dirs(to_stdout = [BOOL])

        Params:
            to_stdout [BOOL]: if True, print the list. If False, return the list.
        """
        if to_stdout:
            print(self.removes)
            return
        
        else:
            return self.removes
        
    def show_renameable_dirs(self, to_stdout = True):
        """
        Print or return the list of objects that must be renamed in this service
        
        Usage: 
            object.show_renameables_dirs(to_stdout = [BOOL])

        Params:
            to_stdout [BOOL]: if True, print the list. If False, return the list.
        """

        if to_stdout:
            print(self.renames)
            return
        else:
            return self.renames

    def delete_removes(self):
        """
        Remove the files that must be deleted for the delivery of the service
        
        Usage:
            object.delete_removes()
        
        Params:


        """

        for item_to_remove in self.removes:

            os.remove()


    def rename_renamables(self):
        
        
        os.rename()


    def full_clean_job(self):

