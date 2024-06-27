#!/usr/bin/python3
# -*- coding: utf-8 -*-

#    Template Translator v0.2
#    Regex-based automatic translator for common strings in gettext files.
#
#    Copyright 2016-2017 roptat <julien@lepiller.eu>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

import sys
import re
import polib
import os.path

class TemplateTranslator:
    def __init__(self, files):
        self.regexps = []
        self.numberregexp = re.compile('^([0-9]+)\\.([0-9]+)$')
        self.files = files
    
    def append(self, regexp, translation):
        self.regexps.append([regexp, translation])

    def translate_group(self, g):
        m = self.numberregexp.match(g)
        # This converts things like 2.1 to 2,1.
        # Good enough, this is also how it should be done in fr and pt.
        if m:
            return m.group(1) + ',' + m.group(2)
        return g

    def convert(self, entry, regexp, template):
        m = regexp.match(entry.msgid)
        #if m:
        # do not modify anything if the translation is already correct
        if m and ("fuzzy" in entry.flags or not entry.msgstr):
            msgstr = template
            try:
                m1 = self.translate_group(m.group(1))
                msgstr = msgstr.replace("#1", m1)
                m2 = self.translate_group(m.group(2))
                msgstr = msgstr.replace('#2', m2)
                m3 = self.translate_group(m.group(3))
                msgstr = msgstr.replace('#3', m3)
                m4 = self.translate_group(m.group(4))
                msgstr = msgstr.replace('#4', m4)
                m5 = self.translate_group(m.group(5))
                msgstr = msgstr.replace('#5', m5)
            except:
                x=1
            entry.msgstr = msgstr
            if "fuzzy" in entry.flags:
                entry.flags.remove("fuzzy")

    def translate_one(self, filename, language):
        realname = language + '/' + filename
        if not os.path.exists(realname):
            print(realname, 'does not exist.')
            return
        po = polib.pofile(realname)
        for entry in po:
            for reg in self.regexps:
                if language in reg[1]:
                    self.convert(entry, reg[0], reg[1][language])
        po.save()
    
    def translate(self, languages):
        number = len(self.files)
        current = 1
        
        for filename in self.files:
            print('Traitement du fichier ', current, '/', number, '     \r',
                    end="", flush=True),
            current = current + 1
            for language in languages:
                self.translate_one(filename, language)
        print('')
