#!/usr/bin/python3
# -*- coding: utf-8 -*-

#    Template Translator v0.1
#    Traduit automatiquement certaines chaine de caractères des paquets

#    Publié par roptat <julien@lepiller.eu> le 8 août 2016
#    sous la licence gnu General Public License version 3 pubilée par la Free Software Foundation.
#    Visitez <http://www.gnu.org/licenses/> pour obtenir la licence.


import sys
import re
from templatetranslator import TemplateTranslator

files = sys.argv
files.pop(0)
lang = files.pop(0)

tt = TemplateTranslator(files)

# regexps
regexps = []

# no translation
tt.append(re.compile('(<\\?dbfo list-presentation="list"\\?> <\\?dbhtml list-presentation="table"\\?>)$'),
    {'fr': '#1',
     'pt_BR': '#1'})
# find an MD5 sum
tt.append(re.compile('([a-f0-9]{32})$'),
    {'fr': '#1',
     'pt_BR': '#1'})
# convert KB to Ko, MB to Mo and GB to Go, and keep SBU
tt.append(re.compile('([0-9\\.]+) ([KMG])B$'),
    {'fr': '#1&nbsp;#2o',
     'pt_BR': '#1 #2B'})
tt.append(re.compile('([0-9\\.]+) ([KMG])B \(with tests\)$'),
    {'fr': '#1&nbsp;#2o (avec les tests)',
     'pt_BR': '#1 #2B (com testes)'})
tt.append(re.compile('([0-9\\.]+) ([KMG])B \(additional ([0-9\\.]+) ([KMG])B for the tests\)$'),
    {'fr': '#1&nbsp;#2o (#3&nbsp;#4o supplémentaires pour les tests)',
     'pt_BR': '#1 #2B (#3 #4B adicionais para os testes)'})
tt.append(re.compile('([0-9\\.]+) ([KMG])B \(add ([0-9\\.]+) ([KMG])B for tests\)$'),
    {'fr': '#1&nbsp;#2o (plus #3&nbsp;#4o pour les tests)',
     'pt_BR': '#1 #2B (adicionar #3 #4B para os testes)'})
tt.append(re.compile('([0-9\\.]+) SBU$'),
    {'fr': '#1&nbsp;SBU',
     'pt_BR': '#1 UPC'})
tt.append(re.compile('([0-9\\.]+) SBU \(with tests\)$'),
    {'fr': '#1&nbsp;SBU (avec les tests)',
     'pt_BR': '#1 UPC (com testes)'})
tt.append(re.compile('([0-9\\.]+) SBU \(using parallelism=([0-9]+)\)$'),
    {'fr': '#1&nbsp;SBU (avec parallélisme = #2)',
     'pt_BR': '#1 UPC (usando paralelismo = #2)'})
tt.append(re.compile('([0-9\\.]+) SBU \(using parallelism=([0-9]+); with tests\)$'),
    {'fr': '#1&nbsp;SBU (avec parallélisme = #2&nbsp;; avec les tests)',
     'pt_BR': '#1 UPC (usando paralelismo = #2; com os testes)'})
tt.append(re.compile('([0-9\\.]+) SBU \(additional ([0-9\\.]+) SBU for the tests\)$'),
    {'fr': '#1&nbsp;SBU (#2&nbsp;SBU supplémentaires pour les tests)',
     'pt_BR': '#1 UPC (#2 UPC adicionais para os testes)'})
tt.append(re.compile('([0-9\\.]+) SBU \(add ([0-9\\.]+) SBU for tests\)$'),
    {'fr': '#1&nbsp;SBU (plus #2&nbsp;SBU pour les tests)',
     'pt_BR': '#1 UPC (adicionar #2 UPC para testes)'})
tt.append(re.compile('less than 0.1 SBU$'),
    {'fr': 'moins de 0,1&nbsp;SBU',
     'pt_BR': 'menos que 0,1 UPC'})
tt.append(re.compile('less than 0.1 SBU (with tests)'),
    {'fr': 'moins de 0,1&nbsp;SBU (avec les tests)',
     'pt_BR': 'menos que 0,1 UPC (com testes)'})
