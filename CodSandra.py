#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 22:01:43 2020

@author: afflorezr
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:44:05 2020

@author: afflorezr
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:41:06 2020

@author: afflorezr
"""

#Import library essentials
#Import library essentials

import PyPDF2
from sumy.parsers.plaintext import PlaintextParser #We're choosing a plaintext parser here, other parsers available for HTML etc.
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lsa import LsaSummarizer #We're choosing Luhn, other algorithms are also built in
from sumy.summarizers.lex_rank import LexRankSummarizer


<<<<<<< HEAD
<<<<<<< HEAD
for i in range(18,267):
    page = read_pdf.getPage(i)
    page_content = page.extractText().replace("\n","")
    parser = PlaintextParser.from_string(page_content, Tokenizer("portuguese"))
    summarizer_lsa = LsaSummarizer()
    summaries.append(list(summarizer_lsa(parser.document,3)))
    parser_rank = PlaintextParser.from_string(page_content, Tokenizer("portuguese"))
    summarizer_lex = LexRankSummarizer()
    summaries_Rank.append(list(summarizer_lex(parser_rank.document,3)))

print(pdf_file)
## segunda modificação
##
=======



## 
## pequena modificação

=======

>>>>>>> 4aafb23218f88657483e1737f400ac76a22efd92
