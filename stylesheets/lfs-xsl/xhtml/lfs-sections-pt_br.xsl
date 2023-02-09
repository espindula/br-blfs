<?xml version='1.0' encoding='UTF-8'?>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns="http://www.w3.org/1999/xhtml"
                version="1.0">

<!--

Direitos autorais (Copyright) da versão modificada traduzida para a 
língua portuguesa escrita e falada no Brasil: (c) 2022, 2023 Jamenson 
Ferreira Espindula de Almeida Melo (<jafesp@gmail.com>).

  Este trabalho de tradução do livro "Beyond Linux From Scratch" é 
  classificado pela Free Software Foundation como sendo uma "versão 
  modificada" do mencionado livro.  Em assim sendo, na qualidade de 
  tradutor, produtor da "versão modificada" e titular dos direitos 
  autorais sobre a versão traduzida para a língua portuguesa do livro 
  "Beyond Linux From Scratch", concede-se a seguinte permissão:

  É concedida permissão para copiar, distribuir e (ou) modificar este 
  livro "Beyond Linux From Scratch", versão traduzida para a língua 
  portuguesa, sob os termos da Licença de Documentação Livre GNU, versão 
  1.3 ou qualquer versão posterior publicada pela Free Software 
  Foundation; sem Seções Invariantes, sem Textos de Capa Frontal e sem 
  Textos de Quarta Capa.  Uma cópia da licença está incluída na seção 
  intitulada "Licença de Documentação Livre GNU".
  
# Atenção: todos os documentos aqui publicados são distribuídos sem qualquer garantia, implícita e (ou) explícita.
  
  Permission is granted to copy, distribute and (or) modify this book 
  "Beyond Linux From Scratch", translated into Brazilian Portuguese, 
  under the terms of the GNU Free Documentation License, Version 1.3 or 
  any later version published by the Free Software Foundation; with no 
  Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.  A 
  copy of the license is included in the section entitled "GNU Free 
  Documentation License".

# Warning: all the files herein published are released with no warranty, implicit and (or) explicit.