# termes à gauche des informations
tt.append(re.compile('Package Information$'),
    {'fr': 'Informations sur le paquet',
     'pt_BR': 'Informação do Pacote'})
tt.append(re.compile('Download \(HTTP\): (.*)$'),
    {'fr': 'Téléchargement (HTTP)&nbsp;: #1',
     'pt_BR': 'Transferência (HTTP): #1'})
tt.append(re.compile('Download \(FTP\): (.*)$'),
    {'fr': 'Téléchargement (FTP)&nbsp;: #1',
     'pt_BR': 'Transferência (FTP): #1'})
tt.append(re.compile('Download MD5 sum: (.*)$'),
    {'fr': 'Somme de contrôle MD5&nbsp;: #1',
     'pt_BR': 'Soma de verificação MD5 da transferência: #1'})
tt.append(re.compile('Download size: (.*)$'),
    {'fr': 'Taille du téléchargement&nbsp;: #1',
     'pt_BR': 'Tamanho da transferência: #1'})
tt.append(re.compile('Estimated disk space required: (.*)$'),
    {'fr': 'Estimation de l\'espace disque requis&nbsp;: #1',
     'pt_BR': 'Espaço em disco estimado exigido: #1'})
tt.append(re.compile('Estimated build time: (.*)$'),
    {'fr': 'Estimation du temps de construction&nbsp;: #1',
     'pt_BR': 'Tempo de construção estimado: #1'})
tt.append(re.compile('(http://[^ ]*)$'),
    {'fr': '#1',
     'pt_BR': '#1'})
tt.append(re.compile('(https://[^ ]*)$'),
    {'fr': '#1',
     'pt_BR': '#1'})
tt.append(re.compile('(ftp://[^ ]*)$'),
    {'fr': '#1',
     'pt_BR': '#1'})
# Dépendances
tt.append(re.compile('Optional Runtime Dependencies$'),
    {'fr': 'Dépendances à l\'exécution facultatives',
     'pt_BR': 'Dependências Opcionais em Tempo de Execução'})
tt.append(re.compile('(.*) Dependencies$'),
    {'fr': 'Dépendances de #1',
     'pt_BR': 'Dependências do #1'})
tt.append(re.compile('Required$'),
    {'fr': 'Requises',
     'pt_BR': 'Exigidas'})
tt.append(re.compile('Optional$'),
    {'fr': 'Facultatives',
     'pt_BR': 'Opcionais'})
tt.append(re.compile('Optional \(Required if building GNOME\)$'),
    {'fr': 'Facultatives (requises pour construire GNOME)',
     'pt_BR': 'Opcionais (Exigidas se construir GNOME)'})
tt.append(re.compile('Recommended$'),
    {'fr': 'Recommandées',
     'pt_BR': 'Recomendadas'})
tt.append(re.compile('Recommended \(Required if building GNOME\)$'),
    {'fr': 'Recommandées (requises pour construire GNOME)',
     'pt_BR': 'Recomendadas (Exigidas se construir GNOME)'})
tt.append(re.compile('Recommended \(required for the testsuite\)$'),
    {'fr': 'Recommandées (requises pour la suite de tests)',
     'pt_BR': 'Recomendadas (Exigidas para a suíte de testes)'})
tt.append(re.compile('User Notes: (.*)$'),
    {'fr': 'Notes utilisateur&nbsp;: #1',
     'pt_BR': 'Observações de Usuário(a): #1'})
# Titres
tt.append(re.compile('Installation of (.*)$'),
    {'fr': 'Installation de #1',
     'pt_BR': 'Instalação do #1'})
tt.append(re.compile('Command Explanations$'),
    {'fr': 'Explication des commandes',
     'pt_BR': 'Explicações do Comando'})
tt.append(re.compile('Config files$'),
    {'fr': 'Fichiers de configuration',
     'pt_BR': 'Arquivos de configuração'})
tt.append(re.compile('Config Files$'),
    {'fr': 'Fichiers de configuration',
     'pt_BR': 'Arquivos de Configuração'})
