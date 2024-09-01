#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import re
import polib
from templatetranslator import TemplateTranslator

languages = sys.argv
languages.pop(0)
files=['introduction/welcome/changelog.po']

tt = TemplateTranslator(files)

tt.append(re.compile('\[([^\]]+)\] - Up[dg]r?a[td]ed? to ([^ ]+).?$', re.MULTILINE|re.DOTALL),
    {'fr': '[#1] — Mise à jour vers #2.',
     'pt_BR': '[#1] - Atualização para #2.'})
tt.append(re.compile('\[([^\]]+)\] - Up[dg]r?a[td]ed? to ([^ ]+). +Fixes (<ulink [^>]+> *#[0-9]+ *</ulink>.?)$', re.MULTILINE|re.DOTALL),
    {'fr': '[#1] — Mise à jour vers #2. Corrige #3',
     'pt_BR': '[#1] - Atualização para #2. Corrige #3'})
tt.append(re.compile('\[([^\]]+)\] - Up[dg]r?a[td]ed? to ([^ ]+). +Finishes (<ulink [^>]+> *#[0-9]+ *</ulink>.?)$', re.MULTILINE|re.DOTALL),
    {'fr': '[#1] — Mise à jour vers #2. Termine #3',
     'pt_BR': '[#1] - Atualização para #2. Finaliza #3'})
tt.append(re.compile('\[([^\]]+)\] - Up[dg]r?a[td]ed? ([^ ]+). +Fixes (<ulink [^>]+> *#[0-9]+ *</ulink>.?)$', re.MULTILINE|re.DOTALL),
    {'fr': '[#1] — Mise à jour vers #2. Corrige #3',
     'pt_BR': '[#1] - Atualização para #2. Corrige #3'})
tt.append(re.compile('\[([^\]]+)\] - Up[dg]r?a[td]ed? to ([^ ]+). +Part of (<ulink [^>]+> *#[0-9]+ *</ulink>.?)$', re.MULTILINE|re.DOTALL),
    {'fr': '[#1] – Mise à jour vers #2. Corrige partiellement #3',
     'pt_BR': '[#1] - Atualização para #2. Corrige parcialmente #3'})
tt.append(re.compile('\[([^\]]+)\] - Up[dg]r?a[td]ed? to ([^ ]+) and ([^ ]+). +Fixes (<ulink [^>]+> *#[0-9]+ *</ulink>.?)$', re.MULTILINE|re.DOTALL),
    {'fr': '[#1] — Mise à jour vers #2 et #3. Corrige #4',
     'pt_BR': '[#1] - Atualização para #2 e #3. Corrige #4'})
tt.append(re.compile('\[([^\]]+)\] - Up[dg]r?a[td]ed? to ([^ ]+) ([0-9\.]+). +Fixes (<ulink [^>]+> *#[0-9]+ *</ulink>.?)$', re.MULTILINE|re.DOTALL),
    {'fr': '[#1] — Mise à jour vers #2 #3. Corrige #4',
     'pt_BR': '[#1] - Atualização para #2 #3. Corrige #4'})
tt.append(re.compile('\[([^\]]+)\] - Up[dg]r?a[td]ed? to ([^ ]+). +Partially fixes (<ulink [^>]+> *#[0-9]+ *</ulink>.?)$', re.MULTILINE|re.DOTALL),
    {'fr': '[#1] — Mise à jour vers #2. Corrige partiellement #3',
     'pt_BR': '[#1] - Atualização para #2. Corrige parcialmente #3'})
tt.append(re.compile('\[([^\]]+)\] - Up[dg]r?a[td]ed? to ([^ ]+) (\([^ ]+\)). +Fixes (<ulink [^>]+> *#[0-9]+ *</ulink>.?)$', re.MULTILINE|re.DOTALL),
    {'fr': '[#1] — Mise à jour vers #2 #3. Corrige #4',
     'pt_BR': '[#1] - Atualização para #2 #3. Corrige #4'})
tt.append(re.compile('\[([^\]]+)\] - Up[dg]r?a[td]ed? to ([^ ]+) \(([^ ]+) [mM]odule\). +Fixes (<ulink [^>]+> *#[0-9]+ *</ulink>.?)$', re.MULTILINE|re.DOTALL),
    {'fr': '[#1] — Mise à jour vers #2 (module #3). Corrige #4',
     'pt_BR': '[#1] - Atualização para #2 (módulo #3). Corrige #4'})