-->

  <!-- This stylesheet controls how preface, chapter, and sections are handled -->

    <!-- Chunk the first top-level section? 1 = yes, 0 = no
         If preface and chapters TOC are generated, this must be 1. -->
  <xsl:param name="chunk.first.sections" select="1"/>

    <!-- preface:
           Output non sect1 child elements before the TOC -->
    <!-- The original template is in {docbook-xsl}/xhtml/components.xsl -->
  <xsl:template match="preface">
    <xsl:call-template name="id.warning"/>
    <div>
      <xsl:apply-templates select="." mode="class.attribute"/>
      <xsl:call-template name="dir">
        <xsl:with-param name="inherit" select="1"/>
      </xsl:call-template>
      <xsl:call-template name="language.attribute"/>
      <xsl:if test="$generate.id.attributes != 0">
        <xsl:attribute name="id">
          <xsl:call-template name="object.id"/>
        </xsl:attribute>
      </xsl:if>
      <xsl:call-template name="component.separator"/>
      <xsl:call-template name="preface.titlepage"/>
      <xsl:apply-templates/>
      <xsl:variable name="toc.params">
        <xsl:call-template name="find.path.params">
          <xsl:with-param name="table" select="normalize-space($generate.toc)"/>
        </xsl:call-template>
      </xsl:variable>
      <xsl:if test="contains($toc.params, 'toc')">
        <xsl:call-template name="component.toc">
          <xsl:with-param name="toc.title.p" select="contains($toc.params, 'title')"/>
        </xsl:call-template>
        <xsl:call-template name="component.toc.separator"/>
      </xsl:if>
      <xsl:call-template name="process.footnotes"/>
    </div>
  </xsl:template>

    <!-- chapter:
           Output non sect1 child elements before the TOC -->
    <!-- The original template is in {docbook-xsl}/xhtml/components.xsl -->
  <xsl:template match="chapter">
    <xsl:call-template name="id.warning"/>
    <div>
      <xsl:apply-templates select="." mode="class.attribute"/>
      <xsl:call-template name="dir">
        <xsl:with-param name="inherit" select="1"/>
      </xsl:call-template>
      <xsl:call-template name="language.attribute"/>
      <xsl:if test="$generate.id.attributes != 0">
        <xsl:attribute name="id">
          <xsl:call-template name="object.id"/>
        </xsl:attribute>
      </xsl:if>
      <xsl:call-template name="component.separator"/>
      <xsl:call-template name="chapter.titlepage"/>
      <xsl:apply-templates/>
      <xsl:variable name="toc.params">
        <xsl:call-template name="find.path.params">
          <xsl:with-param name="table" select="normalize-space($generate.toc)"/>
        </xsl:call-template>
      </xsl:variable>
      <xsl:if test="contains($toc.params, 'toc')">
        <xsl:call-template name="component.toc">
          <xsl:with-param name="toc.title.p" select="contains($toc.params, 'title')"/>
        </xsl:call-template>
        <xsl:call-template name="component.toc.separator"/>
      </xsl:if>
      <xsl:call-template name="process.footnotes"/>
    </div>
  </xsl:template>

    <!-- sect1:
           When there is a role attibute, use it as the class value.
           Process the SVN keywords found in sect1info as a footnote.
           Removed unused code. -->
    <!-- The original template is in {docbook-xsl}/xhtml/sections.xsl -->
  <xsl:template match="sect1">
    <div>
      <xsl:choose>
        <xsl:when test="@role">
          <xsl:attribute name="class">
            <xsl:value-of select="@role"/>
          </xsl:attribute>
        </xsl:when>
        <xsl:otherwise>
          <xsl:apply-templates select="." mode="class.attribute"/>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:call-template name="language.attribute"/>
      <xsl:call-template name="sect1.titlepage"/>
      <xsl:apply-templates/>
      <xsl:apply-templates select="sect1info" mode="svn-keys"/>
    </div>
  </xsl:template>

    <!-- sect2:
           When there is a role attibute, use it as the class value.
           Removed unused code. -->
    <!-- The original template is in {docbook-xsl}/xhtml/sections.xsl -->
  <xsl:template match="sect2">
    <div>
      <xsl:choose>
        <xsl:when test="@role">
          <xsl:attribute name="class">
            <xsl:value-of select="@role"/>
          </xsl:attribute>
        </xsl:when>
        <xsl:otherwise>
          <xsl:attribute name="class">
            <xsl:value-of select="name(.)"/>
          </xsl:attribute>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:call-template name="language.attribute"/>
      <xsl:call-template name="sect2.titlepage"/>
      <xsl:apply-templates/>
    </div>
  </xsl:template>

    <!-- sect3: treat as sect2 (for Python and Perl modules
           When there is a role attibute, use it as the class value.
           Removed unused code. -->
    <!-- The original template is in {docbook-xsl}/xhtml/sections.xsl -->
  <xsl:template match="sect3">
    <div>
      <xsl:choose>
        <xsl:when test="@role">
          <xsl:attribute name="class">
            <xsl:value-of select="@role"/>
          </xsl:attribute>
        </xsl:when>
        <xsl:otherwise>
          <xsl:attribute name="class">
            <xsl:value-of select="name(.)"/>
          </xsl:attribute>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:call-template name="language.attribute"/>
      <xsl:call-template name="sect3.titlepage"/>
      <xsl:apply-templates/>
    </div>
  </xsl:template>

    <!-- sect1info mode svn-keys:
           Self-made template to process SVN keywords found in sect1info. -->
  <xsl:template match="sect1info" mode="svn-keys">
    <p class="updated">Atualizada mais recentemente <!-- by
      <xsl:apply-templates select="othername" mode="svn-keys"/> -->
      em
      <xsl:apply-templates select="date" mode="svn-keys"/>
    </p>
  </xsl:template>

    <!-- othername mode svn-keys:
           Self-made template to process the $LastChangedBy SVN keyword. -->
  <xsl:template match="othername" mode="svn-keys">
    <xsl:variable name="author">
      <xsl:value-of select="."/>
    </xsl:variable>
    <xsl:variable name="nameonly">
      <xsl:value-of select="substring($author,16)"/>
    </xsl:variable>
    <xsl:value-of select="substring-before($nameonly,'$')"/>
  </xsl:template>

    <!-- date mode svn-keys:
           Self-made template to process the $Date SVN keyword. -->
  <xsl:template match="date" mode="svn-keys">
    <xsl:variable name="date">
      <xsl:value-of select="."/>
    </xsl:variable>
    <xsl:value-of select="substring($date,7,26)"/>
  </xsl:template>

</xsl:stylesheet>