tt.append(re.compile('Config file$'),
    {'fr': 'Fichier de configuration',
     'pt_BR': 'Arquivo de configuração'})
tt.append(re.compile('Config File$'),
    {'fr': 'Fichier de configuration',
     'pt_BR': 'Arquivo de Configuração'})
tt.append(re.compile('Configuring ([^ ]+)$'),
    {'fr': 'Configuration de #1',
     'pt_BR': 'Configurando #1'})
tt.append(re.compile('Kernel Configuration$'),
    {'fr': 'Configuration du noyau',
     'pt_BR': 'Configuração do Núcleo'})
tt.append(re.compile('Enable the following options in the kernel configuration and recompile the kernel if necessary:$'),
    {'fr': 'Activez les options suivantes dans la configuration du noyau et recompilez le noyau si nécessaire&nbsp;:',
     'pt_BR': 'Habilite as seguintes opções na configuração do núcleo e recompile o núcleo, se necessário:'})
tt.append(re.compile('Boot Script$'),
    {'fr': 'Script de démarrage',
     'pt_BR': 'Script de Inicialização'})
tt.append(re.compile('Boot Scripts$'),
    {'fr': 'Scripts de démarrage',
     'pt_BR': 'Scripts de Inicialização'})
tt.append(re.compile('Systemd Unit'),
    {'fr': 'Unité systemd',
     'pt_BR': 'Unidade do systemd'})
tt.append(re.compile('Systemd Units'),
    {'fr': 'Unités systemd',
     'pt_BR': 'Unidades do systemd'})
tt.append(re.compile('<phrase revision="sysv">Boot Script</phrase> <phrase revision="systemd">Systemd Unit</phrase>$'),
    {'fr': '<phrase revision="sysv">Script de démarrage</phrase> <phrase revision="systemd">Unité Systemd</phrase>',
     'pt_BR': '<phrase revision="sysv">Script de Inicialização</phrase> <phrase revision="systemd">Unidade do systemd</phrase>'})
tt.append(re.compile('Configuration Information$'),
    {'fr': 'Informations sur la configuration',
     'pt_BR': 'Informação de Configuração'})
tt.append(re.compile('Contents$'),
    {'fr': 'Contenu',
     'pt_BR': 'Conteúdo'})
tt.append(re.compile('Installed Program$'),
    {'fr': 'Programme installé',
     'pt_BR': 'Aplicativo Instalado'})
tt.append(re.compile('Installed Programs$'),
    {'fr': 'Programmes installés',
     'pt_BR': 'Aplicativos Instalados'})
tt.append(re.compile('Installed Library$'),
    {'fr': 'Bibliothèque installée',
     'pt_BR': 'Biblioteca Instalada'})
tt.append(re.compile('Installed Libraries$'),
    {'fr': 'Bibliothèques installées',
     'pt_BR': 'Bibliotecas Instaladas'})
tt.append(re.compile('Installed Directory$'),
    {'fr': 'Répertoire installé',
     'pt_BR': 'Diretório Instalado'})
tt.append(re.compile('Installed Directories$'),
    {'fr': 'Répertoires installés',
     'pt_BR': 'Diretórios Instalados'})
tt.append(re.compile('Short Descriptions$'),
    {'fr': 'Descriptions courtes',
     'pt_BR': 'Descrições Curtas'})
# phrases récurrentes
tt.append(re.compile('Install ([^ ]*) by running the following commands:$'),
    {'fr': 'Installez #1 en exécutant les commandes suivantes&nbsp;:',
     'pt_BR': 'Instale #1 executando os seguintes comandos:'})
tt.append(re.compile('(<userinput.*>.*</userinput>)$', re.MULTILINE|re.DOTALL),
    {'fr': '#1',
     'pt_BR': '#1'})
tt.append(re.compile('(<literal>.*</literal>)$', re.MULTILINE|re.DOTALL),
    {'fr': '#1',
     'pt_BR': '#1'})
tt.append(re.compile('(<computeroutput>.*</computeroutput>)$', re.MULTILINE|re.DOTALL),
    {'fr': '#1',
     'pt_BR': '#1'})