tt.append(re.compile('\[([^\]]+)\] - Up[dg]r?a[td]ed? to ([^ ]+) \([sS]ecurity [fF]ixe?s?\). +Fixes (<ulink [^>]+> *#[0-9]+ *</ulink>.?)$', re.MULTILINE|re.DOTALL),
    {'fr': '[#1] — Mise à jour vers #2 (correctif de sécurité). Corrige #3',
     'pt_BR': '[#1] - Atualização para #2 (Correções de Segurança). Corrige #3'})
tt.append(re.compile('\[([^\]]+)\] - Up[dg]r?a[td]ed? to ([^ ]+) \([sS]ecurity [uU]pdate?s?\). +Fixes (<ulink [^>]+> *#[0-9]+ *</ulink>.?)$', re.MULTILINE|re.DOTALL),
    {'fr': '[#1] — Mise à jour vers #2 (correctif de sécurité). Corrige #3',
     'pt_BR': '[#1] - Atualização para #2 (Atualização de Segurança). Corrige #3'})
tt.append(re.compile('\[([^\]]+)\] - Up[dg]r?a[td]ed? to ([^ ]+) \(Xorg Library\). +Fixes (<ulink [^>]+> *#[0-9]+ *</ulink>.?)$', re.MULTILINE|re.DOTALL),
    {'fr': '[#1] — Mise à jour vers #2 (bibliothèque Xorg). Corrige #3',
     'pt_BR': '[#1] - Atualização para #2 (Biblioteca Xorg). Corrige #3'})
tt.append(re.compile('\[([^\]]+)\] - Up[dg]r?a[td]ed? to ([^ ]+) \(Xorg Application\). +Fixes (<ulink [^>]+> *#[0-9]+ *</ulink>.?)$', re.MULTILINE|re.DOTALL),
    {'fr': '[#1] — Mise à jour vers #2 (application Xorg). Corrige #3',
     'pt_BR': '[#1] - Atualização para #2 (Aplicativo Xorg). Corrige #3'})
tt.append(re.compile('\[([^\]]+)\] - Up[dg]r?a[td]ed? to ([^ ]+). Addresses (<ulink [^>]+> *#[0-9]+ *</ulink>.?)$', re.MULTILINE|re.DOTALL),
    {'fr': '[#1] — Mise à jour vers #2. Corrige #3',
     'pt_BR': '[#1] - Atualização para #2. Corrige #3'})
tt.append(re.compile('\[([^\]]+)\] - Reintroduce ([^ ]+).?$', re.MULTILINE|re.DOTALL),
    {'fr': '[#1] — Réintroduction de #2.',
     'pt_BR': '[#1] - Reintrodução de #2.'})
tt.append(re.compile('\[([^\]]+)\] - Reinstate ([^ ]+).?$', re.MULTILINE|re.DOTALL),
    {'fr': '[#1] — Réintroduction de #2.',
     'pt_BR': '[#1] - Restabelecimento de #2.'})
tt.append(re.compile('\[([^\]]+)\] - Add? ([^ ]+).?$', re.MULTILINE|re.DOTALL),
    {'fr': '[#1] — Ajout de #2.',
     'pt_BR': '[#1] - Adicionar #2.'})

tt.translate(languages)



portugueseMonth = {
    'January': 'janeiro',
    'February': 'fevereiro',
    'March': 'março',
    'April': 'abril',
    'May': 'maio',
    'June': 'junho',
    'July': 'julho',
    'August': 'agosto',
    'September': 'setembro',
    'October': 'outubro',
    'November': 'novembro',
    'December': 'dezembro'
}

frenchMonth = {
    'January': 'janvier',
    'February': 'février',
    'March': 'mars',
    'April': 'avril',
    'May': 'mai',
    'June': 'juin',
    'July': 'juillet',
    'August': 'août',
    'September': 'septembre',
    'October': 'octobre',
    'November': 'novembre',
    'December': 'décembre'
}

datereg = re.compile('([^ ]+) ([0-9]{1,2})(th|nd|st|rd|),? (20[0-9]{2})')

for lang in languages:
    po = polib.pofile(lang + '/introduction/welcome/changelog.po')
    for entry in po:
        m = datereg.match(entry.msgid)
        if m and ("fuzzy" in entry.flags or not entry.msgstr):
            day = m.group(2)
            if int(day) == 1 and lang == 'fr':
                day = '1er'
            try:
                if lang == 'fr':
                    month = frenchMonth[m.group(1)]
                elif lang == 'pt_BR':
                    month = portugueseMonth[m.group(1)]
                year = m.group(4)
                entry.msgstr = day + " " + month + " " + year
                if "fuzzy" in entry.flags:
                    entry.flags.remove("fuzzy")
            except:
                pass
    po.save()
print('')