tt.append(re.compile('Now, as the (.*) user:$'),
    {'fr': 'Maintenant, en tant qu\'utilisateur #1&nbsp;:',
     'pt_BR': 'Agora, como o(a) usuário(a) #1:'})
tt.append(re.compile('To test the results, issue:? (<command>.*</command>).$'),
    {'fr': 'Pour tester les résultats lancez&nbsp;: #1.',
     'pt_BR': 'Para testar os resultados, emita: #1.'})
tt.append(re.compile('To run the test suite, issue:? (<command>.*</command>).$'),
    {'fr': 'Pour lancer la suite de tests, tapez&nbsp;: #1.',
     'pt_BR': 'Para executar a suíte de teste, emita: #1.'})
tt.append(re.compile('This package does not come with a test suite.$'),
    {'fr': 'Ce paquet n\'a pas de suite de tests.',
     'pt_BR': 'Esse pacote não vem com uma suíte de teste.'})
tt.append(re.compile('Additional Downloads$'),
    {'fr': 'Téléchargements supplémentaires',
     'pt_BR': 'Transferências Adicionais'})
tt.append(re.compile('Required [pP]atch: (.*)$'),
    {'fr': 'Correctif requis&nbsp;: #1',
     'pt_BR': 'Remendo exigido: #1'})
tt.append(re.compile('(<othername>.*)$'),
    {'fr': '#1',
     'pt_BR': '#1'})
tt.append(re.compile('Introduction to (.*)$'),
    {'fr': 'Introduction à #1',
     'pt_BR': 'Introdução ao #1'})
tt.append(re.compile('(<xref [^>]*>)$'),
    {'fr': '#1',
     'pt_BR': '#1'})
tt.append(re.compile('To start the (<command>.*</command>) daemon at boot, enable the previously installed systemd unit by running the following command as the (<systemitem class="username">root</systemitem>) user:$'),
    {'fr': 'Pour démarrer le démon #1 au démarrage, activez l\'unité systemd précédemment installée en exécutant la commande suivante en tant qu\'utilisateur #2&nbsp;:',
     'pt_BR': 'Para iniciar o processo de segundo plano #1 na inicialização, habilite a unidade do systemd instalada anteriormente executando o seguinte comando como o(a) usuário(a) #2:'})
tt.append(re.compile('(<command>[^ <]*</command>)$'),
    {'fr': '#1',
     'pt_BR': '#1'})
tt.append(re.compile('(<filename[^>]*>[^ <]*</filename>)$'),
    {'fr': '#1',
     'pt_BR': '#1'})
tt.append(re.compile('(<command>.*</command>): This sed silences several useless and annoying warnings (generated )?(from|by) libtool.$'),
    {'fr': '#1&nbsp;: Ce sed rend muets de nombreux avertissements inutiles et ennuyeux de libtool.',
     'pt_BR': '#1: Este sed silencia muitos avisos da libtool desnecessários e irritantes.'})
tt.append(re.compile('(<command>.*</command>): This sed silences several useless and obsolete warnings (generated )?(from|by) libtool.$'),
    {'fr': '#1&nbsp;: Ce sed rend muets de nombreux avertissements inutiles et obsolètes de libtool.',
     'pt_BR': '#1:Este sed silencia muitos avisos da libtool desnecessários e obsoletos.'})
tt.append(re.compile('([^ <]*)$'),
    {'fr': '#1',
     'pt_BR': '#1'})
tt.append(re.compile('You can start (<application>.*</application>) from a TTY using (<xref linkend="xinit"/>).$'),
    {'fr': 'Vous pouvez démarrer #1 depuis un TTY avec #2.',
     'pt_BR': 'Você pode iniciar #1 a partir de um TTY usando #2.'})
tt.append(re.compile('(<.*>): Use this to disable (.*) support.?$'),
    {'fr': '#1&nbsp;: Utilisez ce paramètre pour désactiver le support de #2',
     'pt_BR': '#1:Use isso para desabilitar o suporte #2'})
tt.append(re.compile('(<.*>): Use this switch if you don\'t have (<application>.*</application>) installed.?$'),
    {'fr': '#1&nbsp;: Utilisez ce paramètre si vous n\'avez pas installé #2',
     'pt_BR': '#1: Use essa chave se você não tiver #2 instalado'})
tt.append(re.compile('(<.*>): Use these switches if you don\'t have (<application>.*</application>) installed.?$'),
    {'fr': '#1&nbsp;: Utilisez ces paramètres si vous n\'avez pas installé #2',
     'pt_BR': '#1: Use essas chaves se você não tiver #2 instalado'})
tt.append(re.compile('(<.*>): Use this switch if you did( no)?(n\')?t install (<application>.*</application>).?$'),
    {'fr': '#1&nbsp;: Utilisez ce paramètre si vous n\'avez pas installé #3',
     'pt_BR': '#1: Use essa chave se você não instalou #3'})
tt.append(re.compile('(<.*>): Use these switches if you did not install (<application>.*</application>).?$'),
    {'fr': '#1&nbsp;: Utilisez ces paramètres si vous n\'avez pas installé #2',
     'pt_BR': '#1: Use essas chaves se você não instalou #2'})
tt.append(re.compile('several in (&kde-dir;/[^ ]*)$'),
    {'fr': 'plusieurs dans #1',
     'pt_BR': 'vários em #1'})
tt.append(re.compile('This package does not come with a working test suite.?$'),
    {'fr': 'Ce paquet ne contient pas de suite de tests utilisable.',
     'pt_BR': 'Esse pacote não vem com uma suíte de teste funcional.'})
tt.append(re.compile('contains the (<application>.*</application>) API functions.$'),
    {'fr': 'Contient les fonctions de l\'API de #1',
     'pt_BR': 'contém as funções da l\'API de #1'})
tt.append(re.compile('Now as the <systemitem class="username">root</systemitem> user:'),
    {'fr': 'Maintenant en tant qu\'utilisateur <systemitem class="username">root</systemitem>&nbsp;:',
     'pt_BR': 'Agora como o(a) usuário(a) <systemitem class="username">root</systemitem>:'})
tt.append(re.compile('Project Home Page: (<ulink .*/>)$', re.MULTILINE|re.DOTALL),
    {'fr': 'Page d\'accueil du projet&nbsp;: #1',
     'pt_BR': 'Página Inicial do Projeto: #1'})
tt.append(re.compile('Download Location: (<ulink .*/>)$', re.MULTILINE|re.DOTALL),
    {'fr': 'Emplacement du téléchargement&nbsp;: #1',
     'pt_BR': 'Local da Transferência: #1'})
tt.append(re.compile('(<.*>): This switch is used to apply( a)? higher level of( the)? compiler( the)? optimizations?.?$', re.MULTILINE|re.DOTALL),
    {'fr': '#1&nbsp;: Ce paramètre est utilisé pour appliquer un plus haut niveau d\'optimisation à la compilation.',
     'pt_BR': '#1: Essa chave é usada para aplicar um nível mais alto de otimização à compilação.'})
tt.append(re.compile('(<ulink [^>]*/>)$', re.MULTILINE|re.DOTALL),
    {'fr': '#1',
     'pt_BR': '#1'})
tt.append(re.compile('(<ulink [^>]*/>, )+, and (<ulink [^>]*/>)$', re.MULTILINE|re.DOTALL),
    {'fr': '#1 et #2',
     'pt_BR': '#1 e #2'})
tt.append(re.compile('Fix a build issue with ([^ ]+)$', re.MULTILINE|re.DOTALL),
    {'fr': 'Corrigez un problème de construction avec #1.',
     'pt_BR': 'Corrija um problema de construção com #1.'})
tt.append(re.compile('(<othername>.*</othername> <date>.*</date>)', re.MULTILINE|re.DOTALL),
    {'fr': '#1',
     'pt_BR': '#1'})
tt.append(re.compile('(<date>.*</date>)', re.MULTILINE|re.DOTALL),
    {'fr': '#1',
     'pt_BR': '#1'})

tt.translate([lang])
